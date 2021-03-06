import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(PROJECT_ROOT)
from utils.read_files import read_files
from utils.verifinger_single_evaluate import evaluate_single_verifinger


def main():

    if ( len(sys.argv) < 4 ):
        print('Usage: python '+sys.argv[0]+ ' <input_dir>')
        print('\t input_dir: this folder should include all the images generated by gan')
        print('\t eval_dir: the results will be stored in this folder')
        print('\t eval_file_name: the name of the file that results should be stored')
        sys.exit(0)

    # parse command line parameters
    input_dir =  sys.argv[1]
    eval_dir =  sys.argv[2]
    if not os.path.exists(eval_dir):
        os.makedirs(eval_dir)
    eval_filename =  sys.argv[3]

    eval_file_path = eval_dir + '/' + eval_filename

    # get the unique files
    unique_files = read_files(input_dir)

    # call the evaluation function
    evaluate_single_verifinger(input_dir, unique_files, eval_file_path)


if __name__ == '__main__':
    main()