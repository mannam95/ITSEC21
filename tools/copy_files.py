import os
import sys
import PIL
import shutil


def copy_files(input_dir, source_dir, dest_dir):
    """This function copies the original files from the given train dataset. 

    :param input_dir: file names directory.
    :param source_dir: source image directory.
    :param dest_dir: destination image directory.
    :return: Returns None.
    """
    files = os.listdir(input_dir)
    for index, image_name in enumerate(files):
        source_img_path = source_dir + "/" + image_name
        dest_img_path = dest_dir + "/" + image_name
        shutil.copy(source_img_path, dest_img_path)



def main():

    if ( len(sys.argv) < 3 ):
        print('Usage: python '+sys.argv[0]+ ' <inp_dir> <des_dir> <src_dir>')
        print('\tinp_dir: this folder contains image files.')
        print('\tdes_dir: this folder is the dest image files.')
        print('\tsrc_dir: Use this option if source of the file is located in different directory with same file name located in input directory.')
        sys.exit(0)

    # parse command line parameters
    input_dir =  sys.argv[1]
    src_dir = input_dir

    des_dir = sys.argv[2]
    if not os.path.exists(des_dir):
        os.makedirs(des_dir)

    if ( len(sys.argv) == 4 ):
        src_dir = sys.argv[3]

    # copy files
    copy_files(input_dir, src_dir, des_dir)


if __name__ == '__main__':
    main()