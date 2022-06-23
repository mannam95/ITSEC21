import os
from PIL import Image, ImageFilter
from pathlib import Path


directorySubFolders = ["test/", "train/", "val/"]
data_Aug_Types = [
    "original",
    "rotate_right_90",
    "rotate_left_90",
    "rotate_180",
    # "noise",
]

data_Aug_Types_Cmp = [
    "original",
    "rotate_right_90",
    "rotate_left_90",
    "rotate_180",
    # "noise",
]

# Minutiae Paths
directoryPath_Min = "D:/Git_WorkSpace/ITSEC21/data/CrossMatch_Sample_DB/model_Data/Split2/A/"
savePath_Min = "D:/Git_WorkSpace/ITSEC21/data/CrossMatch_Sample_DB/dataAugmentation/CDASplit1/A/"

# FingerPrints Path
directoryPath_Fin = "D:/Git_WorkSpace/ITSEC21/data/CrossMatch_Sample_DB/model_Data/Split2/B/"
savePath_Fin = "D:/Git_WorkSpace/ITSEC21/data/CrossMatch_Sample_DB/dataAugmentation/CDASplit1/B/"

# Copies the same image to different path
def copyFunction(imagePath, destPath):
    img = Image.open(imagePath)
    img.save(
        destPath,
        dpi=(500, 500),
        quality=500,
    )


# Rotates the image 90 degress to right
def rotate_right_90(imagePath, destPath):
    img = Image.open(imagePath)
    img = img.transpose(Image.ROTATE_270)
    img.save(
        destPath,
        dpi=(500, 500),
        quality=500,
    )


# Rotates the image 90 degress to left
def rotate_left_90(imagePath, destPath):
    img = Image.open(imagePath)
    img = img.transpose(Image.ROTATE_90)
    img.save(
        destPath,
        dpi=(500, 500),
        quality=500,
    )


# Rotates the image 180
def rotate_180(imagePath, destPath):
    img = Image.open(imagePath)
    img = img.transpose(Image.ROTATE_180)
    img.save(
        destPath,
        dpi=(500, 500),
        quality=500,
    )


# Adds noise to the image
def addNoise(imagePath):
    im = Image.open(imagePath)
    im2 = im.filter(ImageFilter.GaussianBlur(2))
    im2.show()


def perform_Sugmentation():
    for augmentType in data_Aug_Types:
        print("Augmenting ", augmentType)
        for folder in directorySubFolders:
            files = os.listdir(directoryPath_Min + folder)
            Path(savePath_Min + folder).mkdir(parents=True, exist_ok=True)
            Path(savePath_Fin + folder).mkdir(parents=True, exist_ok=True)
            for index, image in enumerate(files):
                imagePath_Min = directoryPath_Min + folder + image
                imagePath_Fin = directoryPath_Fin + folder + image
                if folder != directorySubFolders[1]:
                    destPath_Min = savePath_Min + folder + image
                    destPath_Fin = savePath_Fin + folder + image
                else:
                    destPath_Min = (
                        savePath_Min + folder + augmentType + "_" + str(index) + ".jpg"
                    )
                    destPath_Fin = (
                        savePath_Fin + folder + augmentType + "_" + str(index) + ".jpg"
                    )
                if augmentType == data_Aug_Types_Cmp[0]:
                    copyFunction(imagePath=imagePath_Min, destPath=destPath_Min)
                    copyFunction(imagePath=imagePath_Fin, destPath=destPath_Fin)
                elif (
                    augmentType == data_Aug_Types_Cmp[1]
                    and folder == directorySubFolders[1]
                ):
                    rotate_right_90(imagePath=imagePath_Min, destPath=destPath_Min)
                    rotate_right_90(imagePath=imagePath_Fin, destPath=destPath_Fin)
                elif (
                    augmentType == data_Aug_Types_Cmp[2]
                    and folder == directorySubFolders[1]
                ):
                    rotate_left_90(imagePath=imagePath_Min, destPath=destPath_Min)
                    rotate_left_90(imagePath=imagePath_Fin, destPath=destPath_Fin)
                elif (
                    augmentType == data_Aug_Types_Cmp[3]
                    and folder == directorySubFolders[1]
                ):
                    rotate_180(imagePath=imagePath_Min, destPath=destPath_Min)
                    rotate_180(imagePath=imagePath_Fin, destPath=destPath_Fin)


perform_Sugmentation()
