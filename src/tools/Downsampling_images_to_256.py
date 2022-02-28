import numpy as np
from PIL import Image

import os
import cv2

def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result

class Resize_Images:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def read_all_files(self, read_path, write_path):
        for file in os.listdir(read_path):
            # This will downsample the minutiae maps
            if file.endswith(".jpg"):
                image = cv2.imread(str(read_path + "/" + file))
                imageresize = cv2.resize(image, (256, 256), interpolation = cv2.INTER_AREA)
                grayimage = cv2.cvtColor(imageresize, cv2.COLOR_BGR2GRAY)
                im_pil = Image.fromarray(grayimage)
                im_pil.save(
                    write_path + "/resized_" + file, dpi=(500, 500), quality=500
                )


            # This will downsample the FingerPrint Images
            if file.endswith(".jpeg"):
                image = cv2.imread(str(read_path + "/" + file))
                im_pil = Image.open(str(read_path + "/" + file))

                # U_r_U
                # im_pil2 = add_margin(im_pil, 0, 16, 0, 15, 255)

                # CASIA
                im_pil2 = add_margin(im_pil, 0, 14, 0, 14, 255)

                #Cross
                # im_pil2 = add_margin(im_pil, 12, 0, 12, 0, 255)

                im_pil = Image.fromarray(np.array(im_pil2))
                
                fileName = str(file).rstrip(".jpeg")
                # im_pil.save(
                #     write_path + "/resized_" + fileName + ".png", dpi=(500, 500), quality=500
                # )

                open_cv_img = cv2.cvtColor(np.array(im_pil2), cv2.COLOR_RGB2BGR)
                imageresize = cv2.resize(open_cv_img, (256, 256), interpolation = cv2.INTER_AREA)
                grayimage = cv2.cvtColor(imageresize, cv2.COLOR_BGR2GRAY)
                im_pil = Image.fromarray(grayimage)
                fileName = str(file).rstrip(".jpeg")
                im_pil.save(
                    write_path + "/resized_" + fileName + ".jpg", dpi=(500, 500), quality=500
                )



def main():

    read_minutiae_map_folder_path = "D:/FingerPrint_Dataset/New_Exp/CASIA/Minutiae/minutiaeMaps"
    write_minutiae_map_folder_path = "D:/FingerPrint_Dataset/New_Exp/CASIA/Test_Data/CASIA_Min/test"


    read_fingerprint_folder_path = 'D:/FingerPrint_Dataset/New_Exp/CASIA/FingerPrints/CASIA_JPEG'
    write_fingerprint_folder_path = 'D:/FingerPrint_Dataset/New_Exp/CASIA/Test_Data/CASIA_Fing/test'

    resize_images = Resize_Images()

    # Minutiae
    resize_images.read_all_files(read_minutiae_map_folder_path, write_minutiae_map_folder_path)

    # Finger Prints
    # resize_images.read_all_files(read_fingerprint_folder_path, write_fingerprint_folder_path)


if __name__ == "__main__":
    main()
