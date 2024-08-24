import numpy as np

from mlxtend.classifier import Perceptron


def save_results(y_pred_mlxtend, errors_mlxtend, test_name):
    with open("log/perceptron_learning_results.log", "a") as f:
        f.write(f"Test: {test_name}\n")
        f.write(f"mlxtend Predictions:\n{y_pred_mlxtend}\n")
        f.write(f"mlxtend Errors: {errors_mlxtend}\n")
        f.write("-" * 50 + "\n")


def generate_easy_linearly_separable_data(n_samples=100):
    np.random.seed(42)
    X = np.random.randn(n_samples, 2) * 2
    y = np.array([1 if x[0] + x[1] > 0 else 0 for x in X])
    return X, y


def test_perceptron_learning():
    X, y = generate_easy_linearly_separable_data(n_samples=100)
    
    perceptron_mlxtend = Perceptron(eta=0.1, epochs=10, random_seed=42)
    perceptron_mlxtend.fit(X, y)
    errors_mlxtend = perceptron_mlxtend.cost_
    
    y_pred_mlxtend = perceptron_mlxtend.predict(X)
    
    save_results(y_pred_mlxtend, errors_mlxtend, "test_perceptron_learning")
    
    assert errors_mlxtend[0] > errors_mlxtend[-1], "Perceptron model ne uči; greška se nije smanjila!"
