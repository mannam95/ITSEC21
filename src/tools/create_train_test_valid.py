import splitfolders


Finger_Inp_Path = "D:/Git_WorkSpace/ITSEC21/data/initial_Pre_Process_data/FingerPrints/Fingerprint_Images_256_1Channel_JPG/"
Finger_Out_Path = "D:/Git_WorkSpace/ITSEC21/data/FingerPrints/"
Min_Inp_Path = "D:/Git_WorkSpace/ITSEC21/data/initial_Pre_Process_data/Minutiae/Minutiae_Map_Images_256_JPG/"
Min_Out_Path = "D:/Git_WorkSpace/ITSEC21/data/Minutiae_Maps/"
# https://pypi.org/project/split-folders/
# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
splitfolders.ratio(Finger_Inp_Path, 
                    output=Finger_Out_Path, 
                    seed=1337, 
                    ratio=(.7, .1, .2))

splitfolders.ratio(Min_Inp_Path, 
                    output=Min_Out_Path, 
                    seed=1337, 
                    ratio=(.7, .1, .2))