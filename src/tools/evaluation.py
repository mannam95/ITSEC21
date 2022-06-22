import os
import sys
import base64
import json
import requests

dirPath = "/home/srinath/Documents/itsec_new/results/new_cross_match_point_minutiae_v1/test_latest/images/"


files = os.listdir(dirPath)

separateFiles = []
for index, image in enumerate(files):
    if image.endswith("fake_B.png"):
        len1 = len(image)
        len2 = len(image[-10:])
        len3 = len1 - len2
        separateFiles.append(image[:len3])

count = 0
for index, image in enumerate(separateFiles):
    print image

    fingPath = dirPath

    img1Path = fingPath + image + "fake_B.png"
    img2Path = fingPath + image + "real_B.png"
    img1_base64 = base64.b64encode(open(img1Path, "rb").read())
    img2_base64 = base64.b64encode(open(img2Path, "rb").read())	
    # img2_base64 = base64.b64encode(open(img1Path, "rb").read())	

    url = ""
    headers = {'Content-type': 'application/json'}
    data = {'im1': img1_base64, 'im2': img2_base64}

    r = requests.post(url, data=json.dumps(data), headers=headers)


    print r,r.json()

    if r.json().keys()[0] != 'message':
        if r.json()["decision"].strip() != 'failed':
            count = count + 1

    # print r.json()["decision"]

    # print len(r.json()["decision"])

    # print r.json().keys()[1]

    # if r.json()["decision"].strip() != 'failed':

    #     print r,r.json()

    #     print r.json()["decision"]

    #     print len(r.json()["decision"])

    #     print r.json().keys()[1]
    #     break

print(count, " images passed")