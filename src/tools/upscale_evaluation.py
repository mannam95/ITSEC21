import os
import sys
from subprocess32 import check_output
from tqdm import tqdm


def read_files(dir_path):
    """This function reads all the files in the given directory. 

    :param dir_path: the fingerprints directory path.
    :return: Returns filenmes list.
    """

    files = os.listdir(dir_path)
    unique_files = []
    # Read all the files
    for index, fp_image_file in enumerate(files):
        unique_files.append(fp_image_file)
    
    return unique_files


def evaluate_with_verifinger(real_path, fake_path, unique_files):
    """This function does the evaluation with verifinger. 

    :param real_path: the real images path.
    :param fake_path: the fake images path.
    :return: Returns None.
    """
    
    score36 = 0
    score48 = 0
    score60 = 0

    # Process each image file
    for index, filename in enumerate(tqdm(unique_files)):
        print ('file num: ', index, ' and file name', filename)

        img1Path = real_path + "/" + filename
        img2Path = fake_path + "/" + filename

        try:

            # Use this in SSH
            r = check_output( ['Verifinger1toN', img1Path, img2Path], timeout=60 )
            print(r)
            lines = r.split(b';')
            score = int(lines[2].decode("utf-8"))

            # Use this in local system
            # score = random.randint(20,100)


            print("Score: ", score)
            if score >= 36:
                score36 = score36 + 1

            if score >= 48:
                score48 = score48 + 1

            if score >= 60:
                score60 = score60 + 1
            
        except:
            print("Couldn't execute the fingerprint")
            continue
    
    return (score36, score48, score60)

def main():

    if ( len(sys.argv) < 3 ):
        print('Usage: python '+sys.argv[0]+ ' <input_dir> <output_dir>')
        print('\treal_fing_dir: this folder should include the real upscaled 512*512 images')
        print('\tfake_fing_dir: this folder should include the real upscaled 512*512 images')
        sys.exit(0)

    # parse command line parameters
    real_fing_dir =  sys.argv[1]
    fake_fing_dir = sys.argv[2]

    # get the unique files
    unique_files = read_files(real_fing_dir)

    # call the evaluation function
    (score36, score48, score60) = evaluate_with_verifinger(real_fing_dir, fake_fing_dir, unique_files)

    print("Evaluation total images: ", len(unique_files))
    print("Evaluation images that didn't met the any criteria: ", len(unique_files) - score36)
    print("Score 36: ", score36, " images passed")
    print("Score 48: ", score48, " images passed")
    print("Score 60: ", score60, " images passed")


if __name__ == '__main__':
    main()