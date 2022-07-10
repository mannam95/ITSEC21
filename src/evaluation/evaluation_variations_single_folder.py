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



def read_files_split_into_groups(dir_path):
    """This function separates into groups by second underscore. 

    :param dir_path: the fingerprints directory path.
    :return: Returns all groups.
    """
    
    groups = defaultdict(list)
    files = read_files(dir_path)

    groups =  [list(g) for _, g in itertools.groupby(sorted(files), lambda x: x[0:[m.start() for m in re.finditer(r"_",x)][1]])]

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
      for ind, fing_class in enumerate(tqdm(fingerprints_list, desc='Class Loop')):
        # Loop over each variation
        for sub_ind, variation in enumerate(tqdm(fing_class, desc='Variation Loop')):
          try:
              print("\nProcessing Class {0}/{1} and the variation({2}/{3}) is {4}".format(ind, len(fingerprints_list), sub_ind, len(fing_class), variation))
              
              class_copy = fing_class.copy()
              
              # get remove current variation
              class_copy.remove(variation)

              # get all the verifinger execution in a list
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
    log_end_summary_scores(score36, score48, score60, count, eval_file_path)


def main():

    if ( len(sys.argv) < 3 ):
        print('Usage: python '+sys.argv[0]+ ' <input_dir>')
        print('\t input_dir: this folder should include all the images generated by gan')
        print('\n eval_dir: the results will be stored in this folder')
        sys.exit(0)

    # parse command line parameters
    input_dir =  sys.argv[1]

    eval_dir =  sys.argv[2]
    if not os.path.exists(eval_dir):
        os.makedirs(eval_dir)

    eval_file_path = eval_dir + '/latest.txt'

    # get the unique classes
    all_files = read_files_split_into_groups(input_dir)

    # call the evaluation function
    evaluate_with_verifinger(input_dir, all_files, eval_file_path)


if __name__ == '__main__':
    main()