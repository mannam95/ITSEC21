import os
import sys
import base64
import json
import requests
import pandas as pd
import xlsxwriter


# dirName = ["cross_all_v18", "cross_all_v19", "cross_da_v20"]
dirName = ["U_R_U_All_Data_V1"]
# dirName = ["U_R_U_All_V10", "U_R_U_All_V14", "U_R_U_DA_V19"]



# dirPath = "D:/FingerPrint_Dataset/Logs/U_R_U/U_R_U_All_Data_V1/test_latest/images/"

for dirCount, pathName in enumerate(dirName):

    # dirPath = "D:/FingerPrint_Dataset/Logs/CrossMatch/" + pathName + "/test_latest/images/"
    dirPath = "D:/FingerPrint_Dataset/Logs/U_R_U/" + pathName + "/test_latest/images/"
    files = os.listdir(dirPath)

    scores = []
    indexCount = 0
    separateFiles = []
    for index, image in enumerate(files):
        if image.endswith("fake_B.png"):
            len1 = len(image)
            len2 = len(image[-10:])
            len3 = len1 - len2
            separateFiles.append(image[:len3])

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

        if 'decision' in result:
            scores.append([])
            scores[indexCount].append(indexCount + 1)
            scores[indexCount].append(result.get('score'))
            scores[indexCount].append(image + "fake_B.png")
            scores[indexCount].append(image + "real_B.png")
            indexCount = indexCount + 1
    
    # Save the results in a excel file
    df = pd.DataFrame(scores)
    fileName = "D:/FingerPrint_Dataset/Results/" + pathName + ".xlsx"
    with xlsxwriter.Workbook(fileName) as workbook:
        worksheet = workbook.add_worksheet()

        for row_num, data in enumerate(scores):
            worksheet.write_row(row_num, 0, data)

    print(pathName, " : Completed")