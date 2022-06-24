import os
import sys
import PIL
import shutil


def copy_files(input_dir, output_dir):
    """This function copies the original files from the given train dataset. 

    :param input_dir: source image directory.
    :param output_dir: destination image directory.
    :return: Returns None.
    """
    files = os.listdir(input_dir)
    for index, image_name in enumerate(files):
        source_img_path = input_dir + "/" + image_name
        dest_img_path = output_dir + "/" + image_name
        shutil.copy(source_img_path, dest_img_path)



def main():

    if ( len(sys.argv) < 3 ):
        print('Usage: python '+sys.argv[0]+ ' <input_dir> <output_dir>')
        print('\tinp_dir: this folder is the source image files.')
        print('\tout_dir: this folder is the destination image files.')
        sys.exit(0)

    # parse command line parameters
    input_dir =  sys.argv[1]

    output_dir = sys.argv[2]
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # copy files
    copy_files(input_dir, output_dir)


if __name__ == '__main__':
    main()