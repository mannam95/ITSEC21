
import numpy as np
import tensorflow as tf
from PIL import Image
# from matplotlib import pyplot as plt

import os

class Resize_Images():

  def __init__(self, **kwargs):
     super().__init__(**kwargs)

  def read_all_files(self, read_path, write_path, resize_with_pad = True):
    for file in os.listdir(read_path):
      image = tf.io.read_file(str(read_path + '/' + file))
      if file.endswith(".png"):
        image = tf.io.decode_png(image)
      if file.endswith(".jpeg"):
        image = tf.io.decode_jpeg(image)
      
      final_resized_image = self.resize_images_to_256(image, resize_with_pad)
      #plt.imshow(final_resized_image)
      final_resized_image.save(write_path + '/resized_' + file, dpi=(500, 500), quality=500)
      break
      
  
  def resize_images_to_256(self, image, resize_with_pad):
    if (resize_with_pad):
      resized_image = tf.image.resize_with_pad(image, 256, 256,
                                method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
    else: 
      resized_image = tf.image.resize(image, [256, 256],
                                method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
    
    resized_image = resized_image[:,:,0]

    #convert to PIL image
    pil_image = Image.fromarray(np.array(resized_image))

    return pil_image

def main():
  read_minutiae_map_folder_path = '/content/drive/MyDrive/ITSEC/minutiaeMaps'
  write_minutiae_map_folder_path = '/content/drive/MyDrive/ITSEC/Minutiae_Map_Images_256'

  read_fingerprint_folder_path = '../../data/initial_Pre_Process_data/FingerPrints/FingerPrints_1Channel'
  write_fingerprint_folder_path = '../../data/initial_Pre_Process_data/FingerPrints/Fingerprint_Images_256'

  resize_images = Resize_Images()
  # resize_images.read_all_files(read_folder_path, write_folder_path, False)
  resize_images.read_all_files(read_fingerprint_folder_path, write_fingerprint_folder_path, True)

if __name__ == '__main__':
  main()