# utils.py

"""
utils.py -> This file constists some useful functions that help us create 3 new dataset.
    """

import os
import zipfile
import shutil
import random
import logging
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tqdm.auto import tqdm



def setup_logging(log_file="process.log"):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s]: %(message)s",
    )

def unzip_data(file_path, save_path, unzip_path):
    """ Unzip a file into the specified directory. Fisrt Check if the file exists
    end if it doesn't exists unzip it.
       
    Args:
         - file_path (str): The file that will be unzipped
         - save_path (str): The path that unzipped folder will be saved.

    """
    if  os.path.exists(save_path):
        print(f"[INFO] The file is already uznipped.")
        
    else:
        print(f"[INFO] I'm unzipiing the file.")
        zip_ref = zipfile.ZipFile(file_path, 'r')
        zip_ref.extractall(unzip_path)
        zip_ref.close()

def walk_through_dir(dir_path):
    """
    Walks through dir_path returning its contents.
    """
    for dirpath, dirnames, filenames in os.walk(dir_path):
        print(f"There are {len(dirnames)} directories and {len(filenames)} images in {dirpath}")


def rename_folders(base_dir, translations):
    """Rename directories based on translations.

        Args:
        - target_dir (str): The directory where the folder are located.
        - translation (dir): The dictionary that the the animals translation are.
    """
    for old_name, new_name in translations.items():
        old_path = os.path.join(base_dir, old_name)
        new_path = os.path.join(base_dir, new_name)
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            logging.info(f"Renamed '{old_name}' to '{new_name}'.")
        else:
            logging.warning(f"Directory '{old_name}' not found, skipping.")



def view_random_images_from_classes(target_dir,classes):
    """
    The function selects a random image for every class and plot it.
    
    Args:
        target_dir: The directory that the classes are located.
        
    Return:
        Images for every class.
    """
    # Get all the class names (folders) in the target directory
   # classes = [cls for cls in os.listdir(target_dir) if os.path.isdir(os.path.join(target_dir, cls))]
    
    # Set up a figure with 2 rows and 5 columns
    num_classes = len(classes)
    fig, axes = plt.subplots(2, 5, figsize=(15, 8))  # 2 rows, 5 columns
    
    # Flatten axes for easier indexing if needed
    axes = axes.flatten()
    
    # Loop through classes and display a random image in each subplot
    for i, target_class in enumerate(classes):
        target_folder = os.path.join(target_dir, target_class)
        
        # Randomly select an image from the class folder
        random_image = random.choice(os.listdir(target_folder))
        
        # Load and display the image
        img = mpimg.imread(os.path.join(target_folder, random_image))
        axes[i].imshow(img)
        axes[i].set_title(target_class)
        axes[i].axis('off')
    
    # Turn off unused subplots if there are fewer than 10 classes
    for j in range(num_classes, 10):
        axes[j].axis('off')
    
    plt.tight_layout()
    plt.show()

def copy_images(source_dir, destination_dir, num_images):
    """
    Copies a specified number of images from the source directory to the destination directory.
    
    Args:
        - source_dir (str): Path to the source directory containing the images.
        - destination_dir (str): Path to the destination directory.
        - num_images (int): Number of images to copy.
    """
    # Get a list of all files in the source directory
    all_files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
    
    # Shuffle and pick the specified number of images
    selected_files = random.sample(all_files, min(num_images, len(all_files)))
    
    # Ensure the destination directory exists
    os.makedirs(destination_dir, exist_ok=True)
    
    # Copy each selected file to the destination directory
    for file_name in selected_files:
        source_path = os.path.join(source_dir, file_name)
        destination_path = os.path.join(destination_dir, file_name)
        shutil.copy(source_path, destination_path)
        print(f"Copied {file_name} to {destination_dir}")
    
    logging.info(f"\nSuccessfully copied {len(selected_files)} image(s) to {destination_dir}.")


def move_images(source_dir, destination_dir, num_images):
    """
    Copies a specified number of images from the source directory to the destination directory.
    
    Args:
        - source_dir (str): Path to the source directory containing the images.
        - destination_dir (str): Path to the destination directory.
        - num_images (int): Number of images to copy.
    """
    # Get a list of all files in the source directory
    all_files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
    
    # Shuffle and pick the specified number of images
    selected_files = random.sample(all_files, min(num_images, len(all_files)))
    
    # Ensure the destination directory exists
    os.makedirs(destination_dir, exist_ok=True)
    
    # Copy each selected file to the destination directory
    for file_name in selected_files:
        source_path = os.path.join(source_dir, file_name)
        destination_path = os.path.join(destination_dir, file_name)
        shutil.move(source_path, destination_path)
        print(f"Copied {file_name} to {destination_dir}")
    
    logging.info(f"\nSuccessfully copied {len(selected_files)} image(s) to {destination_dir}.")


def create_set(directory_path, moved_dir_path, classes ):
    """ Creates a new set by taking some images of an existing folder and copy it to another folder 

    Args:
        directory_path (str): The path that the images are.
        moved_dir_path (_type_): The folder that the images will be stored
        classes (_type_): The different animals. DEFAULT = CLASSES. 
    """
    for animal in tqdm(classes):
    
        # Create the source_dir 
        source_dir_loop = directory_path + f'/{animal}'

        # Create the destination directory for the loop
        destination_dir_loop = moved_dir_path + f'/{animal}'
        
        # if the destination dir loop exists, means that we already have the testing set
        if os.path.exists(destination_dir_loop):
            print(f"[INFO] The {destination_dir_loop} already exists.")
            pass
            
        else:
            print(f"[INFO] We start moving photos to create the test set.")
            move_images(source_dir = source_dir_loop,
                        destination_dir = destination_dir_loop,
                        num_images = 50 )
            

def delete_folder(directory_path,folder_path):
    """
    Deletes a folder and all its contents.
    
    Parameters:
    - folder_path (str): Path to the folder to be deleted.
    """
   
    shutil.rmtree(directory_path + folder_path)
    print(f"Folder '{directory_path + folder_path}' and its contents have been deleted.")

def delete_directory(directory_path):
    """
    Deletes a directory and its contents.

    Parameters:
    - directory_path (str): Path to the directory to be deleted.

    Returns:
    - str: A message indicating the result of the operation.
    """
    try:
        # Try to remove the directory (if empty)
        os.rmdir(directory_path)
        return f"{directory_path} removed successfully (empty)."
    except OSError:
        # If directory is not empty, remove all contents
        try:
            shutil.rmtree(directory_path)
            return f"{directory_path} and its contents removed successfully."
        except FileNotFoundError:
            return f"{directory_path} does not exist."
        except PermissionError:
            return f"Permission denied: unable to delete {directory_path}."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def copy_folder_structure_with_images(source_folder, destination_folder):
    """
    Copies the structure of a source folder, including all subfolders and images,
    to a destination folder.

    Parameters:
        source_folder (str): The path to the source folder.
        destination_folder (str): The path to the destination folder.
    """
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Walk through the source folder
    for root, dirs, files in os.walk(source_folder):
        # Compute the relative path from the source folder
        relative_path = os.path.relpath(root, source_folder)

        # Determine the target path in the destination folder
        target_path = os.path.join(destination_folder, relative_path)

        # Ensure the subfolder exists in the destination folder
        if not os.path.exists(target_path):
            os.makedirs(target_path)

        # Copy image files to the target path
        for file in files:
            # Check if the file is an image based on its extension
            if file.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif", ".tiff")):
                source_file = os.path.join(root, file)
                destination_file = os.path.join(target_path, file)

                # Copy the file
                shutil.copy2(source_file, destination_file)