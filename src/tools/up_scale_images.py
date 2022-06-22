from PIL import Image
import os

# Local Path
# results_path = "/home/srinath/Documents/git/pytorch-CycleGAN-and-pix2pix/results/new_CM_5_S2_Fold2/test_latest/images/"
# original_path = "/home/srinath/Documents/itsec_new/neuro/CrossMatch/"

# upscale_real_path = "/home/srinath/Documents/itsec_new/results/upscaled/new_CM_5_S2_Fold2/real/"
# upscale_fake_path = "/home/srinath/Documents/itsec_new/results/upscaled/new_CM_5_S2_Fold2/fake/"

# Host Machine Paths
results_path = "/vol1/itsec_1/pytorch-CycleGAN-and-pix2pix/results/new_CM_5_S2_Fold1/test_latest/images"
original_path = "/vol1/itsec_1/new_exp/data/neuro/CrossMatch/"

upscale_real_path = "/vol1/itsec_1/new_exp/results/upscaled/CrossMatch_5_SplitsV2/folder_1/real/"
upscale_fake_path = "/vol1/itsec_1/new_exp/results/upscaled/CrossMatch_5_SplitsV2/folder_1/fake/"

# Create directories if not present
if (os.path.exists(upscale_real_path) == False):
    os.mkdir(upscale_real_path)
if (os.path.exists(upscale_fake_path) == False):
    os.mkdir(upscale_fake_path)


files = os.listdir(results_path)

# Read gan generated results file names
separateFiles = []
for index, image in enumerate(files):
    if image.endswith("fake_B.png"):
        len1 = len(image)
        len2 = len(image[-11:])
        len3 = len1 - len2
        separateFiles.append(image[:len3])


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

def upscale_fake(image):
    """This function upscales and saves the given fake image. 

    :return: Returns None.
    """
    fake_img_path = results_path + image + "_fake_B.png"


    img = Image.open(fake_img_path)
    img = img.resize((512,512), Image.ANTIALIAS)
    img.save(
        upscale_fake_path + image + ".png", dpi=(500, 500), quality=500
    )

def upscale_real(image):
    """This function upscales and saves the given real image. 

    :return: Returns None.
    """
    real_img_path = original_path + image + ".tif"

    im_orig = Image.open(real_img_path).convert('L')

    # padding
    # CM(neuro): top=16, right=4, bottom=16, left=4
    # U_R_U(neuro): top=78, right=93, bottom=77, left=93
    neu_CM = [16, 4, 16, 4]
    neu_URU = [78, 93, 77, 93]

    current_pad = neu_CM

    im_orig_scaled = add_padding(im_orig, top=current_pad[0], right=current_pad[1], bottom=current_pad[2], left=current_pad[3], color=255)

    im_orig_scaled.save(
        upscale_real_path + image + ".png", dpi=(500, 500), quality=500
    )




# loop over the entire gan generated results
for index, image in enumerate(separateFiles):

    upscale_fake(image)
    upscale_real(image)

