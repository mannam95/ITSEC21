from PIL import Image
import os
import sys
from tqdm import tqdm
import shutil
import numpy as np


def filter_empty_images(input_dir, output_dir):
    """This function removes the empty images in the given directory and copies them into the given directory. 

    :param input_dir: source image directory.
    :param output_dir: destination image directory.
    :return: Returns None.
    """
    files = os.listdir(input_dir)
    count = 0
    for index, image_name in enumerate(tqdm(files)):
        source_img_path = input_dir + "/" + image_name
        img = Image.open(source_img_path)
        num_img = np.array(img)
        img_splits = np.split(num_img, 2, axis=1)

        if np.min(img_splits[1]) == np.max(img_splits[1]):
            count = count + 1
            print("skipping: ", image_name)
        else :
            dest_img_path = output_dir + "/" + image_name
            shutil.copy(source_img_path, dest_img_path)
    print("Total images skipped copying: ", count)


def main():

    if ( len(sys.argv) < 3 ):
        print('Usage: python '+sys.argv[0]+ ' <input_dir> <output_dir>')
        print('\tinput_dir: this folder should include the gan generated images')
        print('\toutput_dir: this folder is the folder where rescaled images are stored')
        sys.exit(0)

    # parse command line parameters
    input_dir =  sys.argv[1]

    output_dir = sys.argv[2]
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    filter_empty_images(input_dir, output_dir)


if __name__ == '__main__':
    main()