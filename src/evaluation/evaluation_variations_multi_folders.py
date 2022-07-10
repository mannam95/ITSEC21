import os
import sys
sys.path.insert(0, '../utils')
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(PROJECT_ROOT)
from utils.split_files_into_groups import read_files_split_into_groups
from utils.verifinger_variations_evaluate import evaluate_variations_verifinger
from tqdm import tqdm


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
        evaluate_variations_verifinger(input_dir, all_files, eval_file_path)
        

if __name__ == '__main__':
    main()