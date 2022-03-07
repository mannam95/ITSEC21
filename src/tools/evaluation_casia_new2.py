import os
import sys
import base64
import json
from subprocess32 import check_output
# import requests


# dirPath = "D:/FingerPrint_Dataset/Logs/U_R_U/U_R_U_All_V6/test_latest/images/"

dirPath = "/vol1/itsec_3/pytorch-CycleGAN-and-pix2pix/results/casia_new2/test_latest/images/"


files = os.listdir(dirPath)

separateFiles = []
for index, image in enumerate(files):
    if image.endswith("fake_B.png"):
        len1 = len(image)
        len2 = len(image[-10:])
        len3 = len1 - len2
        separateFiles.append(image[:len3])

count = 0
score36 = 0
score48 = 0
score60 = 0
for index, image in enumerate(separateFiles):
    print ('file num: ', index, ' and file name', image)

    fingPath = dirPath

    img1Path = fingPath + image + "fake_B.png"
    img2Path = fingPath + image + "real_B.png"

    try:
        r = check_output( ['VerifyFinger', img1Path, img2Path], timeout=60 )

        foo,threshold,score,decision = r.rsplit(';', 3)


        print(threshold, score, decision)

        # if decision.strip() != 'failed':
        #     count = count + 1
        #     break
        if int(score) >= 36:
            score36 = score36 + 1

        if int(score) >= 48:
            score48 = score48 + 1

        if int(score) >= 60:
            score60 = score60 + 1
    except:
        print("Couldn't execute the fingerprint")
        continue


print(score36, " images passed")
print(score48, " images passed")
print(score60, " images passed")