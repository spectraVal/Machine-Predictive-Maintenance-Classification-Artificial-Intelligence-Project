from plot_target_distribution import plot_target_distribution
from plot_confusion_matrix import plot_confusion_matrix
from plot_feature_correlation import plot_feature_correlation

def generate_all_visualizations():
    DATA_PATH = 'data/raw/predictive_maintenance.csv'
    TARGET_COLUMN = 'Failure Type'

    CONFUSION_MATRIX_PATH = 'outputs/confusion_matrix.csv'

    OUTPUT_DIR = 'outputs/visualization/'

    import os
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    plot_target_distribution(
        data_path=DATA_PATH,
        target_column=TARGET_COLUMN,
        output_path=f"{OUTPUT_DIR}/target_distribution.png"
    )

    plot_confusion_matrix(
        cm_csv_path=CONFUSION_MATRIX_PATH,
        output_path=f"{OUTPUT_DIR}/confusion_matrix_heatmap.png"
    )

    numeric_columns = [
        "Air temperature [K]",
        "Process temperature [K]",
        "Rotational speed [rpm]",
        "Torque [Nm]",
        "Tool wear [min]"
    ]

    plot_feature_correlation(
        data_path=DATA_PATH,
        numeric_columns=numeric_columns,
        output_path=f"{OUTPUT_DIR}/feature_correlation.png"
    )

if __name__ == "__main__":
    generate_all_visualizations()