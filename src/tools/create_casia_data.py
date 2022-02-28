import os
from PIL import Image
import glob as glob
import cv2
import random
import numpy as np
import shutil

trainFileNames = np.load('casiaFilenames.npy')

sourceMinPath = 'D:/FingerPrint_Dataset/New_Exp/CASIA/Test_Data/A/test/'
targetMinPath1 = 'D:/FingerPrint_Dataset/New_Exp/CASIA/model_Data/A/train/'
targetMinPath2 = 'D:/FingerPrint_Dataset/New_Exp/CASIA/model_Data/A/test/'
targetMinPath3 = 'D:/FingerPrint_Dataset/New_Exp/CASIA/model_Data/A/val/'

sourceFingPath = 'D:/FingerPrint_Dataset/New_Exp/CASIA/Test_Data/B/test/'
targetFingPath1 = 'D:/FingerPrint_Dataset/New_Exp/CASIA/model_Data/A/train/'
targetFingPath2 = 'D:/FingerPrint_Dataset/New_Exp/CASIA/model_Data/A/test/'
targetFingPath3 = 'D:/FingerPrint_Dataset/New_Exp/CASIA/model_Data/A/val/'


# print(trainFileNames.shape)
# print(trainFileNames)


for filePath in os.listdir(sourceMinPath):
    if filePath.endswith(".jpg"):
        fileName = str(filePath).rstrip(".jpg")
        fileName = fileName[8::]
        if fileName in trainFileNames:
            # shutil.copy(sourceFingPath+filePath, targetFingPath1+filePath)
            shutil.copy(sourceMinPath+filePath, targetMinPath1+filePath)
        else:
            # shutil.copy(sourceFingPath+filePath, targetFingPath2+filePath)
            # shutil.copy(sourceFingPath+filePath, targetFingPath3+filePath)
            shutil.copy(sourceMinPath+filePath, targetMinPath2+filePath)
            shutil.copy(sourceMinPath+filePath, targetMinPath3+filePath)