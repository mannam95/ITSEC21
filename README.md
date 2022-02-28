# ITSEC - Reconstruction of Fingerprints from Minutiae Templates

### Contributors (Assignment Team)

- **Venkata Srinath Mannam**
- **Meghana Rao**
- **Lukas Partes**

## Getting Started

These instructions will get you to set up on your local machine for development and testing purposes.

### Prerequisites

- Understanding of python, linux would be better.
- Create a conda env or python venv

### Installing

- Clone the repository or download and unzip it.
- Make sure that all the files are present in folder and in the following similar structure.
- Install the packages mentioned at req.txt
- Conda env creation: conda create -n <environment-name> --file req.txt

```
ITSEC21(Parent Folder)
    data
            CrossMatch_Sample_DB
            U_Are_U
    src
            minutiae_Map_Reconstruction
            tools
    .gitignore
    README.md
```

## Working in devlopment

The project includes multiple tasks:

- Getting Datasets
- Extrcating Minutiae
- Minutiae Map Construction
- Training Data Creation
- Data Augmentation
- Evaluation

### Getting Datasets

- We have used two public datasets in this project [Cross Match](https://www.neurotechnology.com/download/CrossMatch_Sample_DB.zip) and [U.are.U](https://www.neurotechnology.com/download/UareU_sample_DB.zip)

### Extracting Minutiae

- To extract minutiae we have used MINDTCT tool by [NIST](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7392.pdf).
- The mentioned datasets are in ".tif" format but MINDTCT tool expects the inputs to be in ".jpeg" format. To convert the datasets, we have used the python script [src/tools/convert_TIF_JPEG.py](src/tools/convert_TIF_JPEG.py)
- To iteratively extract minutiae we have used the script file [src/minutiae_Map_Reconstruction/extractMinutiae.sh](src/minutiae_Map_Reconstruction/extractMinutiae.sh)

### Minutiae Map Construction

- We have taken .xyt files which contains minutiae information.
- Run the python file of [src/minutiae_Map_Reconstruction/main.py](src/minutiae_Map_Reconstruction/main.py). May be input folder and target folder paths needs to be modified in this file.

### Training Data Creation

- First for each dataset we create the images in the following way:

  - Cross Match dataset (Both for fingerprints, minutiae maps)
    - the original dimensions are 504\*480.
    - we have applied in such a way that new dims are 504\*504.
    - Now we downscale the images until 256\*256.
    - The above 3 steps are performed by using the python script [src/tools/Downsampling_images_to_256.py](src/tools/Downsampling_images_to_256.py)
  - U.are.U dataset (Both for fingerprints, minutiae maps)
    - the original dimensions are 326\*357.
    - we have applied in such a way that new dims are 357\*357.
    - Now we downscale the images until 256\*256.
    - The above 3 steps are performed by using the python script [src/tools/Downsampling_images_to_256.py](src/tools/Downsampling_images_to_256.py)

- We should create the train, test, val sets of the downsampled images for both minutiae_Maps, fingerprints. This can be done by running the python script [src/tools/create_train_test_valid.py](src/tools/create_train_test_valid.py)
- Using the above mentioned train, test, val sets train the model of [pix2pix-network](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)

### Data Augmentation

- In order to do augmentation for the dataset as the size of the datasets are very low, run the python script [src/tools/data_Augmentation.py](src/tools/data_Augmentation.py)
- But augmentation didn't worked for our project.

### Evaluation

- Once the model is trained, now run the model for testing and it will gives us the reconstructed fingerprints.
- Now, we should perform the evaluation for the original fingerprints and reconstructed fingerprints by the model.
- The evaluation can be done by running the python script [src/tools/evaluation_p3.py](src/tools/evaluation_p3.py).

# Note

- The mentioned **Folder-Paths** needs to be corrected in the mentioned python script files.
- Please ignore the other files as we have tried with some other datasets(for example casia) and additional experiments, so we had written new scripts.
