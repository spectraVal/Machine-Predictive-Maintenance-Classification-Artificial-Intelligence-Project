import os
import pandas as pd


from src.config.base_config import *
from src.data.data_loader import load_dataset
from src.data.preprocessing import split_and_scale
from src.models.model_factory import create_model
from src.training.trainer import cross_validate_model
from src.evaluation.evaluator import evaluate
from src.analisis.analisis import run_error_analisis

def run_experiments():
    df = load_dataset(DATA_PATH)

    df = df.drop(columns=[c for c in DROP_COLUMNS if c in df.columns])

    x = df.drop(columns=[TARGET_COLUMN])
    y = df[TARGET_COLUMN]

    for model_name in MODELS:
        print(f"\n<<<=== MODEL: {model_name.upper()}===>>>")

        # variants = RF_VARIANTS if model_name == "random_forest" else ["default"]

        # for variant in variants:
        #     if model_name == "random_forest":
        #         print(f"\n<<=== RANDOM FOREST [{variant.upper()}]===>>")
            
        model = create_model(model_name)

        for test_size in TEST_SIZE:
            print(f"\n<=== Split {int((1 - test_size) * 100)}:{int(test_size * 100)} ===>")
                
            x_train, x_test, y_train, y_test = split_and_scale(
                x, y, test_size, RANDOM_STATE
            )

            scores = cross_validate_model(
                model, x_train, y_train, CV_FOLDS, RANDOM_STATE
            )
            print("CV Macro F1: ", scores.mean())

            model.fit(x_train, y_train)
            report = evaluate(model, x_test, y_test)
            print(report)

            if model_name in ["random_forest", "desicion_tree"]:
                run_error_analisis(
                    model=model,
                    x_test=x_test,
                    y_test=y_test,
                    label_names=LABELS,
                    focus_labels=FOCUS_CLASSES
                )
                    
if __name__ == "__main__":
    run_experiments()