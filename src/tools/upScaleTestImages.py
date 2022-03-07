#Create an Image Object from an Image
from PIL import Image
import os

dirPath = "D:/FingerPrint_Dataset/Logs/New_Exp/U_R_U/test_latest/images/"


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

    imgFileName1 = image + "fake_B.png"

    img2Path = dirPath + image + "real_B.png"

    imgFileName2 = image + "real_B.png"

    srcInp = img1Path

    img = Image.open(img1Path)
    img = img.resize((504,504), Image.ANTIALIAS)
    img.save(
        'D:/FingerPrint_Dataset/Logs/New_Exp/U_R_U/upscale/' + imgFileName1, dpi=(500, 500), quality=500
    )

    img = Image.open(img2Path)
    img = img.resize((504,504), Image.ANTIALIAS)
    img.save(
        'D:/FingerPrint_Dataset/Logs/New_Exp/U_R_U/upscale/' + imgFileName2, dpi=(500, 500), quality=500
    )
