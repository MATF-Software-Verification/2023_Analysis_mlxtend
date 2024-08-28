import numpy as np
from sklearn.datasets import make_classification

from mlxtend.classifier import LogisticRegression


def generate_classification_data(n_samples=50000, n_features=20, n_informative=10, 
                                 n_redundant=5, random_state=42):
    X, y = make_classification(n_samples=n_samples, n_features=n_features, 
                               n_informative=n_informative, n_redundant=n_redundant, 
                               n_classes=2, random_state=random_state)
    return X, y


def main():
    X, y = generate_classification_data()

    eta = 0.01
    epochs = 10000
    random_seed = 42
    print_progress = 2
    l2_lambda = 0.1

    logistic_regression_classifier = LogisticRegression(
        eta=eta,
        epochs=epochs,
        l2_lambda=l2_lambda,
        random_seed=random_seed,
        print_progress=print_progress
    )
    logistic_regression_classifier.fit(X, y)

    X_test, y_test = generate_classification_data()
    y_pred = logistic_regression_classifier.predict(X_test)
    accuracy = np.mean(y_pred == y_test)
    print()
    print("Accuracy:", accuracy)


if __name__ == "__main__":
    main()
