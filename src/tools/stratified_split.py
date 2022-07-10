from posixpath import split
import numpy as np
import os
from sklearn.model_selection import StratifiedKFold
import shutil
import sys

files = []

def read_files(dir_path):
    """This function reads all the files. 

    :param dir_path: the fingerprints directory path.
    :return: Returns (X, y) tuple for splitting.
    """
    _X, _y, _files = [], [], []
    for file in os.listdir(dir_path):
        person_fingerprint_name = "_".join(file.split("_", 2)[:2])
        _files.append(file)
        if person_fingerprint_name not in _X:
            _X.append(person_fingerprint_name)
            _y.append(file.split("_", 2)[0])
    global files
    files = _files.copy()
    return (np.sort(np.asarray(_X)), np.sort(np.asarray(_y)))


def k_stratified_splits(input_dir,k=5):
    """This function does stratified k splits. 

    :param input_dir: input directory of files.
    :param k: splits length.
    :return: Returns the k stratified splits, each split as (train, test) tuple.
    """
    skf = StratifiedKFold(n_splits=k)
    (X, y) = read_files(input_dir)
    X_train_split, X_test_split = [], []
    for train_index, test_index in skf.split(X, y):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        X_train_split.append(X_train)
        X_test_split.append(X_test)
    
    return (X_train_split, X_test_split)

def create_k_folders(output_dir,folder_prefix):
    """This function creates the k directories. 

    :param output_dir: output directory of files.
    :return: Returns the (train_path, test_path) path.
    """
    path = os.path.join(output_dir, 'folder_'+str(folder_prefix+1))
    train_path = os.path.join(path, "train")
    test_path = os.path.join(path, "test")

    if (os.path.exists(train_path) == False):
        os.makedirs(train_path)
    if (os.path.exists(test_path) == False):
        os.makedirs(test_path)
    
    return (train_path, test_path)

def copy_file(train_test_data, input_dir, train_path, test_path):
    """This function copies files recursively to the specified fold train, test. 

    :param train_test_data: (train_split, test_split) as a tuple.
    :param input_dir: input directory of files.
    :param train_path: train folder path.
    :param test_path: test folder path.
    :return: Returns None.
    """
    X_train_split, X_test_split = train_test_data
    for fingerprint in X_train_split: # loop over at fingerprint level.
        variations = [s for s in files if fingerprint in s] # get all variations for the current fingerprint.
        for current_variation in variations:
            train_source_path = input_dir + '/' + str(current_variation)  
            train_destination_path = str(train_path) + '/' + str(current_variation)    
            if (train_source_path):
                shutil.copy2(train_source_path, train_destination_path)
        
    for fingerprint in X_test_split: # loop over at fingerprint level.
        variations = [s for s in files if fingerprint in s] # get all variations for the current fingerprint.
        for current_variation in variations:
            test_source_path = input_dir + '/' + str(current_variation)  
            test_destination_path = str(test_path) + '/' + str(current_variation)
            if (test_source_path):
                shutil.copy2(test_source_path, test_destination_path)

def store_k_splits(input_dir, output_dir):
    """This function performs each mentioned step. 

    :param input_dir: input directory of files.
    :param output_dir: OUTPUT directory of files.
    :return: Returns None.
    """
    (X_train_split, X_test_split) = k_stratified_splits(input_dir, 5)
    
    for index, split_data in enumerate(zip(X_train_split, X_test_split)):
        (train_path, test_path) = create_k_folders(output_dir, index)
        copy_file(split_data, input_dir, train_path, test_path)

def main():

    if ( len(sys.argv) < 3 ):
        print('Usage: python '+sys.argv[0]+ ' <input_dir> <output_dir>')
        print('\tinput_dir: this folder should include image files only')
        print('\toutput_dir: stratified splits will be saved in this main directory')
        sys.exit(0)
    
    input_dir =  sys.argv[1]

    output_dir = sys.argv[2]
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    store_k_splits(input_dir, output_dir)


if __name__ == '__main__':
    main()


stratified_split.py
