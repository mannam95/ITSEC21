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

    print(min(2 ** 1, 8))

    break

    img1Path = dirPath + image + "fake_B.png"

    imgFileName = image + "fake_B.png"

    srcInp = img1Path

    # src = cv2.imread(srcInp, cv2.IMREAD_UNCHANGED)

    # dsize = (504, 504)

    # output = cv2.resize(src, dsize,  interpolation = cv2.INTER_AREA)


    # # newImg = output[0:357, 14:340]

    # grayimage = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    # im_pil = Image.fromarray(grayimage)
    # im_pil.save(
    #     'D:/FingerPrint_Dataset/upScaleImages/cross_all_v18/' + imgFileName, dpi=(500, 500), quality=500
    # )


    

    basewidth = 300
    img = Image.open(img1Path)
    img = img.resize((504,504), Image.ANTIALIAS)
    img.save(
        'D:/FingerPrint_Dataset/upScaleImages/temp/' + imgFileName, dpi=(500, 500), quality=500
    )
