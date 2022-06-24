from PIL import Image
import os
import sys
from tqdm import tqdm


def read_files(dir_path):
    """This function reads the unique fake file names. 

    :param dir_path: the gan generated fingerprints path.
    :return: Returns fake file names.
    """
    files = os.listdir(dir_path)
    unique_files = []
    for index, image in enumerate(files):
        if image.endswith("fake_B.png"):
            len1 = len(image)
            len2 = len(image[-11:])
            len3 = len1 - len2
            unique_files.append(image[:len3])
    
    return unique_files


def upscale_fake(image_name, input_dir, output_dir):
    """This function upscales and saves the given fake image. 

    :param input_dir: the gan generated fingerprints path.
    :param output_dir: the save path of upscaled images.
    :return: Returns None.
    """

    fake_img_path = input_dir + "/" + image_name + ".png"
    img = Image.open(fake_img_path)
    img = img.resize((512,512), Image.ANTIALIAS)
    img.save(
        output_dir + "/" + image_name + ".png", dpi=(500, 500), quality=500
    )


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
    
    # get the unique files
    unique_files = read_files(input_dir)

    # loop over the entire gan generated results
    for index, filename in enumerate(tqdm(unique_files)):

        upscale_fake(filename, input_dir, output_dir)


if __name__ == '__main__':
    main()