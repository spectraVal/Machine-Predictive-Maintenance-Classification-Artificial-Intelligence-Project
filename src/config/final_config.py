DATA_PATH = "data/raw/predictive_maintenance.csv"

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