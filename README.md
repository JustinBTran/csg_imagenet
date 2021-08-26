# csg_imagenet
Python Version: This project requires Python 3.7. It will not work with Python 3.8 or above.

Steps:

1. On command line type in  the following\n
 `export DATASET_ROOT=$PWD`  or `set DATASET_ROOT=%cd%` on windows
2. Move the imagenet data folder to the root directory of this project
3. Download the requiremetns using 'pip install -r requirements.txt' 
4. On line 41 of spectral_metric/handle_datasets.py, change the image_dim to match the dimensions of the images in imagenet 
5. Use the command `python main.py imagenet --embd embd` to get both the embedding and csg for imagenet
PS there are some dll errors that we are facing on the windows machine, but we are hoping they should work on the u of t PCs. Let us know. 
