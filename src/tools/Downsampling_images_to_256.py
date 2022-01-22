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

                im_pil2 = add_margin(im_pil, 0, 16, 0, 15, 255)

                open_cv_img = cv2.cvtColor(np.array(im_pil2), cv2.COLOR_RGB2BGR)
                imageresize = cv2.resize(open_cv_img, (256, 256), interpolation = cv2.INTER_AREA)
                grayimage = cv2.cvtColor(imageresize, cv2.COLOR_BGR2GRAY)
                im_pil = Image.fromarray(grayimage)
                fileName = str(file).rstrip(".jpeg")
                im_pil.save(
                    write_path + "/resized_" + fileName + ".jpg", dpi=(500, 500), quality=500
                )



def main():

    read_minutiae_map_folder_path = "../../data/U_Are_U/Minutiae/minutiaeMaps20"
    write_minutiae_map_folder_path = "../../data/U_Are_U/Minutiae/resize/minutiaeMaps_20"


    read_fingerprint_folder_path = '../../data/U_Are_U/FingerPrints/original_jpeg'
    write_fingerprint_folder_path = '../../data/U_Are_U/FingerPrints/resize/FingerPrints_All'

    resize_images = Resize_Images()

    # Minutiae
    resize_images.read_all_files(read_minutiae_map_folder_path, write_minutiae_map_folder_path)

    # Finger Prints
    # resize_images.read_all_files(read_fingerprint_folder_path, write_fingerprint_folder_path)


if __name__ == "__main__":
    main()
