import pytest
import os

from mlxtend.classifier import EnsembleVoteClassifier

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def save_results_vote_cls(y_pred, y_test, valid_classes, test_name, y_pred_sklearn):
    if not os.path.exists("log"):
        os.makedirs("log")

    with open("log/ensemble_vote_classifier_results.log", "a") as f:
        f.write(f"Test: {test_name}\n")
        f.write(f"mlxtend Predictions:\n{y_pred}\n")
        f.write(f"sklearn Predictions:\n{y_pred_sklearn}\n")
        f.write(f"Test data:\n{y_test}\n")
        f.write(f"Valid classes:\n{valid_classes}\n")
        f.write(f"Are all predictions valid? {'Yes' if all(pred in valid_classes for pred in y_pred) else 'No'}\n")
        f.write(f"Are predictions the same as sklearn? {'Yes' if all(y_pred == y_pred_sklearn) else 'No'}\n")
        f.write(f"Number of predictions: {len(y_pred)}; Number of test samples: {len(y_test)}\n")
        f.write("-" * 50 + "\n")


def test_ensemble_vote_classifier():
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    clf1 = LogisticRegression(random_state=42)
    clf2 = DecisionTreeClassifier(random_state=42)
    eclf = EnsembleVoteClassifier(clfs=[clf1, clf2], voting='hard')
    eclf.fit(X_train, y_train)
    y_pred = eclf.predict(X_test)

    sklearn_eclf = VotingClassifier(estimators=[('lr', clf1), ('dt', clf2)], voting='hard')
    sklearn_eclf.fit(X_train, y_train)
    y_pred_sklearn = sklearn_eclf.predict(X_test)

    valid_classes = set(y_train)

    save_results_vote_cls(y_pred, y_test, valid_classes, "test_ensemble_vote_classifier", y_pred_sklearn)

    assert len(y_pred) == len(y_test), "Dužina predikcija mora biti jednaka dužini test uzorka!"
    assert all(pred in valid_classes for pred in y_pred), "Sve predikcije moraju biti unutar skupa validnih klasa!"


def test_ensemble_vote_classifier_single_classifier():
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    clf1 = LogisticRegression(random_state=42)
    eclf = EnsembleVoteClassifier(clfs=[clf1], voting='hard')  # Samo jedan klasifikator
    eclf.fit(X_train, y_train)
    y_pred = eclf.predict(X_test)

    sklearn_eclf = VotingClassifier(estimators=[('lr', clf1)], voting='hard')
    sklearn_eclf.fit(X_train, y_train)
    y_pred_sklearn = sklearn_eclf.predict(X_test)

    valid_classes = set(y_train)

    save_results_vote_cls(y_pred, y_test, valid_classes, "test_ensemble_vote_classifier_single_classifier", y_pred_sklearn)

    assert len(y_pred) == len(y_test), "Dužina predikcija mora biti jednaka dužini test uzorka!"
    assert all(pred in valid_classes for pred in y_pred), "Sve predikcije moraju biti unutar skupa validnih klasa!"


def test_ensemble_vote_classifier_no_voting():
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    clf1 = LogisticRegression(random_state=42)
    clf2 = DecisionTreeClassifier(random_state=42)
    eclf = EnsembleVoteClassifier(clfs=[clf1, clf2], voting=None)  # Bez glasanja
    
    with pytest.raises(ValueError):
        eclf.fit(X_train, y_train)


def test_ensemble_vote_classifier_soft_voting():
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    clf1 = LogisticRegression(random_state=42)
    clf2 = DecisionTreeClassifier(random_state=42)
    eclf = EnsembleVoteClassifier(clfs=[clf1, clf2], voting='soft')
    eclf.fit(X_train, y_train)
    y_pred = eclf.predict(X_test)

    sklearn_eclf = VotingClassifier(estimators=[('lr', clf1), ('dt', clf2)], voting='soft')
    sklearn_eclf.fit(X_train, y_train)
    y_pred_sklearn = sklearn_eclf.predict(X_test)

    valid_classes = set(y_train)

    save_results_vote_cls(y_pred, y_test, valid_classes, "test_ensemble_vote_classifier_soft_voting", y_pred_sklearn)

    assert len(y_pred) == len(y_test), "Dužina predikcija mora biti jednaka dužini test uzorka!"
    assert all(pred in valid_classes for pred in y_pred), "Sve predikcije moraju biti unutar skupa validnih klasa!"
