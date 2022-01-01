import minutiae_map
import numpy as np
import math
from PIL import Image
import os
import matplotlib.pyplot as plt
import statistics


def plot_statistics(folder_path, thresholds):
    minutiae_maps = []
    for threshold in thresholds:
        maps_threshold = []
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".xyt"):
                maps_threshold.append(parse(folder_path + "/" + file_name, threshold))
        minutiae_maps.append(maps_threshold)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    avgs = [statistics.mean([len(m_map.minutiae_list) for m_map in maps_threshold]) for maps_threshold in minutiae_maps]
    ax.bar([str(x) for x in thresholds], avgs)
    plt.show()



# create images of minutiae maps for all .xyt files
def create_all_minutiae_maps(folder_path, threshold=0):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".xyt"):
            create_image(folder_path, file_name, threshold)


def create_all_minutiae_maps_filtered(folder_path, threshold):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".xyt"):
            create_image(folder_path, file_name, threshold)


def transform_image(image):
    pad_left = int(math.ceil(357 - 326)/2)
    pad_right = int(math.floor(357-326)/2)
    padded_image = scale(np.pad(image, [(0, 0), (pad_left, pad_right)], mode='constant'), 357, 357)
    return padded_image

# give total values for aimed height and width
def scale(im, height, width):
  initial_height = len(im)     # source number of rows
  initial_width = len(im[0])  # source number of columns
  return [[im[int(initial_height * r / height)][int(initial_width * c / width)]
           for c in range(width)] for r in range(height)]


def create_image(folder_path, file_name, threshold):
    path = folder_path + "/" + file_name
    create_image_from_map(parse(path, threshold), file_name, threshold)


def parse(path, threshold):
    m_map = minutiae_map.MinutiaeMap()
    with open(path) as f:
        lines = f.readlines()
        m_map.minutiae_list = [read_minutiae(list(map(int, x.split()))) for x in lines if int(x.split()[3]) >= threshold]
    return m_map


def read_minutiae(arr):
    return minutiae_map.MinutiaeInformation(arr[0], arr[1], arr[2], arr[3])


def create_image_from_map(minutiaes, file_name, threshold):
    array = np.zeros([326, 357], dtype=np.uint8)
    for minutiae in minutiaes.minutiae_list:
        lower_y = minutiae.y_position-5
        upper_y = minutiae.y_position+6
        lower_x = minutiae.x_position-5
        upper_x = minutiae.x_position+6
        array[lower_y: upper_y, lower_x: upper_x] = math.floor(minutiae.theta/2)
    transformed_image = np.array(transform_image(array))
    img = Image.fromarray(transformed_image)
    path = "../../data/initial_Pre_Process_data/Minutiae/minutiaeMaps" + (("" + str(threshold)) if threshold>0 else "")
    if not os.path.isdir(path):
        os.mkdir(path)
    img.save(path + "/" + file_name[:-3] + "jpg", dpi=(500, 500), quality=500)
