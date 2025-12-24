import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_feature_correlation(
        data_path: str,
        numeric_columns: list[str],
        output_path: str
) -> None:
    
    df = pd.read_csv(data_path)

    corr_matrix = df[numeric_columns].corr()

    plt.figure(figsize=(12, 10))
    sns.heatmap(
        corr_matrix,
        cmap='coolwarm',
        annot=False,
        square=True,
    )
    plt.title('Feature Correlation Heatmap')
    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()