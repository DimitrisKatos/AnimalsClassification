"""
Contains PyTorch model code to instantiate a TinyVGG model.
"""
import torch
from torch import nn
# Create the model
model = torchvision.models.efficientnet_b0(weights = weights).to(device)


# Freeze the layers
for param in model.parameters():
    param.requires_grad = False

# Change the classifier
model.classifier = nn.Sequential(
    nn.Dropout(p = 0.2, inplace = True),
    nn.Linear(in_features = 1280, out_features = len(class_names))
    ).to(device)
