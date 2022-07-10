import splitfolders


# Finger Prints Path
Finger_Inp_Path = "D:/Git_WorkSpace/ITSEC21/data/CrossMatch_Sample_DB/FingerPrints/resize/FingerPrints_All/"
Finger_Out_Path = "D:/Git_WorkSpace/ITSEC21/data/CrossMatch_Sample_DB/model_Data/B/"

# Minutiae maps path
Min_Inp_Path = "D:/Git_WorkSpace/ITSEC21/data/CrossMatch_Sample_DB/Minutiae/resize/minutiaeMaps_All/"
# Min_Inp_Path = "D:/Git_WorkSpace/ITSEC21/data/re_pre-Process/Minutiae/resize/minutiaeMaps20_256/"
# Min_Inp_Path = "D:/Git_WorkSpace/ITSEC21/data/re_pre-Process/Minutiae/resize/minutiaeMaps40_256/"

# Save the train, test, val directories
Min_Out_Path = (
    "D:/Git_WorkSpace/ITSEC21/data/CrossMatch_Sample_DB/model_Data/A/"
)

# Min_Out_Path = (
#     "D:/Git_WorkSpace/ITSEC21/data/re_pre-Process/model_Data/minutiae_Maps_20"
# )
# Min_Out_Path = (
#     "D:/Git_WorkSpace/ITSEC21/data/re_pre-Process/model_Data/minutiae_Maps_40"
# )


# https://pypi.org/project/split-folders/
# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
# splitfolders.ratio(Finger_Inp_Path,
#                     output=Finger_Out_Path,
#                     seed=1337,
#                     ratio=(.7, .1, .2))
# splitfolders.ratio(Finger_Inp_Path, output=Finger_Out_Path, seed=1337, ratio=(0.8, 0.2))
splitfolders.ratio(Min_Inp_Path, output=Min_Out_Path, seed=1337, ratio=(0.8, 0.2))