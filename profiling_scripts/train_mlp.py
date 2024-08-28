import numpy as np
from sklearn.datasets import make_moons

from mlxtend.classifier import MultiLayerPerceptron


def generate_moons_data(n_samples=10000, noise=0.1, random_state=42):
    X, y = make_moons(n_samples=n_samples, noise=noise, random_state=random_state)
    return X, y

def main():
    X, y = generate_moons_data()

    eta = 0.01
    epochs = 1000
    n_classes = 2
    momentum = 0.9
    l1 = 0.0
    l2 = 0.01
    minibatches = 10
    random_seed = 42
    print_progress = 2
    hidden_layers = [23]

    mlp_classifier = MultiLayerPerceptron(
        eta=eta,
        epochs=epochs,
        n_classes=n_classes,
        momentum=momentum,
        l1=l1,
        l2=l2,
        minibatches=minibatches,
        random_seed=random_seed,
        print_progress=print_progress,
        hidden_layers=hidden_layers
    )
    mlp_classifier.fit(X, y)

    X_test, y_test = generate_moons_data()
    y_pred = mlp_classifier.predict(X_test)
    accuracy = np.mean(y_pred == y_test)
    print()
    print("Accuracy:", accuracy)


if __name__ == "__main__":
    main()
