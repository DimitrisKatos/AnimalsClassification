# Experiment Tracking
In this step we create the `experiment_tracking.ipynb` notebook where we create different models using different hyperparameters

We create totally 12 models changing the following:
- Use 2 models (EffNetB0 VS EffNetB2)
- Try different training time (5 VS 10 Epochs)
- Train using different number of images (25 VS 50 VS 100 training images in each class)

During the cahnges of the hyperparameters we found out which is the best model and will use it in production. 

Finally, we found out that the best model is: 
- Train in the biggest training datasets with 1000 images (100 for each class).
- Training for longer, 10 epochs.
- Using the EffNetB2 model. 
