from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

def split_and_scale(
        x, y, test_size: float, random_state: int
):
    x_train, x_test, y_train, y_test =train_test_split(
        x, y, test_size=test_size, stratify=y, random_state=random_state
    )

    # HANDLE CATEGORICAL
    if 'Type' in x_train.columns:
        encoder = LabelEncoder()
        x_train['Type'] = encoder.fit_transform(x_train['Type'])
        x_test['Type'] = encoder.transform(x_test['Type'])

    # SCALING NUMERIC
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)

    return x_train_scaled, x_test_scaled, y_train, y_test