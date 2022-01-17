import image_creation
if __name__ == '__main__':
    folder_path = '../../data/CrossMatch_Sample_DB/Minutiae/minutiaeExtraction'
    size_x = 504
    size_y = 480
    output_folder = '../../data/CrossMatch_Sample_DB/Minutiae/minutiaeMaps'
    threshold = 0

    image_creation.create_all_minutiae_maps(folder_path, size_x, size_y, output_folder, threshold)








    #for threshold in [0, 20, 40]:
        # image_creation.create_all_minutiae_maps(folder_path, threshold)
    #image_creation.plot_statistics(folder_path, [0, 20, 40])

    