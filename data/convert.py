#Note:- The following code ran in colab, for some reason it doesn't work in local system
import os
from PIL import Image
import glob as glob

#Clone the google drive to the folder where the tif files are present
for name in glob.glob('*.tif'):
    jpegName = str(name).rstrip(".tif")
    jpegPath = '/content/drive/My Drive/Colab Notebooks/OVGU/ITSEC_21/imageConversion/FingerPrints_1Channel/' + jpegName + '.jpeg'
    im = Image.open(name)
    greyScaleImage = im.convert("L")
    # im.convert('RGB').save(jpegPath, dpi=(500, 500))
    greyScaleImage.save(jpegPath, dpi=(500, 500), quality=500)
    # im.convert("P", palette=Image.ADAPTIVE, colors=8).save(jpegPath, dpi=(500, 500))
