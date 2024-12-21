# main.py
import os
from config import *
from utils import *
from tqdm.auto import tqdm

def main():
    # Step 1: Set up logging
    setup_logging()

    delete_directory(directory_path= BASE_DIR +'/transformed_dataset_50_images')
    delete_directory(directory_path= BASE_DIR +'/transformed_dataset_100_images')
    delete_directory(directory_path= BASE_DIR +'/transformed_dataset_25_images')
    delete_directory(directory_path= BASE_DIR + '/tranformed_dataset_all_images')
    delete_directory(directory_path= BASE_DIR + '/valid')
    delete_directory(directory_path= BASE_DIR + '/test')

    # Step 2: Unzip dataset
    unzip_data(os.path.join(BASE_DIR, "animals10.zip"), RAW_DATA_DIR, unzip_path = BASE_DIR)

    # Step 2: Rename folders
    rename_folders(RAW_DATA_DIR, TRANSLATIONS)

    # Step 3: Create the same test and validation sets.
    # We create this test before the training datasets, because we want this sets to contain
    # Images that the model have never seen before.
    create_set(RAW_DATA_DIR, os.path.join(BASE_DIR, 'test'), classes= CLASSES, ) ### PROBLEM
    create_set(RAW_DATA_DIR, os.path.join(BASE_DIR, 'valid'), classes = CLASSES, )

    # Step 4: Create big training set that contains all the images.
    copy_folder_structure_with_images(BASE_DIR+ '/raw-img',
                                       BASE_DIR+'/tranformed_dataset_all_images/train')

    # Step 5: Create transformed datasets based on the number of images that we want.
    for dataset_name, num_images in DATASET_SIZES.items():
        dataset_path = os.path.join(BASE_DIR, dataset_name)
        for animal in TRANSLATIONS.values():
            source = os.path.join(RAW_DATA_DIR, animal)
            dest = os.path.join(dataset_path, 'train', animal)
            copy_images(source, dest, num_images= num_images)

    # Step 6: Add the transformed_data_all_images to the dictionary that store the name and the number of images
    # from each new dataset
    DATASET_SIZES['tranformed_dataset_all_images'] = 50

    # Step 7: Copy the test and validation sets in the new datasets.
    for dataset in DATASET_SIZES.keys():
        copy_folder_structure_with_images(BASE_DIR +'/test',  BASE_DIR+ f'/{dataset}'+'/test')
        copy_folder_structure_with_images(BASE_DIR +'/valid',  BASE_DIR+ f'/{dataset}' +'/valid')

    # Step 8: Remove the datasets, NOTE: only for storage managment. 
    '''delete_directory(directory_path= BASE_DIR +'/transformed_dataset_50_images')
    delete_directory(directory_path= BASE_DIR +'/transformed_dataset_100_images')
    delete_directory(directory_path= BASE_DIR +'/transformed_dataset_25_images')
    delete_directory(directory_path= BASE_DIR + '/tranformed_dataset_all_images')
    delete_directory(directory_path= BASE_DIR +'/raw-img')
    delete_directory(directory_path= BASE_DIR +'/test')
    delete_directory(directory_path= BASE_DIR + '/valid')'''
if __name__ == "__main__":
    main()
