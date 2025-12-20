DATA_PATH = "data/raw/predictive_maintenance.csv"

TARGET_COLUMN = "Failure Type"

DROP_COLUMNS = [
    "UDI",
    "Product ID",
    "Target"
]

MODELS = [
    "logistic_regression",
    "desicion_tree",
    "random_forest"
]

RANDOM_STATE = 42

TEST_SIZE = [0.25, 0.2, 0.1] # 75:25, 80:20, 90:10

CV_FOLDS = 5

LABELS = [
    "Heat Dissipation Failure",
    "No Failure",
    "Overstrain Failure",
    "Power Failure",
    "Random Failures",
    "Tool Wear Failure",
]

FOCUS_CLASSES = [
    "Random Failures",
    "Tool Wear Failure",
]

RF_VARIANTS = [
    "default",
    "shallow",
    "conservative"
]