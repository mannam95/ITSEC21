#Create an Image Object from an Image
import cv2
from PIL import Image
import os

dirPath = "D:/FingerPrint_Dataset/Logs/CrossMatch/cross_all_v18/test_latest/images/"


files = os.listdir(dirPath)

separateFiles = []
for index, image in enumerate(files):
    if image.endswith("fake_B.png"):
        len1 = len(image)
        len2 = len(image[-10:])
        len3 = len1 - len2
        separateFiles.append(image[:len3])


for index, image in enumerate(separateFiles):

    img1Path = dirPath + image + "fake_B.png"

    imgFileName = image + "fake_B.png"

    srcInp = img1Path

    img = Image.open(img1Path)
    img = img.resize((504,504), Image.ANTIALIAS)
    img.save(
        'D:/FingerPrint_Dataset/upScaleImages/temp/' + imgFileName, dpi=(500, 500), quality=500
    )
