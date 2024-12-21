"""
  Contains functionallities to make predictions and evaluate the model.
"""
# Import tqdm for progress bar
from tqdm.auto import tqdm
from torchmetrics import ConfusionMatrix
from mlxtend.plotting import plot_confusion_matrix

device = 'cuda' if torch.cuda.is_available() else 'cpu'
def make_predictions(model: torch.nn.Module,
                            test_dataloader: torch.utils.data.DataLoader, device = device):
    # 1. Make predictions with trained model
    y_preds = []
    y_targets = []  # Collect true targets to avoid re-fetching them
    model.eval()
    with torch.inference_mode():
        for X, y in tqdm(test_dataloader, desc="Making predictions"):
            # Send data and targets to target device
            X, y = X.to(device), y.to(device)
            # Do the forward pass
            y_logit = model(X)
            # Turn predictions from logits -> prediction probabilities -> prediction labels
            y_pred = torch.softmax(y_logit, dim=1).argmax(dim=1)
            # Collect predictions and targets
            y_preds.append(y_pred.cpu())  # Move predictions to CPU
            y_targets.append(y.cpu())     # Move targets to CPU

    # Concatenate list of predictions and targets into tensors
    y_pred_tensor = torch.cat(y_preds)
    y_target_tensor = torch.cat(y_targets)

    # Ensure both predictions and targets are on the same device (e.g., CPU)
    device = 'cpu'  # Change to 'cuda' if using GPU
    y_pred_tensor = y_pred_tensor.to(device)
    y_target_tensor = y_target_tensor.to(device)

    return(y_pred_tensor, y_target_tensor)

# Apply the function to create the predictions
y_pred_tensor , y_target_tensor = make_predictions(model = model, test_dataloader = valid_dataloader)

# 2. Setup confusion matrix instance and compare predictions to targets
confmat = ConfusionMatrix(num_classes=len(class_names), task='multiclass').to(device)  # Ensure metric is on the same device
confmat_tensor = confmat(preds=y_pred_tensor, target=y_target_tensor)

# 3. Plot the confusion matrix
fig, ax = plot_confusion_matrix(
    conf_mat=confmat_tensor.numpy(),  # matplotlib likes working with NumPy
    class_names=class_names,          # turn the row and column labels into class names
    figsize=(10, 7)
)

def accuracy_score(y_true, y_pred):
    # find the accuracy of the model in test set
    testing_accuracy = accuracy_fn(y_true =y_target_tensor , y_pred =y_pred_tensor )
    print(f"The testing accuracy is {testing_accuracy}")

def classification_report(y_true, y_pred):
  from sklearn.metrics import classification_report

  # Generate the classification report as a dictionary
  report = classification_report(y_target_tensor, y_pred_tensor, target_names=class_names, output_dict=True)

  # Filter out the overall metrics (like accuracy, macro avg, etc.)
  class_metrics = {label: metrics for label, metrics in report.items() if isinstance(metrics, dict)}

  # Find classes with the lowest recall and precision
  sorted_by_recall = sorted(class_metrics.items(), key=lambda x: x[1].get('recall', 0))
  sorted_by_precision = sorted(class_metrics.items(), key=lambda x: x[1].get('precision', 0))

  print("Classes with the lowest recall:")
  for label, metrics in sorted_by_recall[:3]:  # Show top 3 problematic classes
      print(f"{label}: Recall = {metrics.get('recall', 'N/A')}")

  print("\nClasses with the lowest precision:")
  for label, metrics in sorted_by_precision[:3]:  # Show top 3 problematic classes
      print(f"{label}: Precision = {metrics.get('precision', 'N/A')}")
