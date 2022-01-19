import os
import sys
import base64
import json
import requests
import matplotlib.pyplot as plt
import numpy as np

dirPath = "D:/FingerPrint_Dataset/Logs/CrossMatch/cross_all_v10/test_latest/images/"

dirPath = "C:/Users/Lukas/Documents/Uni/ITSEC/cross_all_v10/test_latest/images/"

files = os.listdir(dirPath)

separateFiles = []
for index, image in enumerate(files):
    if image.endswith("fake_B.png"):
        len1 = len(image)
        len2 = len(image[-10:])
        len3 = len1 - len2
        separateFiles.append(image[:len3])

count = 0
count_fail = 0
scores = []
veryfinger_error_count = 0

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
        else:
            count_fail += 1
        scores.append(r.json()["score"])
    else:
        veryfinger_error_count += 1
    print(scores[len(scores)-1])

print(count, " images passed")
plt.bar(['succeeded', 'failed', 'verifinger error'], [count, count_fail, veryfinger_error_count])
plt.savefig('')
plt.grid()
plt.show()

boundaries = [0,36,48,60]
occurences = np.zeros(len(boundaries)-1)
for i in range(1, len(boundaries)):
    for s in scores:
        if boundaries[i] <= s < boundaries[i]:
            occurences[i-1] += 1
plt.bar(list(map(str, boundaries[1:len(boundaries)])), [100*x/(len(scores)+veryfinger_error_count)for x in occurences])
plt.title("perentage of scores in ranges")
plt.grid()
plt.show()
print()

boundaries = [0,36,48,60]
occurences = np.zeros(len(boundaries)-1)
for i in range(1, len(boundaries)):
    for s in scores:
        if s >= boundaries[i]:
            occurences[i-1] += 1
plt.bar(list(map(str,boundaries[1:len(boundaries)])), [100*x/(len(scores)+veryfinger_error_count)for x in occurences])
plt.title("percentage of passings according to thresholds")
plt.grid()
plt.show()
print()


