import numpy as np
import os

from mlxtend.evaluate import accuracy_score


def save_results_accuracy(test_name, method, y_target, y_predicted, score, expected_score, iteration):
    if not os.path.exists("log"):
        os.makedirs("log")

    with open("log/accuracy_evaluation_results.log", "a") as f:
        f.write(f"Test: {test_name}, Iteration: {iteration}, Method: {method}\n")
        f.write(f"Target values:\n{y_target}\n")
        f.write(f"Predicted values:\n{y_predicted}\n")
        f.write(f"Calculated accuracy score: {score}\n")
        f.write(f"Expected accuracy score: {expected_score}\n")
        f.write(f"Difference: {abs(score - expected_score)}\n")
        f.write("-" * 50 + "\n")


def test_accuracy_standard():
    y_target = np.array([0, 1, 2, 2, 1, 0])
    y_predicted = np.array([0, 1, 2, 2, 1, 0])

    score = accuracy_score(y_target, y_predicted, method="standard", normalize=True)
    expected_score = 1.0
    save_results_accuracy("test_accuracy_standard", "standard", y_target, y_predicted, score, expected_score, 0)
    assert score == expected_score, "Accuracy (method='standard') nije ispravna za savršene prognoze!"

    y_predicted = np.array([0, 1, 1, 2, 0, 0])
    score = accuracy_score(y_target, y_predicted, method="standard", normalize=True)
    expected_score = 4 / 6
    save_results_accuracy("test_accuracy_standard", "standard", y_target, y_predicted, score, expected_score, 1)
    assert score == expected_score, "Accuracy (method='standard') nije ispravna za nesavršene prognoze!"


def test_accuracy_binary():
    y_target = np.array([0, 1, 1, 0, 1, 0])
    y_predicted = np.array([0, 1, 0, 0, 1, 1])

    score = accuracy_score(y_target, y_predicted, method="binary", pos_label=1, normalize=True)
    expected_score = 2 / 3
    save_results_accuracy("test_accuracy_binary", "binary", y_target, y_predicted, score, expected_score, 0)
    assert score == expected_score, "Accuracy (method='binary') nije ispravna za pozitivnu klasu!"

    score = accuracy_score(y_target, y_predicted, method="binary", pos_label=0, normalize=True)
    expected_score = 2 / 3
    save_results_accuracy("test_accuracy_binary", "binary", y_target, y_predicted, score, expected_score, 1)
    assert score == expected_score, "Accuracy (method='binary') nije ispravna za negativnu klasu!"


def test_accuracy_average():
    y_target = np.array([0, 1, 2, 2, 1, 0])
    y_predicted = np.array([0, 2, 1, 2, 1, 0])

    score = accuracy_score(y_target, y_predicted, method="average", normalize=True)
    
    # posmatra se kao binarna klasifikacija gde su ostale klase suprotna klasa
    acc_class_0 = np.mean(np.where(y_target != 0, 1, 0) == np.where(y_predicted != 0, 1, 0))
    acc_class_1 = np.mean(np.where(y_target != 1, 1, 0) == np.where(y_predicted != 1, 1, 0))
    acc_class_2 = np.mean(np.where(y_target != 2, 1, 0) == np.where(y_predicted != 2, 1, 0))
    
    expected_score = (acc_class_0 + acc_class_1 + acc_class_2) / 3
    
    save_results_accuracy("test_accuracy_average", "average", y_target, y_predicted, score, expected_score, 0)
    assert np.isclose(score, expected_score), "Accuracy (method='average') nije ispravna."


def test_accuracy_balanced():
    y_target = np.array([0, 1, 2, 2, 1, 0])
    y_predicted = np.array([0, 2, 1, 2, 1, 0])

    score = accuracy_score(y_target, y_predicted, method="balanced", normalize=True)
    expected_score = (1.0 + 0.5 + 0.5) / 3 
    save_results_accuracy("test_accuracy_balanced", "balanced", y_target, y_predicted, score, expected_score, 0)
    assert np.isclose(score, expected_score), "Accuracy (method='balanced') nije ispravna."


def test_accuracy_mismatched_lengths():
    y_target = np.array([0, 1, 2])
    y_predicted = np.array([0, 1])

    try:
        accuracy_score(y_target, y_predicted)
        assert False, "Očekuje se AttributeError zbog neusklađenih dužina nizova!"
    except AttributeError:
        pass


def test_accuracy_invalid_method():
    y_target = np.array([0, 1, 2])
    y_predicted = np.array([0, 1, 2])

    try:
        accuracy_score(y_target, y_predicted, method="invalid_method")
        assert False, "Očekivana je ValueError zbog prosleđivanja nepostojeće metode!"
    except ValueError:
        pass
