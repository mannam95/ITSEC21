import os
from subprocess import check_output
from tqdm import tqdm
from utils.results_log_end import log_end_summary_scores


def evaluate_variations_verifinger(dir_path, fingerprints_list, eval_file_path):
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