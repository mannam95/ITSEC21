import image_creation
if __name__ == '__main__':
    folder_path = '../../data/CrossMatch_Sample_DB/minutiaeExtraction'
    #image_creation.create_all_minutiae_maps(folder_path, 504, 480, "../../data/CrossMatch_Sample_DB/Minutiae/minutiaeMaps")

    folder_path = '../../data/initial_Pre_Process_data/Minutiae/minutiaeExtraction'
    image_creation.create_all_minutiae_maps(folder_path, 326, 357, "../../data/initial_Pre_Process_data/Minutiae/minutiaeMaps")
    #for threshold in [0, 20, 40]:
        # image_creation.create_all_minutiae_maps(folder_path, threshold)
    #image_creation.plot_statistics(folder_path, [0, 20, 40])