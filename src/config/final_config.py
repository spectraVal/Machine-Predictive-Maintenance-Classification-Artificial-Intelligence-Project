from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_PATH = PROJECT_ROOT / "data" / "raw"/ "predictive_maintenance.csv"

TARGET_COLUMN = "Failure Type"

DROP_COLUMNS = [
    "UDI",
    "Product ID",
    "Target"
]

FINAL_SIZE = 0.2 # 80:20

RANDOM_STATE = 42

FINAL_MODEL = "random_forest"

FINAL_VARIANT = "shallow"

OUTPUT_DIR = "outputs"