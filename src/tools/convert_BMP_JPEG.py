#Note:- The following code ran in colab, for some reason it doesn't work in local system
import os
from PIL import Image
import glob as glob
import cv2


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
        print(dirs)
        subDirPath = dirPath + dirs + "/"

        #Loop through sub-sub-folders
        for subDirs in os.listdir(subDirPath):
            print(subDirs)
            filesPath = subDirPath + subDirs + "/"

            filesList = []
            #Loop through files
            for filePath in os.listdir(filesPath):
                if filePath.endswith(".bmp"):
                    filesList.append(filePath)
                    print(filePath)
                    fileName = str(filePath).rstrip(".bmp")
                    saveFilePath = saveDirPath + fileName+ '.jpeg'

                    read = cv2.imread(str(filesPath + filePath))
                    grayimage = cv2.cvtColor(read, cv2.COLOR_BGR2GRAY)
                    im_pil = Image.fromarray(grayimage)
                    im_pil.save(saveFilePath, dpi=(500, 500), quality=500)
