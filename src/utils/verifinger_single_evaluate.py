import os
from subprocess import check_output
from tqdm import tqdm
from results_log_end import log_end_summary_scores


def evaluate_single_verifinger(dir_path, unique_files, eval_file_path):
    """This function does the evaluation with verifinger. 

    :param dir_path: the fingerprints directory path.
    :return: Returns None.
    """
    
    score36 = 0
    score48 = 0
    score60 = 0

    with open(eval_file_path, 'w') as f:
        f.truncate(0) # Clear the existing content
        f.write("fakefingerprint;realfingerprint;matchingscore") # Headers
        f.write('\n')
        # Process each image file
        for index, filename in enumerate(tqdm(unique_files)):
            print ('file num: ', index, ' and file name', filename)

            img1Path = dir_path + "/" + filename + "real_B.png"
            img2Path = dir_path + "/" + filename + "fake_B.png"

            try:

                # Verifinger1toN should be installed.
                output = check_output( ['Verifinger1toN', img1Path, img2Path], timeout=60 )
                lines = output.split(b'\n')
                

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
                # break
                
            except Exception as ex:
                template = "An exception of type {0} occurred at first try block. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                print(message)
                continue
        
        log_end_summary_scores(score36, score48, score60, len(unique_files), eval_file_path)