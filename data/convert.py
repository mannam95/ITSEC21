#Note:- The following code runned in colab, for some reason it doesn't work in local system
import os
from PIL import Image
import glob as glob

#Clone the google drive to the folder where the tif files are present
for name in glob.glob('*.tif'):
    jpegName = str(name).rstrip(".tif")
    jpegPath = '/content/drive/My Drive/Colab Notebooks/OVGU/ITSEC_21/imageConversion/FingerPrints/' + jpegName + '.jpeg'
    Image.open(name).convert('RGB').save(jpegPath, dpi=(500, 500), quality=500)