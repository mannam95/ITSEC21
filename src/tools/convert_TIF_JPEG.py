#Note:- The following code ran in colab, for some reason it doesn't work in local system
import os
from PIL import Image
import glob as glob
import cv2


dirPath = "D:/Git_WorkSpace/ITSEC21/data/CrossMatch_Sample_DB/"

#Clone the google drive to the folder where the tif files are present
count = 0
for file in os.listdir(dirPath + 'original_tif/'):
# for name in glob.glob('*.tif'):
    print(file)
    jpegName = str(file).rstrip(".tif")
    count = count + 1
    jpegPath = dirPath + 'original_jpeg/' + str(count) + '.jpeg'
    # im = Image.open(str(dirPath + "original_tif/" + file))
    # greyScaleImage = im.convert("L")
    # # im.convert('RGB').save(jpegPath, dpi=(500, 500))
    # greyScaleImage.save(jpegPath, dpi=(500, 500), quality=500)
    # im.convert("P", palette=Image.ADAPTIVE, colors=8).save(jpegPath, dpi=(500, 500))


    read = cv2.imread(str(dirPath + "original_tif/" + file))
    grayimage = cv2.cvtColor(read, cv2.COLOR_BGR2GRAY)
    im_pil = Image.fromarray(grayimage)
    im_pil.save(jpegPath, dpi=(500, 500), quality=500)
