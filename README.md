# csg_imagenet
Python Version: This project requires Python 3.7. It will not work with Python 3.8 or above.

Steps:

1. On command line type in  the following
 `export DATASET_ROOT=$PWD`  or `set DATASET_ROOT=%cd%` on windows
2. Move the imagenet data folder to the root directory of this project
3. Download the requiremetns using 'pip install -r requirements.txt' 
4. If you want to crop the images to a standard size, uncomment the code on lines 56 & 74 in pectral_metric/handle_datasets.py. Line 41 is where you can set what this standard dimension is
5. Use the command `python main.py imagenet --embd embd` to get both the embedding and csg for imagenet
