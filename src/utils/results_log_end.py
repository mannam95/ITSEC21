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