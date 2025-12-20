import numpy as np
from sklearn.metrics import confusion_matrix, classification_report

def run_error_analisis(
        model,
        x_test,
        y_test,
        label_names,
        focus_labels=None
) : 
    y_pred = model.predict(x_test)
    cm = confusion_matrix(y_test, y_pred)

    _print_global_summary(cm, label_names)
    _print_focus_class_errors(cm, label_names, focus_labels)

    return cm

def _print_global_summary(cm, labels):
    print("\n=== CONFUSION MATRIX (GLOBAL) ===")
    print("Rows: True Label | Cols: Predicted Label\n")

    header = " " * 18 + "".join(f"{l[:6]:>8}" for l in labels)
    print(header)

    for i, row in enumerate(cm):
        row_str = "".join(f"{v:>8}" for v in row)
        print(f"{labels[i][:15]:>15} {row_str}")
    
def _print_focus_class_errors(cm, labels, focus_labels):
    if not focus_labels:
        return
    
    print("\n=== FOCUS CLASS ERROR ANALYSIS ===")

    for label in focus_labels:
        idx = labels.index(label)
        row = cm[idx]

        total = row.sum()
        correct = row[idx]
        errors = total - correct

        print(f"\nClass: {label}")
        print(f"Total samples: {total}")
        print(f"Correct predictions: {correct}")
        print(f"Errors: {errors}")

        if errors > 0:
            print("Missclassified as: ")
            for j, count in enumerate(row):
                if j != idx and count > 0:
                    print(f" -> {labels[j]} : {count}")