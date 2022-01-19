import image_creation
if __name__ == '__main__':
    folder_path = '../../data/U_Are_U/Minutiae/minutiaeExtraction'
    size_x = 326
    size_y = 357
    output_folder = '../../data/U_Are_U/Minutiae/minutiaeMaps'
    threshold = 20

    image_creation.create_all_minutiae_maps(folder_path, size_x, size_y, output_folder, threshold)








    #for threshold in [0, 20, 40]:
        # image_creation.create_all_minutiae_maps(folder_path, threshold)
    #image_creation.plot_statistics(folder_path, [0, 20, 40])

    