from sklearn.metrics import classification_report

def evaluate(model, x_test, y_test):
    y_pred = model.predict(x_test)
    return classification_report(
        y_test, 
        y_pred,
        zero_division=0
    )