from PIL import Image
import os
import sys
import PIL

# padding
# CM(neuro): top=16, right=4, bottom=16, left=4
# U_R_U(neuro): top=78, right=93, bottom=77, left=93
neu_CM = [16, 4, 16, 4]
neu_URU = [78, 93, 77, 93]

fvc_CM = [16, 0, 16, 0]
fvc_CM_crop = [0, 64, 0, 64]
fvc_URU = [74, 92, 74, 92]


def add_padding(pil_img, top, right, bottom, left, color=255):
    """This function adds the padding to the given image. 

    :param pil_img: image data.
    :param top: top padding.
    :param right: right padding
    :param bottom: bottom padding.
    :param left: left padding.
    :param color: which color to pad.
    :return: Returns the padded image.
    """
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result

def crop_img(pil_img, top, right, bottom, left):
    """This function crops the given image. 

    :param pil_img: image data.
    :param top: top crop.
    :param right: right crop
    :param bottom: bottom crop.
    :param left: left crop.
    :return: Returns the cropped image.
    """
    width, height = pil_img.size
    left = left
    right = width - right
    top = height - height
    bottom = height
    result = pil_img.crop((left, top, right, bottom))
    return result

def main():

    if ( len(sys.argv) < 4 ):
        print('Usage: python '+sys.argv[0]+ ' <input_dir> <output_dir>')
        print('\tinput_dir: this folder should include image files only')
        print('\toutput_dir: padded or rescaled images will be stored in this folder')
        print('\tinput database type: NeuroTech_CrossMatch=0, NeuroTech_CrossMatch=1, FVC_CrossMatch=2, FVC_URU=3')
        sys.exit(0)

    # parse command line parameters
    input_dir =  sys.argv[1]
    fp_image_files = os.listdir(input_dir)

    output_dir = sys.argv[2]
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    database_id = int(sys.argv[3])

    current_pad = None
    if database_id == 0:
        current_pad = neu_CM
    elif database_id == 1:
        current_pad = neu_URU
    elif database_id == 2:
        current_pad = fvc_CM
    elif database_id == 3:
        current_pad = fvc_URU

    # process images in the input folder
    for idx, fp_image_file in enumerate(fp_image_files):

        try:
            im_orig = Image.open(input_dir + '/' + fp_image_file).convert('L')

            # Padding
            im_orig_scaled = add_padding(im_orig, top=current_pad[0], right=current_pad[1], bottom=current_pad[2], left=current_pad[3], color=255)

            # Apply Cropping only for FVC CrossMatch
            if database_id == 2:
                im_orig_scaled = crop_img(im_orig_scaled, top=fvc_CM_crop[0], right=fvc_CM_crop[1], bottom=fvc_CM_crop[2], left=fvc_CM_crop[3])

            # Save the image
            im_orig_scaled.save(
                output_dir+'/' + fp_image_file[::-1].split('.', 1)[1][::-1] + '.png',
                dpi=(500, 500), quality=500
                )

        except FileNotFoundError:
            print("File not Found: ", fp_image_file)
            continue
        except PIL.UnidentifiedImageError:
            print("File not identified as image: ", fp_image_file)
            continue
        except:
            print("Unknown error for file: ", fp_image_file)
            continue



if __name__ == '__main__':
    main()