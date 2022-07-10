import image_creation
if __name__ == '__main__':
    
    
    input_path = '/home/srinath/Documents/git/ITSEC21/data/CrossMatch_Sample_DB/Minutiae/minutiaeExtraction'
    output_path = '/home/srinath/Documents/git/ITSEC21/data/CrossMatch_Sample_DB/Minutiae/minutiaeMaps'

    cross_match_x = 504
    cross_match_y = 480
    u_r_u_x = 328
    u_r_u_y = 356

    threshold = 0 # this is a parameter, consider the minutiae points only if their confidence score is more than this.

    image_creation.create_all_minutiae_maps(input_path, cross_match_x, cross_match_y, output_path, threshold)








    #for threshold in [0, 20, 40]:
        # image_creation.create_all_minutiae_maps(folder_path, threshold)
    #image_creation.plot_statistics(folder_path, [0, 20, 40])

    