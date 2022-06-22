from posixpath import split
import numpy as np
import os
from sklearn.model_selection import StratifiedKFold
import shutil

parent_dir = '/home/srinath/Documents/itsec_new/neuro/UareU_sample_DB'
save_splits_dir = '/home/srinath/Documents/itsec_new/neuro/CrossMatchCombined/model_data/CrossMatch_5_SplitsV1'
files = []

def read_files(dir_path):
    """This function adds the padding to the given image. 

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


def k_stratified_splits(k=5):
    """This function does stratified k splits. 

    :param k: splits length.
    :return: Returns the k stratified splits, each split as (train, test) tuple.
    """
    skf = StratifiedKFold(n_splits=k)
    (X, y) = read_files(parent_dir)
    X_train_split, X_test_split = [], []
    for train_index, test_index in skf.split(X, y):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        X_train_split.append(X_train)
        X_test_split.append(X_test)
    
    return (X_train_split, X_test_split)

def create_k_folders(folder_prefix):
    """This function creates the k directories. 

    :return: Returns the (train_path, test_path) path.
    """
    main_directory = 'folder_'+str(folder_prefix+1)
    sub_train_directory = 'train'
    sub_test_directory = 'test'
    path = os.path.join(save_splits_dir, main_directory)
    train_path = os.path.join(path, sub_train_directory)
    test_path = os.path.join(path, sub_test_directory)

    if (os.path.exists(path) == False):
        os.mkdir(path)
    if (os.path.exists(path) == False):
        os.mkdir(path)
    if (os.path.exists(train_path) == False):
        os.mkdir(train_path)
    if (os.path.exists(test_path) == False):
        os.mkdir(test_path)
    
    return (train_path, test_path)

def copy_file(train_test_data, train_path, test_path):
    """This function copies files recursively to the specified fold train, test. 

    :param train_test_data: (train_split, test_split) as a tuple.
    :param train_path: train folder path.
    :param test_path: test folder path.
    :return: Returns None.
    """
    X_train_split, X_test_split = train_test_data
    for fingerprint in X_train_split: # loop over at fingerprint level.
        variations = [s for s in files if fingerprint in s] # get all variations for the current fingerprint.
        for current_variation in variations:
            train_source_path = parent_dir + '/' + str(current_variation)  
            train_destination_path = str(train_path) + '/' + str(current_variation)    
            if (train_source_path):
                shutil.copy2(train_source_path, train_destination_path)
        
    for fingerprint in X_test_split: # loop over at fingerprint level.
        variations = [s for s in files if fingerprint in s] # get all variations for the current fingerprint.
        for current_variation in variations:
            test_source_path = parent_dir + '/' + str(current_variation)  
            test_destination_path = str(test_path) + '/' + str(current_variation)
            if (test_source_path):
                shutil.copy2(test_source_path, test_destination_path)

def store_k_splits():
    """This function performs each mentioned step. 

    :return: Returns None.
    """
    (X_train_split, X_test_split) = k_stratified_splits(5)
    
    for index, split_data in enumerate(zip(X_train_split, X_test_split)):
        (train_path, test_path) = create_k_folders(index)
        copy_file(split_data, train_path, test_path)


# Call the main function
store_k_splits()



