"""
  Contains functionality for creating PyTorch Dataloaders for
  image classification.
"""
import os
import torchvision
from torchvision import transforms
from torchvision import datasets
from torch.utils.data import DataLoader

NUM_WORKERS = os.cpu_count()

# Create a function that create Dataloaders
def create_dataloader(train_data: str,
                      test_data: str,
                      valid_data: str = None,
                      transform: transforms.Compose = None,
                      batch_size: int = 32,
                      num_workers :int = NUM_WORKERS):

    """ Create training, testing and validation dataloaders.

    Args:
      - train_data (str): Path to train directory
      - test_data (str) : Path to test directory
      - valid_data (str): Path to valid directory
      - transform (tranform.Compose) : Transform to perform on data (images)
      - batch_size (int) : Number of samples per batch in each of the Dataloaders

    Return:
      A tuple of the following:
        - train_dataloader (DataLoader)
        - test_dataloader (DataLoader)
        - valid_dataloader (DataLoader)
        - class_names (list) : List of the class names

    """

    # Create datasets for train and test
    train_dataset = datasets.ImageFolder(train_data, transform = transform)
    test_dataset = datasets.ImageFolder(test_data, transform = transform)

    # Create dataset and dataloader for validation if exists
    if valid_data:
      valid_dataset = datasets.ImageFolder(valid_data, transform = transform)
      valid_dataloader = DataLoader(valid_dataset, batch_size = batch_size, shuffle = False,
                                    num_workers = num_workers)
    else:
      print(f"[INFO] We don't have validation dataset")

    # the names of classes are
    class_names = train_dataset.classes

    # Create dataloaders
    train_dataloader = DataLoader(train_dataset, batch_size = batch_size, shuffle = True,
                                  num_workers = num_workers)
    test_dataloader = DataLoader(test_dataset, batch_size = batch_size , shuffle = False,
                                 num_workers = num_workers)

    print(f"[INFO] Dataloaders and datasets are created")

    return train_dataloader, test_dataloader, valid_dataloader, class_names
