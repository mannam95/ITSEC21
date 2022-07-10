import sys
sys.path.insert(0, '../utils')
from read_files import read_files
from verifinger_single_evaluate import evaluate_single_verifinger


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
    for index, folder_name in enumerate(eval_list):

        eval_file_path = '/vol1/itsec_1/new_exp/evaluation/type1_fake_vs_real/' + folder_name + '.txt'
        
        print("Processing ", folder_name)

        if index >= 16:
            input_dir = root_start_path + 'cross_sensor/' + folder_name + root_end_path
        else:
            input_dir = root_start_path + folder_name + root_end_path
        # get the unique files
        unique_files = read_files(input_dir)

        # call the evaluation function
        evaluate_single_verifinger(input_dir, unique_files, eval_file_path)


if __name__ == '__main__':
    main()