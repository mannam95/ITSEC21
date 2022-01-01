import image_creation
if __name__ == '__main__':
    folder_path = '../../data/initial_Pre_Process_data/Minutiae/minutiaeExtraction'
    #for threshold in [0, 20, 40]:
        # image_creation.create_all_minutiae_maps(folder_path, threshold)
    image_creation.plot_statistics(folder_path, [0, 20, 40])