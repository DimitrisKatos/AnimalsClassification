
### 1. Imports and class names setup
import gradio as gr
import os 
import torch
import gradio as gr
import torchvision

from model import create_effnetb2_model
from timeit import default_timer as timer
from typing import Dict, Tuple

class_names = ['butterfly',  'cat',  'chicken',  'cow', 'dog',
               'elephant',  'horse',   'sheep',  'spider', 'squirrel']

### 2. Model and transforms prepartaion ###
effnetb2, effnetb2_transforms = create_effnetb2_model()

# Loade the save weights.
effnetb2.load_state_dict(torch.load(f = "effnetb2_model.pth",
                                    map_location = torch.device("cpu")))

### 3. Predict Function ###
effnetb2 = effnetb2.to('cpu')
def predict(img) -> Tuple[Dict, float]:
    """Transforms and performs a prediction on img and returns prediction and time taken.
    """
    
    # Start the timer
    start_time = timer()
    
    # Transform the target image and add a batch dimension
    img = effnetb2_transforms(img).unsqueeze(0)
    
    # Put model into evaluation mode and turn on inference mode
    effnetb2.eval()
    with torch.inference_mode():
        # Pass the transformed image through the model and turn the prediction logits into prediction probabilities
        pred_probs = torch.softmax(effnetb2(img), dim=1)
    
    # Create a prediction label and prediction probability dictionary for each prediction class (this is the required format for Gradio's output parameter)
    pred_labels_and_probs = {class_names[i]: float(pred_probs[0][i]) for i in range(len(class_names))}
    
    # Calculate the prediction time
    pred_time = round(timer() - start_time, 5)
    
    # Return the prediction dictionary and prediction time 
    return pred_labels_and_probs, pred_time

### 4. ### 

# Create title, description and article strings
title = "AnimalsClassification "
description = """An EfficientNetB2 feature extractor computer vision model to classify images of ten different animals.
                Curently the app can identify 10 diffferent animal species which is the following.
                1. Dog
                2. Cat
                3. Horse
                4. Butterfly
                5. Cow
                6. Chicken
                7. Sheep
                8. Squirrel
                9. Elephant
                10 Spider"""
article = "ModelDeployment"

# Create example list.
example_list = [["examples/" + example] for example in os.listdir('examples')]

# Create the Gradio demo
demo = gr.Interface(fn=predict, # mapping function from input to output
                    inputs=gr.Image(type="pil"), # what are the inputs?
                    outputs=[gr.Label(num_top_classes=3, label="Predictions"), # what are the outputs?
                             gr.Number(label="Prediction time (s)")], # our fn has two outputs, therefore we have two outputs
                    examples=example_list, 
                    title=title,
                    description=description,
                    article=article)

# Launch the demo!
demo.launch(debug=False, # print errors locally?
            share=True) # generate a publically shareable URL?
