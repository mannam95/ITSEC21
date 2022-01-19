import os
import sys
import base64
import json
import requests

dirPath = "D:/FingerPrint_Dataset/Logs/CrossMatch/cross_all_v10/test_latest/images/"


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

    fingPath = dirPath

    img1Path = fingPath + image + "fake_B.png"
    img2Path = fingPath + image + "real_B.png"

    with open(img1Path, "rb") as f:
        im_bytes1 = f.read()  
    
    img1_base64 = base64.b64encode(im_bytes1).decode("utf8")

    with open(img2Path, "rb") as f:
        im_bytes2 = f.read()  
    
    img2_base64 = base64.b64encode(im_bytes2).decode("utf8")


    url = "http://141.44.30.186:5001/api/verifinger"
    headers = {'Content-type': 'application/json'}
    data = {'im1': img1_base64, 'im2': img2_base64}

    r = requests.post(url, data=json.dumps(data), headers=headers)

    result = r.json()

    print(image)
    print(result)

    if 'decision' in result:
        if result.get('decision').strip() == 'succeeded':
            count = count + 1

print(count, " images passed")