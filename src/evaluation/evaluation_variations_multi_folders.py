import os
import sys
import base64
import json
from subprocess32 import check_output
from tqdm import tqdm
import random
from collections import defaultdict
import itertools
import re


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


def read_files_split_into_groups(dir_path, underscore_index):
    """This function separates into groups by second underscore. 

    :param dir_path: the fingerprints directory path.
    :return: Returns all groups.
    """
    
    groups = defaultdict(list)
    files = read_files(dir_path)

    groups =  [list(g) for _, g in itertools.groupby(sorted(files), lambda x: x[0:[m.start() for m in re.finditer(r"_",x)][underscore_index]])]

    return groups


def log_end_summary_scores(score36, score48, score60, count, eval_file_path):
    """This function logd the end summary results inside the eval.txt file 

    :param dir_path: the fingerprints directory path.
    :param fingerprints_list: all fingerprints at class level.
    :return: Returns None.
    """

    with open(eval_file_path, 'a') as f:

        print1 = "Evaluation total images: " + str(count)
        print2 = "Evaluation total images: " + "Evaluation images that didn't met the any criteria: " + str(count - score36)
        print3 = "Score 36: " + str(score36) + " images passed"
        print4 = "Score 48: " + str(score48) + "images passed"
        print5 = "Score 60: " + str(score60) + "images passed"

        f.write('\n')
        f.write("Below are results") # End Footer
        f.write('\n')
        f.write(print1)
        f.write('\n')
        f.write(print2)
        f.write('\n')
        f.write(print3)
        f.write('\n')
        f.write(print4)
        f.write('\n')
        f.write(print5)
        f.write('\n')

        print(print1)
        print(print2)
        print(print3)
        print(print4)
        print(print5)
        print("\n")


def evaluate_with_verifinger(dir_path, fingerprints_list, eval_file_path):
    """This function does the evaluation with verifinger. 

    :param dir_path: the fingerprints directory path.
    :param fingerprints_list: all fingerprints at class level.
    :return: Returns matching scores.
    """

    score36 = 0
    score48 = 0
    score60 = 0
    count = 0

    with open(eval_file_path, 'w') as f:
      f.truncate(0) # Clear the existing content
      f.write("realfingerprint;fakefingerprint;matchingscore") # Headers
      f.write('\n')

      # Loop over each class
      for ind, fing_class in enumerate(fingerprints_list):
        # Loop over each variation
        for sub_ind, variation in enumerate(fing_class):
          try:
              print("\nProcessing Class {0}/{1} and the variation({2}/{3}) is {4}".format(ind, len(fingerprints_list), sub_ind, len(fing_class), variation))

              class_copy = fing_class.copy()
              # get remove current variation.
              class_copy.remove(variation)

              # get all the verifinger execution in a list.
              verifinger_list = ['Verifinger1toN']
              real_image_Path = dir_path + '/' + variation + 'real_B.png'
              verifinger_list.append(real_image_Path)
              fake_images_path = [dir_path + '/' + s + 'fake_B.png' for s in class_copy]
              verifinger_list = verifinger_list + fake_images_path

              # update the counter.
              count = count + len(class_copy)

              # Use this in SSH
              output = check_output( verifinger_list, timeout=60 )
              lines = output.split(b'\n')

              # Process the output of verifinger
              for line in lines:
                split_line = line.split(b';')
                if len(split_line) > 0 and '/vol1/itsec_1' in split_line[0].decode("utf-8"):
                  img1_name = os.path.basename(split_line[0].decode("utf-8"))
                  img2_name = split_line[1].decode("utf-8")
                  score = int(split_line[2].decode("utf-8"))

                  write_output = img1_name + ";" + img2_name + ";" + str(score)
                  f.write(write_output)
                  f.write('\n')

                  print("The matching score of variation:{0} vs variation:{1} is {2}\n".format(img1_name, img2_name, score))                
              
                  if score >= 36:
                    score36 = score36 + 1
                  
                  if score >= 48:
                    score48 = score48 + 1

                  if score >= 60:
                    score60 = score60 + 1
          except Exception as ex:
              template = "An exception of type {0} occurred at first try block. Arguments:\n{1!r}"
              message = template.format(type(ex).__name__, ex.args)
              print(message)
              continue
        #       break
        #   break
        # break
    log_end_summary_scores(score36, score48, score60, count, eval_file_path)


def main():

    root_start_path = '/vol1/itsec_1/pytorch-CycleGAN-and-pix2pix/results/'
    root_end_path = '/test_latest/images'

    eval_list = ['new_CM_5_S3_Fold1', 'new_CM_5_S3_Fold2', 
                 'new_CM_5_S3_Fold3_v2', 'new_CM_5_S3_Fold4', 
                 'new_CM_5_S3_Fold5', 'new_URU_5_S3_Fold1_lr_1e_2', 
                 'new_URU_5_S3_Fold2_lr_1e_2', 'new_URU_5_S3_Fold3_lr_1e_2',
                 'new_URU_5_S3_Fold4_lr_1e_2', 'new_URU_5_S3_Fold5_lr_1e_2',
                 'new_CM_5_S3_Fold1_Aug', 'new_URU_5_S3_Fold2_lr_1e_2_Aug',
                 'neuro_CM_train_fvc_CM_test', 'fvc_CM_train_neuro_CM_test',
                 'neuro_URU_train_fvc_URU_test', 'fvc_URU_train_neuro_URU_test',
                 'neuro_CM_train_neuro_URU_test', 'fvc_CM_train_fvc_URU_test',
                 'neuro_URU_train_neuro_CM_test', 'fvc_URU_train_fvc_CM_test'
                ]
    und_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0]


    for index, folder_name in enumerate(tqdm(eval_list)):

        eval_file_path = '/vol1/itsec_1/new_exp/evaluation/type2_real_vs_fake/' + folder_name + '.txt'
        
        print("Processing ", folder_name)

        if index >= 16:
            input_dir = root_start_path + 'cross_sensor/' + folder_name + root_end_path
        else:
            input_dir = root_start_path + folder_name + root_end_path

        underscore_index = und_list[index]
        # get the unique classes
        all_files = read_files_split_into_groups(input_dir, underscore_index)

        # call the evaluation function
        evaluate_with_verifinger(input_dir, all_files, eval_file_path)
        

if __name__ == '__main__':
    main()