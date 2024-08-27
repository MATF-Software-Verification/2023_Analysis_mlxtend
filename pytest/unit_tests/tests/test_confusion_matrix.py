import numpy as np
import os

from mlxtend.evaluate import confusion_matrix

from sklearn.metrics import confusion_matrix as sklearn_confusion_matrix


def save_results_confusion_matrix(test_name, y_target, y_predicted, cm, sklearn_cm, iteration):
    if not os.path.exists("log"):
        os.makedirs("log")

    with open(f"log/{test_name}_results.log", "a") as f:
        f.write(f"Test: {test_name}, Iteration: {iteration}\n")
        f.write(f"Target values:\n{y_target}\n")
        f.write(f"Predicted values:\n{y_predicted}\n")
        f.write(f"Confusion matrix (mlxtend):\n{cm}\n")
        f.write(f"Confusion matrix (sklearn):\n{sklearn_cm}\n")
        f.write("-" * 50 + "\n")


def test_confusion_matrix_binary_true():
    y_target = np.array([0, 1, 1, 0, 1, 0])
    y_predicted = np.array([0, 1, 0, 0, 1, 1])

    cm = confusion_matrix(y_target, y_predicted, binary=True)
    sklearn_cm = sklearn_confusion_matrix(y_target, y_predicted)

    save_results_confusion_matrix("test_confusion_matrix_binary_true", y_target, y_predicted, cm, sklearn_cm, 0)
    assert np.array_equal(cm, sklearn_cm), "Matrica konfuzije (binary=True) iz mlxtend se ne poklapa sa sklearn!"


def test_confusion_matrix_binary_false():
    y_target = np.array([0, 1, 2, 2, 1, 0])
    y_predicted = np.array([0, 2, 1, 2, 1, 0])

    cm = confusion_matrix(y_target, y_predicted, binary=False)
    sklearn_cm = sklearn_confusion_matrix(y_target, y_predicted)

    save_results_confusion_matrix("test_confusion_matrix_binary_false", y_target, y_predicted, cm, sklearn_cm, 0)
    assert np.array_equal(cm, sklearn_cm), "Matrica konfuzije (binary=False) iz mlxtend se ne poklapa sa sklearn!"


def test_confusion_matrix_binary_false_single_class():
    y_target = np.array([0, 0, 0, 0, 0])
    y_predicted = np.array([0, 0, 0, 0, 0])

    cm = confusion_matrix(y_target, y_predicted, binary=False)
    sklearn_cm = sklearn_confusion_matrix(y_target, y_predicted, labels=[0, 1])

    save_results_confusion_matrix("test_confusion_matrix_binary_false_single_class", y_target, y_predicted, cm, sklearn_cm, 0)
    assert np.array_equal(cm, sklearn_cm), "Matrica konfuzije (binary=False) za jednu klasu iz mlxtend se ne poklapa sa sklearn!"


def test_confusion_matrix_binary_false_multi_class():
    y_target = np.array([0, 1, 2, 2, 1, 0, 1, 2, 0, 1, 2])
    y_predicted = np.array([0, 2, 1, 2, 1, 0, 0, 2, 1, 1, 2])

    cm = confusion_matrix(y_target, y_predicted, binary=False)
    sklearn_cm = sklearn_confusion_matrix(y_target, y_predicted)

    save_results_confusion_matrix("test_confusion_matrix_binary_false_multi_class", y_target, y_predicted, cm, sklearn_cm, 0)
    assert np.array_equal(cm, sklearn_cm), "Matrica konfuzije (binary=False) za problem sa više klasa iz mlxtend se ne poklapa sa sklearn!"
