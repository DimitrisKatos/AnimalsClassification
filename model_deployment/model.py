import torch
import torchvision
from torch import nn

def create_effnetb2_model():
    # 1. Setup the pretrained EffNetB2 weights
    effnetb2_weights = torchvision.models.EfficientNet_B2_Weights.DEFAULT

    # 2. Setup the transforms
    effnetb2_transforms = effnetb2_weights.transforms()

    # 3. Setup pretrained model instance
    effnetb2 = torchvision.models.efficientnet_b2(weights = effnetb2_weights)

    # 4. Freeze the layers
    for param in effnetb2.parameters():
        param.requires_grad = False

    # 5. Change the classifier of the model
    effnetb2.classifier = nn.Sequential(
        nn.Dropout(p = 0.3, inplace = True),
        nn.Linear(in_features = 1408, out_features = 10, bias = True)
    )

    return effnetb2, effnetb2_transforms
