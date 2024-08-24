import numpy as np
import pytest
import os

from mlxtend.feature_selection import SequentialFeatureSelector as SFS

from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_selection import SequentialFeatureSelector as SklearnSFS
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def save_results_sfs_cls(y_pred, y_test, sfs, test_name, y_pred_sklearn):
    if not os.path.exists("log"):
        os.makedirs("log")

    with open("log/sfs_with_classification_results.log", "a") as f:
        f.write(f"Test: {test_name}\n")
        f.write(f"mlxtend Selected features: {sfs.k_feature_idx_}\n")
        f.write(f"sklearn Selected features: {sfs.k_feature_idx_}\n")
        f.write(f"Scoring method: {sfs.scoring}\n")
        f.write(f"mlxtend Predictions:\n{y_pred}\n")
        f.write(f"sklearn Predictions:\n{y_pred_sklearn}\n")
        f.write(f"Are predictions the same? {'Yes' if all(y_pred == y_pred_sklearn) else 'No'}\n")
        f.write("-" * 50 + "\n")


def test_sfs_with_classification():
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    knn = KNeighborsClassifier(n_neighbors=3)
    sfs = SFS(knn, k_features=3, forward=True, floating=False, scoring='accuracy', cv=5)
    sfs = sfs.fit(X_train, y_train)
    
    knn.fit(X_train[:, sfs.k_feature_idx_], y_train)
    y_pred = knn.predict(X_test[:, sfs.k_feature_idx_])

    sklearn_sfs = SklearnSFS(knn, n_features_to_select=3, direction='forward', cv=5, scoring='accuracy')
    sklearn_sfs = sklearn_sfs.fit(X_train, y_train)
    knn_sklearn = KNeighborsClassifier(n_neighbors=3)
    knn_sklearn.fit(X_train[:, sklearn_sfs.get_support(indices=True)], y_train)
    y_pred_sklearn = knn_sklearn.predict(X_test[:, sklearn_sfs.get_support(indices=True)])

    save_results_sfs_cls(y_pred, y_test, sfs, "test_sfs_with_classification", y_pred_sklearn)
    
    assert len(sfs.k_feature_idx_) == 3, "Broj izabranih atributa mora biti 3!"


def test_sfs_with_one_feature_classification():
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    knn = KNeighborsClassifier(n_neighbors=3)
    sfs = SFS(knn, k_features=1, forward=True, floating=False, scoring='accuracy', cv=5)
    sfs = sfs.fit(X_train, y_train)
    
    knn.fit(X_train[:, sfs.k_feature_idx_], y_train)
    y_pred = knn.predict(X_test[:, sfs.k_feature_idx_])

    sklearn_sfs = SklearnSFS(knn, n_features_to_select=1, direction='forward', cv=5, scoring='accuracy')
    sklearn_sfs = sklearn_sfs.fit(X_train, y_train)
    knn_sklearn = KNeighborsClassifier(n_neighbors=3)
    knn_sklearn.fit(X_train[:, sklearn_sfs.get_support(indices=True)], y_train)
    y_pred_sklearn = knn_sklearn.predict(X_test[:, sklearn_sfs.get_support(indices=True)])

    save_results_sfs_cls(y_pred, y_test, sfs, "test_sfs_with_one_feature_classification", y_pred_sklearn)
    
    assert len(sfs.k_feature_idx_) == 1, "Broj izabranih atributa mora biti 1!"


def test_sfs_with_all_features_classification():
    # zapravo jedan manje od "all" po definiciji:
    # k_features : int or tuple or str (default: 1)
    #     Number of features to select,
    #     where k_features < the full feature set.
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    knn = KNeighborsClassifier(n_neighbors=3)
    sfs = SFS(knn, k_features=3, forward=True, floating=False, scoring='accuracy', cv=5)  # Svi atributi
    sfs = sfs.fit(X_train, y_train)
    
    knn.fit(X_train[:, sfs.k_feature_idx_], y_train)
    y_pred = knn.predict(X_test[:, sfs.k_feature_idx_])

    sklearn_sfs = SklearnSFS(knn, n_features_to_select=3, direction='forward', cv=5, scoring='accuracy')
    sklearn_sfs = sklearn_sfs.fit(X_train, y_train)
    knn_sklearn = KNeighborsClassifier(n_neighbors=3)
    knn_sklearn.fit(X_train[:, sklearn_sfs.get_support(indices=True)], y_train)
    y_pred_sklearn = knn_sklearn.predict(X_test[:, sklearn_sfs.get_support(indices=True)])

    save_results_sfs_cls(y_pred, y_test, sfs, "test_sfs_with_all_features_classification", y_pred_sklearn)
    
    assert len(sfs.k_feature_idx_) == 3, "Broj izabranih atributa mora biti 3!"


def test_sfs_empty_input():
    knn = KNeighborsClassifier(n_neighbors=3)
    sfs = SFS(knn, k_features=3, forward=True, floating=False, scoring='accuracy', cv=5)
    
    with pytest.raises(ValueError):
        sfs.fit(np.empty((0, 4)), np.empty((0,)))
