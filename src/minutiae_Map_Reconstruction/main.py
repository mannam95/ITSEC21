import image_creation
if __name__ == '__main__':
    folder_path = 'D:/FingerPrint_Dataset/New_Exp/CASIA/CASIA_Minutiae/CASIA_Minutiae'
    size_x = 328
    size_y = 356
    output_folder = 'D:/FingerPrint_Dataset/New_Exp/CASIA/Minutiae/minutiaeMaps'
    threshold = 0

    image_creation.create_all_minutiae_maps(folder_path, size_x, size_y, output_folder, threshold)








    #for threshold in [0, 20, 40]:
        # image_creation.create_all_minutiae_maps(folder_path, threshold)
    #image_creation.plot_statistics(folder_path, [0, 20, 40])

    