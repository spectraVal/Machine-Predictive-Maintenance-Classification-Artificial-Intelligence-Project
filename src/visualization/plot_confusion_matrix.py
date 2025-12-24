import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_confusion_matrix(
        cm_csv_path: str,
        output_path: str
) -> None:
    
    cm_df = pd.read_csv(cm_csv_path, index_col=0)

    plt.figure(figsize=(10, 8))
    sns.heatmap(
        cm_df,
        annot=True,
        fmt='d',
        cmap='Blues',
        cbar=False,
    )
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted Label')
    plt.ylabel('Actual Label')
    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()