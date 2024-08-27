import pytest
import os
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split


def save_results_sfs_regr(y_pred, y_test, sfs, test_name, y_pred_sklearn):
    if not os.path.exists("log"):
        os.makedirs("log")

    with open("log/sfs_with_regression_results.log", "a") as f:
        f.write(f"Test: {test_name}\n")
        f.write(f"mlxtend Selected features: {sfs.k_feature_idx_}\n")
        f.write(f"sklearn Selected features: {sfs.k_feature_idx_}\n")
        f.write(f"Scoring method: {sfs.scoring}\n")
        f.write(f"mlxtend R2 score: {sfs.k_score_}\n")
        f.write(f"mlxtend Predictions:\n{y_pred}\n")
        f.write(f"sklearn Predictions:\n{y_pred_sklearn}\n")
        f.write(f"Are predictions the same? {'Yes' if all(y_pred == y_pred_sklearn) else 'No'}\n")
        f.write("-" * 50 + "\n")


def test_sfs_with_regression():
    X, y = make_regression(n_samples=100, n_features=5, noise=0.1, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    lr = LinearRegression()
    sfs = SFS(lr, k_features=3, forward=True, floating=False, scoring='r2', cv=5)
    sfs = sfs.fit(X_train, y_train)
    
    lr.fit(X_train[:, sfs.k_feature_idx_], y_train)
    y_pred = lr.predict(X_test[:, sfs.k_feature_idx_])

    sklearn_sfs = SequentialFeatureSelector(lr, n_features_to_select=3, direction='forward', cv=5, scoring='r2')
    sklearn_sfs = sklearn_sfs.fit(X_train, y_train)
    lr_sklearn = LinearRegression()
    lr_sklearn.fit(X_train[:, sklearn_sfs.get_support(indices=True)], y_train)
    y_pred_sklearn = lr_sklearn.predict(X_test[:, sklearn_sfs.get_support(indices=True)])

    save_results_sfs_regr(y_pred, y_test, sfs, "test_sfs_with_regression", y_pred_sklearn)
    
    assert len(sfs.k_feature_idx_) == 3, "Broj selektovanih karakteristika mora biti 3!"
    assert sfs.scoring == 'r2', "Scoring mora biti 'r2'!"
    assert sfs.k_score_ > 0, "R2 bi trebalo da bude pozitivan!"  # više za praktičnu primenu, ne toliko za testiranje biblioteke


def test_sfs_with_one_feature():
    X, y = make_regression(n_samples=100, n_features=5, noise=0.1, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    lr = LinearRegression()
    sfs = SFS(lr, k_features=1, forward=True, floating=False, scoring='r2', cv=5)
    sfs = sfs.fit(X_train, y_train)
    
    lr.fit(X_train[:, sfs.k_feature_idx_], y_train)
    y_pred = lr.predict(X_test[:, sfs.k_feature_idx_])

    sklearn_sfs = SequentialFeatureSelector(lr, n_features_to_select=1, direction='forward', cv=5, scoring='r2')
    sklearn_sfs = sklearn_sfs.fit(X_train, y_train)
    lr_sklearn = LinearRegression()
    lr_sklearn.fit(X_train[:, sklearn_sfs.get_support(indices=True)], y_train)
    y_pred_sklearn = lr_sklearn.predict(X_test[:, sklearn_sfs.get_support(indices=True)])

    save_results_sfs_regr(y_pred, y_test, sfs, "test_sfs_with_one_feature", y_pred_sklearn)
    
    assert len(sfs.k_feature_idx_) == 1, "Broj selektovanih karakteristika mora biti 1!"
    assert sfs.k_score_ > 0, "R2 bi trebalo da bude pozitivan!"  # više za praktičnu primenu, ne toliko za testiranje biblioteke


def test_sfs_with_all_features():
    # zapravo jedan manje od "all" po definiciji:
    # k_features : int or tuple or str (default: 1)
    #     Number of features to select,
    #     where k_features < the full feature set.
    X, y = make_regression(n_samples=100, n_features=5, noise=0.1, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    lr = LinearRegression()
    sfs = SFS(lr, k_features=4, forward=True, floating=False, scoring='r2', cv=5)
    sfs = sfs.fit(X_train, y_train)
    
    lr.fit(X_train[:, sfs.k_feature_idx_], y_train)
    y_pred = lr.predict(X_test[:, sfs.k_feature_idx_])

    sklearn_sfs = SequentialFeatureSelector(lr, n_features_to_select=4, direction='forward', cv=5, scoring='r2')
    sklearn_sfs = sklearn_sfs.fit(X_train, y_train)
    lr_sklearn = LinearRegression()
    lr_sklearn.fit(X_train[:, sklearn_sfs.get_support(indices=True)], y_train)
    y_pred_sklearn = lr_sklearn.predict(X_test[:, sklearn_sfs.get_support(indices=True)])

    save_results_sfs_regr(y_pred, y_test, sfs, "test_sfs_with_all_features", y_pred_sklearn)
    
    assert len(sfs.k_feature_idx_) == 4, "Broj selektovanih karakteristika mora biti 4!"
    assert sfs.k_score_ > 0, "R2 bi trebalo da bude pozitivan!"  # više za praktičnu primenu, ne toliko za testiranje biblioteke


def test_sfs_with_no_features():
    X, y = make_regression(n_samples=100, n_features=5, noise=0.1, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    lr = LinearRegression()
    sfs = SFS(lr, k_features=0, forward=True, floating=False, scoring='r2', cv=5)
    
    with pytest.raises(AttributeError):
        sfs.fit(X_train, y_train)
