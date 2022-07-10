from sklearn.model_selection import train_test_split
import numpy as np
import os
import shutil
from pathlib import Path

min_Dir_Path = 'D:/Git_WorkSpace/ITSEC21/data/U_Are_U/Minutiae/resize/minutiaeMaps_40/'
fin_Dir_Path = 'D:/Git_WorkSpace/ITSEC21/data/U_Are_U/FingerPrints/resize/FingerPrints_All/'

dest_Min_Path = 'D:/Git_WorkSpace/ITSEC21/data/U_Are_U/model_Data/USplit5/A/'
dest_Fing_Path = 'D:/Git_WorkSpace/ITSEC21/data/U_Are_U/model_Data/USplit5/B/'

Path('D:/Git_WorkSpace/ITSEC21/data/U_Are_U/model_Data/USplit5').mkdir(parents=True, exist_ok=True)
Path(dest_Min_Path).mkdir(parents=True, exist_ok=True)
Path(dest_Fing_Path).mkdir(parents=True, exist_ok=True)


fileNames = []
for file in os.listdir(min_Dir_Path):
    fileNames.append(file)


train, test = train_test_split(fileNames, test_size=0.2)

#Train Data
Path(dest_Min_Path + 'train/').mkdir(parents=True, exist_ok=True)
Path(dest_Fing_Path + 'train/').mkdir(parents=True, exist_ok=True)
for file in train:
    shutil.copy2(min_Dir_Path + file, dest_Min_Path + 'train/' + file)
    shutil.copy2(fin_Dir_Path + file, dest_Fing_Path + 'train/' + file)


# Test Data
Path(dest_Min_Path + 'test/').mkdir(parents=True, exist_ok=True)
Path(dest_Fing_Path + 'test/').mkdir(parents=True, exist_ok=True)
for file in test:
    shutil.copy2(min_Dir_Path + file, dest_Min_Path + 'test/' + file)
    shutil.copy2(fin_Dir_Path + file, dest_Fing_Path + 'test/' + file)

# Val Data
Path(dest_Min_Path + 'val/').mkdir(parents=True, exist_ok=True)
Path(dest_Fing_Path + 'val/').mkdir(parents=True, exist_ok=True)
for file in test:
    shutil.copy2(min_Dir_Path + file, dest_Min_Path + 'val/' + file)
    shutil.copy2(fin_Dir_Path + file, dest_Fing_Path + 'val/' + file)