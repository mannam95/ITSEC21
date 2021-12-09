import minutiae_map
import numpy as np
import math
from PIL import Image
import os


def create_all_minutiae_maps(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".xyt"):
            create_image(folder_path, file_name)

def create_image(folder_path, file_name):
    path = folder_path + "/" + file_name
    create_image_from_map(parse(path), file_name)


def parse(path):
    m_map = minutiae_map.MinutiaeMap()
    with open(path) as f:
        lines = f.readlines()
        m_map.minutiae_list = [read_minutiae(list(map(int, x.split()))) for x in lines]
    return m_map


def read_minutiae(arr):
    return minutiae_map.MinutiaeInformation(arr[0], arr[1], arr[2])


def create_image_from_map(minutiaes, file_name):
    array = np.zeros([326, 357], dtype=np.uint8)
    for minutiae in minutiaes.minutiae_list:
        lower_y = minutiae.y_position-5
        upper_y = minutiae.y_position+6
        lower_x = minutiae.x_position-5
        upper_x = minutiae.x_position+6
        array[lower_y: upper_y, lower_x: upper_x] = math.floor(minutiae.theta/2)
    img = Image.fromarray(array)
    path = "data/minutiaeMaps/" + file_name[:-3] + "png"
    img.save(path)
