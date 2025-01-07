# config.py
"""
    In this file we initialize some parameters that will be using throughout the data
    transfromation. 
    
    BASE_DIR (str): The directory in computer that the project is stored.
    DATASET_URL (str): The path that the dataset will be downloaded as .zip
    RAW_DATA_DIR (str): The path of the unzip data.
    TRANSLATIONS (dir): Directory that stores the translation of the animals
    DATASET_SIZES (dir): As keys saved the names of the new datasets and as values
                        stores an integer that describe the number of images will have.
"""
import os

BASE_DIR = os.path.abspath("C:/Users/dimit/OneDrive/Desktop/my_work_git/AnimalsClassification/AnimalsClassification/data_preprocessing_folder")
DATASET_URL = "https://www.kaggle.com/datasets/alessiocorrado99/animals10"
RAW_DATA_DIR = os.path.join(BASE_DIR, "raw-img")
TRANSLATIONS = {
    "cane": "dog",
    "cavallo": "horse",
    "elefante": "elephant",
    "farfalla": "butterfly",
    "gallina": "chicken",
    "gatto": "cat",
    "mucca": "cow",
    "pecora": "sheep",
    "ragno": "spider",
    "scoiattolo": "squirrel",
}


CLASSES = [animal for animal in TRANSLATIONS.values()]

SETS = ['train', 'valid']

DATASET_SIZES = {
    'transformed_dataset_25_images': 25,
    'transformed_dataset_50_images': 50,
    'transformed_dataset_100_images': 100,
    'trasnformed_dataset_500_images': 500
    
}

FOLDER_TO_DELETE = [dataset for dataset in DATASET_SIZES.items()]