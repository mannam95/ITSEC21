#Note:- The following code ran in colab, for some reason it doesn't work in local system
import os
from PIL import Image
import glob as glob
import cv2
import random
import numpy as np


readDirPath = "D:/FingerPrint_Dataset/CASIA/"

folderPaths = ["CASIA-FingerprintV5 (000-099)", "CASIA-FingerprintV5 (100-199)", "CASIA-FingerprintV5 (200-299)", "CASIA-FingerprintV5 (300-399)", "CASIA-FingerprintV5 (400-499)"]
startList = ["000", "100", "200", "300", "400"]
endList = ["099", "199", "299", '399', '499']

saveDirPath = "D:/FingerPrint_Dataset/CASIA_Converted/"

trainFileNames = []

# Loop through folders
for i in range(len(folderPaths)):
    dirPath = readDirPath + folderPaths[i] + "/"

    #Loop through sub-folders
    for dirs in os.listdir(dirPath):
        subDirPath = dirPath + dirs + "/"

        #Loop through sub-sub-folders
        for subDirs in os.listdir(subDirPath):
            filesPath = subDirPath + subDirs + "/"

            filesList = []
            #Loop through files
            for filePath in os.listdir(filesPath):
                if filePath.endswith(".bmp"):
                    fileName = str(filePath).rstrip(".bmp")
                    filesList.append(fileName)
            
            randomFiles = random.sample(filesList, 2)
            trainFileNames = trainFileNames + randomFiles

npList = np.asarray(trainFileNames)
np.save("casiaFilenames.npy", npList)
