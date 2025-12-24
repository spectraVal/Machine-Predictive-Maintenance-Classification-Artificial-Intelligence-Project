import pandas as pd
import matplotlib.pyplot as plt

def plot_target_distribution(
        data_path: str,
        target_column: str,
        output_path: str
) -> None:
    
    df = pd.read_csv(data_path)

    counts = df[target_column].value_counts().sort_index()

    plt.figure(figsize=(10, 6))
    counts.plot(kind='bar')
    plt.title('Distribution of Failure Types')
    plt.xlabel('Failure Type')
    plt.ylabel('Number of Samples')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()