import sys
from utils.read_files import read_files
from utils.verifinger_single_evaluate import evaluate_single_verifinger


def main():

    if ( len(sys.argv) < 2 ):
        print('Usage: python '+sys.argv[0]+ ' <input_dir>')
        print('\tinput_dir: this folder should include all the images generated by gan')
        sys.exit(0)

    # parse command line parameters
    input_dir =  sys.argv[1]

    # get the unique files
    unique_files = read_files(input_dir)

    # call the evaluation function
    evaluate_single_verifinger(input_dir, unique_files)


if __name__ == '__main__':
    main()