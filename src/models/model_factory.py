from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

def create_model(name: str, variant: str = "default"):
    if name == "logistic_regression":
        return LogisticRegression(
            max_iter=1000,
            class_weight="balanced",
            solver="lbfgs"
        )

    if name == "desicion_tree":
        return DecisionTreeClassifier(
            criterion="gini",
            max_depth=10,
            min_samples_leaf=10,
            class_weight="balanced",
            random_state=42
        )
    
    if name == "random_forest":
        return _create_random_forest(variant)
    
    raise ValueError(f"Unknown model: {name}")
    
def _create_random_forest(variant: str):
    if variant == "default":
        return RandomForestClassifier(
            n_estimators=100,
            class_weight="balanced",
            random_state=42,
            n_jobs=-1
        )
        
    if variant == "shallow":
        return RandomForestClassifier(
            n_estimators=200,
            max_depth=10,
            min_samples_leaf=5,
            class_weight="balanced",
            random_state=42,
            n_jobs=-1
        )
        
    if variant == "conservative":
        return RandomForestClassifier(
            n_estimators=100,
            max_depth=8,
            min_samples_leaf=10,
            class_weight="balanced",
            random_state=42,
            n_jobs=-1
        )
    
    if variant == "final":
        return RandomForestClassifier(
            n_estimators=200,
            max_depth=10,
            min_samples_leaf=5,
            class_weight="balanced",
            random_state=42,
            n_jobs=-1
        )
    
    raise ValueError(f"Unknown Random Forest variant: {variant}")