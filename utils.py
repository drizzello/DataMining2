import datetime
import os
import glob
import pandas as pd
from IPython.display import Markdown, display
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize

def backup_dataframe(df, backup_dir="backups", base_filename="df_backup"):
   # Create backup directory if it doesn't exist
   os.makedirs(backup_dir, exist_ok=True)
    
   # Generate timestamped filename
   timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
   filename = f"{base_filename}_{timestamp}.csv"
   filepath = os.path.join(backup_dir, filename)
    
   # Save DataFrame to CSV
   df.to_csv(filepath, index=False)
   print(f"✅ Backup saved to {filepath}")

def load_latest_backup(backup_dir="backups", base_filename="df_backup"):
    pattern = os.path.join(backup_dir, f"{base_filename}_*.csv")
    backup_files = sorted(glob.glob(pattern), key=os.path.getmtime, reverse=True)

    if not backup_files:
        raise FileNotFoundError("❌ No backup files found.")

    latest_file = backup_files[0]
    print(f"📂 Loading latest backup: {latest_file}")
    return pd.read_csv(latest_file)

def printmd(string):
    display(Markdown(string))



def plot_multiclass_roc(y_true, y_score, class_names=None):
    n_classes = y_score.shape[1]
    y_true_bin = label_binarize(y_true, classes=list(range(n_classes)))

    fpr, tpr, roc_auc = {}, {}, {}

    for i in range(n_classes):
        fpr[i], tpr[i], _ = roc_curve(y_true_bin[:, i], y_score[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])

    plt.figure(figsize=(10, 8))
    for i in range(n_classes):
        label = f"{class_names[i]}" if class_names is not None else f"Class {i}"
        plt.plot(fpr[i], tpr[i], lw=2, label=f"{label} (AUC = {roc_auc[i]:.2f})")

    plt.plot([0, 1], [0, 1], "k--", lw=2)
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("Multi-class ROC Curve")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.tight_layout()
