# 1. Data Preprocessing.
This is the first step of the project, in which we have to main goals.
1. Create 3 new datataset and every one of them will contain a different number or training images.
2. Change the structure of the data, in a format that is more useful for our project. The structure is the following.


The input of this process is the original dataset that contains 10 different classes of animals. The name of the classes is in Italian, so we need to fix this. Also, the dataset hasn't testing and validation files. 

The process of this step does the following:
1. Unzip the original Dataset.
2. Rename the folders in English
3. Create testing and validation sets.
4. Create a big training set, that contains all the images except the training and validation sets.
5. Create 3 Dataset:
    * `transformed_dataset_25_images`: Contains 25 images of every class. Total training images is 250.
    * `transformed_dataset_50_images`: Contains 50 images of every class. Total training images is 500.
    * `transformed_dataset_100_images`: Contains 100 images of every class. Total training images is 2500.
6. Copy the testing and validation sets to the previous 3 datasets.

Now, the dataset is in the right format that is the following.

```
transformed_dataset_25_images/ <- overall dataset folder
    train/ <- training images
        butterfly/ <- class name as folder name
            image01.jpeg
            image02.jpeg
            ...
        cat/
            image24.jpeg
            image25.jpeg
            ...
        chicken/
            image37.jpeg
            ...
    test/ <- testing images
        butterfly/
            image101.jpeg
            image102.jpeg
            ...
        cat/
            image154.jpeg
            image155.jpeg
            ...
        chicken/
            image167.jpeg
            ...
    vali/ <- testing images
        butterfly/
            image201.jpeg
            image202.jpeg
            ...
        cat/
            image254.jpeg
            image255.jpeg
            ...
        chicken/
            image267.jpeg
            ...

```

All the datasets has the same number of training and validation images. Finally, the 4 datasets contain the same test set that will be used for the final evaluation of the models.

The processes that walk through the dataset are stored in `data_preprocessing_folders` and contains the following files:
* `data_preprocessing.ipynb`  - It is the raw file that shows the process of modifying our data to create some datasets.
* `config.py` - Stored all the hyperparameters that is used in the following files.
* `utils.py` - Consists functionalities that was created in `data_preprocessing.ipynb`. By saving the functionalities in another file helps to have more clean code and improve it or maintain bases on the necessaries of every project.
* `main.py` - In this file we call the functions we have created in the `utils.py`. 