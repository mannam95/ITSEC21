"""This module contains simple helper functions """
import os


def read_files(dir_path):
    """This function reads the unique fake file names. 

    :param dir_path: the fingerprints directory path.
    :return: Returns None.
    """

    files = os.listdir(dir_path)
    unique_files = []
    # Read all the files
    for index, fp_image_file in enumerate(files):
        if fp_image_file.endswith("fake_B.png"):
            len1 = len(fp_image_file)
            len2 = len(fp_image_file[-10:])
            len3 = len1 - len2
            unique_files.append(fp_image_file[:len3])
    
    return unique_files