import os
import sys
import base64
import json
import requests

# dirPath = "D:/FingerPrint_Dataset/Logs/New_Exp/Cross_Match/test_latest/images/"
# fakePath = "D:/FingerPrint_Dataset/Logs/New_Exp/Cross_Match/test_latest/images/"


dirPath = "D:/FingerPrint_Dataset/Logs/New_Exp/casia_new2/test_latest/images/"
fakePath = "D:/FingerPrint_Dataset/Logs/New_Exp/casia_new2/test_latest/images/"


files = os.listdir(fakePath)

separateFiles = []
for index, image in enumerate(files):
    if image.endswith("fake_B.png"):
        # CrossMatch
        imgName = image[8:]
        imgName = imgName[:-11]
        separateFiles.append(imgName)

        # URU
        # imgName = image[:-11]
        # separateFiles.append(imgName)

count = 0
score36 = 0
score48 = 0
score60 = 0
for index, image in enumerate(separateFiles):
    print(image)

    # CrossMatch
    imgName1 = "resized_" + image + "_real_B.png"
    imgName2 = "resized_" + image + "_fake_B.png"

    # URU
    # imgName1 = image + "_real_B.png"
    # imgName2 = image + "_real_B.png"

    img1Path = dirPath + imgName1
    img2Path = fakePath + imgName2

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

    print("Finger Print Name: ", image)
    print("Result: ",result)

    if 'decision' in result:
        # if result.get('decision').strip() == 'succeeded':
        #     count = count + 1
        
        if result.get('score') >= 36:
            score36 = score36 + 1

        if result.get('score') >= 48:
            score48 = score48 + 1

        if result.get('score') >= 60:
            score60 = score60 + 1
print(score36, " images passed")
print(score48, " images passed")
print(score60, " images passed")