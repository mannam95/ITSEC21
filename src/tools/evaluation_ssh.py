import os
import sys
import base64
import json
from subprocess32 import check_output
# import requests


dirPath = "/vol1/itsec_1/pytorch-CycleGAN-and-pix2pix/results/new_CM_5_S1_Fold1/test_latest/images/"
files = os.listdir(dirPath)

# dirPath = "/vol1/itsec_1/new_exp/results/upscaled/CrossMatch_5_SplitsV2/folder_1_diff/"
# files = os.listdir(dirPath + "fake")

separateFiles = []
for index, image in enumerate(files):
    if image.endswith("fake_B.png"):
        len1 = len(image)
        len2 = len(image[-10:])
        len3 = len1 - len2
        separateFiles.append(image[:len3])
    # separateFiles.append(image)

count = 0
score36 = 0
score48 = 0
score60 = 0
for index, image in enumerate(separateFiles):
    print ('file num: ', index, ' and file name', image)
    fingPath = dirPath

    img1Path = fingPath + image + "real_B.png"
    img2Path = fingPath + image + "fake_B.png"

    # img1Path = fingPath + "real/" + image
    # img2Path = fingPath + "fake/" + image

    try:
        r = check_output( ['Verifinger1toN', img1Path, img2Path], timeout=60 )

        print(r)
        lines = r.split(b';')
        # foo,threshold,score,decision = r.rsplit(';', 3)
        score = int(lines[2].decode("utf-8"))


        print("Score: ", score)

        # if decision.strip() != 'failed':
        #     count = count + 1
        #     break
        if score >= 36:
            score36 = score36 + 1

        if score >= 48:
            score48 = score48 + 1

        if score >= 60:
            score60 = score60 + 1
        
    except:
        print("Couldn't execute the fingerprint")
        continue

print("Evaluation total images: ", len(separateFiles))
print("Evaluation images that didn't met the any criteria: ", len(separateFiles) - score36)
print("Score 36: ", score36, " images passed")
print("Score 48: ", score48, " images passed")
print("Score 60: ", score60, " images passed")