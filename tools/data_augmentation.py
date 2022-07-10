import os
import sys
import PIL
from PIL import Image
import shutil


def read_files(dir_path):
    """This function reads the image file names. 

    :param dir_path: the images folder that should be augmented.
    :return: Returns image file names.
    """
    files = os.listdir(dir_path)
    unique_files = []
    for index, image_name in enumerate(files):
        unique_files.append(image_name)
    
    return unique_files


# Rotates the image 90 degress to right
def rotate_image(image_path, save_path, angle):
    """This function rotates the image of given angle. 

    :param image_path: the image path.
    :param save_path: the image path.
    :param angle: the image path.
    :return: Returns None.
    """

    try:
        img = Image.open(image_path)
        img = img.rotate(angle, fillcolor = 255) # fill with white color in rotated spaces.
        img.save(
            save_path,
            dpi=(500, 500),
            quality=500,
        )
    except:
        print("Couldn't rotate the image: ", image_path, " with angle: ", angle)


def flip_image(image_path, save_path):
    """This function rotates the image of given angle. 

    :param image_path: the image path.
    :param save_path: the image path.
    :param angle: the image path.
    :return: Returns None.
    """

    try:
        img = Image.open(image_path)
        img = img.transpose(PIL.Image.FLIP_LEFT_RIGHT) # Flip Image w.r.t. Vertical Axis.
        img.save(
            save_path,
            dpi=(500, 500),
            quality=500,
        )
    except:
        print("Couldn't flipe the image: ", image_path)


def perform_flip_augmentation(output_dir, unique_files):
    """This function augments each flipped image. 

    :param output_dir: the augmented images saved path.
    :param unique_files: the image path.
    :return: Returns None.
    """
    # Process rotating the images.
    rotation_options = [10,20,-10,-20]
    for angle in rotation_options:
        print("flipped image augmenting angle: ", angle)
        if angle == -10 or angle == -20:
            postfix_name = "_minus_"
        else:
            postfix_name = "_plus_"
        for index, image_name in enumerate(unique_files):
            file_name = image_name.rsplit('.', 1)[0]
            image_path = output_dir + "/" + file_name + "_flip.png"
            save_path = output_dir + "/" + file_name + "_flip_" + postfix_name + str(abs(angle)) + ".png"
            rotate_image(image_path, save_path, angle)
        print("Completed flipped image augmenting angle: ", angle)


def perform_augmentation(input_dir, output_dir, unique_files):
    """This function augments each image. 

    :param input_dir: the original images directory.
    :param output_dir: the augmented images save path.
    :param unique_files: the image path.
    :return: Returns None.
    """

    # Process rotating the images.
    rotation_options = [10,20,-10,-20]
    for angle in rotation_options:
        print("Augmenting angle: ", angle)
        if angle == -10 or angle == -20:
            postfix_name = "_minus_"
        else:
            postfix_name = "_plus_"
        for index, image_name in enumerate(unique_files):
            image_path = input_dir + "/" + image_name
            save_path = output_dir + "/" + image_name.rsplit('.', 1)[0] + postfix_name + str(abs(angle)) + ".png"
            rotate_image(image_path, save_path, angle)
        print("Completed augmenting angle: ", angle)
    
    # Process flipping the images.
    print("Augmenting flipiing")
    for index, image_name in enumerate(unique_files):
        image_path = input_dir + "/" + image_name
        save_path = output_dir + "/" + image_name.rsplit('.', 1)[0] + "_flip.png"
        flip_image(image_path, save_path)
    perform_flip_augmentation(output_dir, unique_files) # perform augmentation for flipped images
    print("Completed augmenting flipping")

    # Process orifinal images.
    print("Copying the original files")
    for index, image_name in enumerate(unique_files):
        image_path = input_dir + "/" + image_name
        save_path = output_dir + "/" + image_name
        shutil.copy(image_path, save_path)
    print("Completed copying original images flipping")


def main():

    if ( len(sys.argv) < 3 ):
        print('Usage: python '+sys.argv[0]+ ' <input_dir> <output_dir>')
        print('\tinp_dir: this folder is the original images folder.')
        print('\tout_dir: this folder is the one where augmented images will be saved.')
        sys.exit(0)

    # parse command line parameters
    input_dir =  sys.argv[1]

    output_dir = sys.argv[2]
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # get the file names
    unique_files = read_files(input_dir)

    # call the augmentation method for rotating and flipping.
    perform_augmentation(input_dir, output_dir, unique_files)


if __name__ == '__main__':
    main()