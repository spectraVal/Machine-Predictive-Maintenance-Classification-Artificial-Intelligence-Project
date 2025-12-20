import os
import pandas as pd

from src.config.final_config import (
    DATA_PATH,
    TARGET_COLUMN,
    DROP_COLUMNS,
    RANDOM_STATE,
    FINAL_MODEL,
    FINAL_SIZE,
    FINAL_VARIANT,
    OUTPUT_DIR
)
from src.data.data_loader import load_dataset
from src.data.preprocessing import split_and_scale
from src.models.model_factory import create_model
from src.evaluation.evaluator import evaluate
from sklearn.metrics import confusion_matrix

def final_main():
    # Load & prepare data

    df = load_dataset(DATA_PATH)
    df = df.drop(columns=[c for c in DROP_COLUMNS if c in df.columns])

    x = df.drop(columns=[TARGET_COLUMN])
    y = df[TARGET_COLUMN]

    # Train-test split

    x_train, x_test, y_train, y_test = split_and_scale(
        x,
        y,
        test_size=FINAL_SIZE,
        random_state=RANDOM_STATE
    )

    # Build Final Model

    model = create_model(
        name=FINAL_MODEL,
        variant=FINAL_VARIANT
    )

    # Train

    model.fit(x_train, y_train)

    # Predict

    y_pred = model.predict(x_test)

    # Save prediction output
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    prediction_df = pd.DataFrame({
        "actual": y_test.values,
        "predicted": y_pred
    })
    prediction_df.to_csv(
        os.path.join(OUTPUT_DIR, "prediction_results.csv"),
        index=False
    )

    # Save classification report
    report = evaluate(model, x_test, y_test)

    with open(os.path.join(OUTPUT_DIR, "classification_report.csv"), "w") as f:
        f.write(report)

    # Save confusion matrix
    cm = confusion_matrix(y_test, y_pred)

    cm_df = pd.DataFrame(cm)
    cm_df.to_csv(
        os.path.join(OUTPUT_DIR, "confusion_matrix.csv"),
        index=False
    )

    # Save model config
    with open(os.path.join(OUTPUT_DIR, "model_config.csv"), "w") as f:
        f.write("Random Forest Final Configuration\n")
        f.write(f"Model Variant: {FINAL_VARIANT}\n")
        f.write(f"Random State: {RANDOM_STATE}\n\n")

        for param, value in model.get_params().items():
            f.write(f"{param}: {value}\n")

if __name__ == "__main__":
    final_main()