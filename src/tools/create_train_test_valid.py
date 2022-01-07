import splitfolders


# Finger Prints Path
Finger_Inp_Path = "D:/Git_WorkSpace/ITSEC21/data/initial_Pre_Process_data/FingerPrints/Fingerprint_Images_256_1Channel_JPG/"
Finger_Out_Path = "D:/Git_WorkSpace/ITSEC21/data/model_Train_Data/FingerPrints/"

# Minutiae maps path
# Min_Inp_Path = "D:/Git_WorkSpace/ITSEC21/data/initial_Pre_Process_data/Minutiae/Minutiae_Map_Images_256_JPG/"
# Min_Inp_Path = "D:/Git_WorkSpace/ITSEC21/data/initial_Pre_Process_data/Minutiae/minutiaeMaps20_256/"
Min_Inp_Path = "D:/Git_WorkSpace/ITSEC21/data/initial_Pre_Process_data/Minutiae/minutiaeMaps40_256/"

# Save the train, test, val directories
# Min_Out_Path = (
#     "D:/Git_WorkSpace/ITSEC21/data/model_Train_Data/Minutiae_Maps/minutiae_Maps_All"
# )
# Min_Out_Path = (
#     "D:/Git_WorkSpace/ITSEC21/data/model_Train_Data/Minutiae_Maps/minutiae_Maps_20"
# )
Min_Out_Path = (
    "D:/Git_WorkSpace/ITSEC21/data/model_Train_Data/Minutiae_Maps/minutiae_Maps_40"
)


# https://pypi.org/project/split-folders/
# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
# splitfolders.ratio(Finger_Inp_Path,
#                     output=Finger_Out_Path,
#                     seed=1337,
#                     ratio=(.7, .1, .2))
splitfolders.ratio(Min_Inp_Path, output=Min_Out_Path, seed=1337, ratio=(0.7, 0.1, 0.2))
