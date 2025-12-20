from sklearn.model_selection import StratifiedKFold, cross_val_score

def cross_validate_model(model, x, y, n_splits: int, random_state: int):
    cv = StratifiedKFold(
        n_splits=n_splits,
        shuffle=True,
        random_state=random_state
    )

    scores = cross_val_score(
        model,
        x,
        y,
        cv=cv,
        scoring="f1_macro"
    )

    return scores