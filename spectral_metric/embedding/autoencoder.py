import os

import keras.backend as K
from keras import Input
from keras.layers import BatchNormalization
from keras.layers import Dense
from keras.layers import GaussianNoise

from spectral_metric.embedding.common import GenericAutoEncoder, EmbeddingGetter
from spectral_metric.embedding.utils import need_sequence
from spectral_metric.handle_datasets import all_datasets, paper_dataset, add_dataset
# from spectral_metric.handle_datasets import read_tiny_imagenet, TINY_IMAGENET
from spectral_metric.handle_datasets import read_imagenet, IMAGENET

pjoin = os.path.join


def model_fn(input_shape):
    """
    Train an AE
    Args:
        X_train: [?,?] dataset

    Returns: Layer, the embdedding layer.

    """

    inp = Input((input_shape[1:]))
    x = GaussianNoise(0.1)(inp)
    x = Dense(512)(x)
    x = BatchNormalization()(x)
    x = Dense(256)(x)
    x = BatchNormalization()(x)
    x = Dense(128)(x)
    x = BatchNormalization()(x)
    embd = Dense(264, name='embd')(x)
    x = Dense(256)(x)
    x = BatchNormalization()(x)
    x = Dense(512)(x)
    x = BatchNormalization()(x)
    x = Dense(sum(list(input_shape[1:])))(x)
    return inp, embd, x


class AutoencoderEmbd(EmbeddingGetter):
    def get_embedding(self, dat):
        if need_sequence(dat):
            return GenericAutoEncoder(model_fn,
                                      flatten=True,
                                      normalize=True).fit_generator(dat,
                                                                    batch_size=128,
                                                                    size=128).reshape([dat.shape[0], -1])
        else:
            return GenericAutoEncoder(model_fn,
                                      flatten=True,
                                      normalize=True).fit(dat,
                                                          batch_size=128).reshape([dat.shape[0], -1])

    @classmethod
    def get_embedding_name(cls):
        return 'embd'


def main():
    for k in paper_dataset:
        print(k)
        add_dataset(k, read_imagenet, IMAGENET)
        (data, target), _ = all_datasets[k]()
        AutoencoderEmbd()(data, k)
        K.clear_session()


if __name__ == '__main__':
    main()
