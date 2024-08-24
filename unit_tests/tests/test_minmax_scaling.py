import numpy as np
import os

from mlxtend.preprocessing import minmax_scaling

from sklearn.preprocessing import MinMaxScaler


def save_results_minmax(X_mlxtend, X_sklearn, test_name, iteration):
    if not os.path.exists("log"):
        os.makedirs("log")

    with open("log/scaling_results.log", "a") as f:
        f.write(f"Test: {test_name}, Iteration: {iteration}\n")
        f.write(f"mlxtend result:\n{X_mlxtend}\n")
        f.write(f"sklearn result:\n{X_sklearn}\n")
        f.write(f"Are shapes the same? {'Yes' if X_mlxtend.shape == X_sklearn.shape else 'No'}\n")
        f.write(f"Are values close? {'Yes' if np.allclose(X_mlxtend, X_sklearn) else 'No'}\n")
        f.write("-" * 50 + "\n")


def test_minmax_scaling():
    X = np.random.rand(1000, 3) * 100
    
    X_scaled_mlxtend = minmax_scaling(X, columns=[0, 1, 2])
    
    scaler = MinMaxScaler()
    X_scaled_sklearn = scaler.fit_transform(X)

    save_results_minmax(X_scaled_mlxtend, X_scaled_sklearn, "test_minmax_scaling", 0)
    
    assert np.allclose(X_scaled_mlxtend, X_scaled_sklearn), "Skalirani podaci iz mlxtend se ne podudaraju sa očekivanim vrednostima iz sklearn!"


def test_minmax_scaling_constant_values():
    for i in range(100):
        value = np.random.uniform(low=-1000, high=1000)
        X = np.full((10, 3), value)
        X_scaled_mlxtend = minmax_scaling(X, columns=[0, 1, 2])
        scaler = MinMaxScaler()
        X_scaled_sklearn = scaler.fit_transform(X)

        save_results_minmax(X_scaled_mlxtend, X_scaled_sklearn, "test_minmax_scaling_constant_values", i)

        assert X_scaled_mlxtend.shape == X_scaled_sklearn.shape, "Oblik (shape) povratnih vrednosti se ne podudara!"
        assert np.allclose(X_scaled_mlxtend, X_scaled_sklearn), "MinMax skaliranje nije ispravno za konstantne vrednosti!"


def test_minmax_scaling_large_range():
    for i in range(100):
        X = np.random.uniform(low=1e-9, high=1e9, size=(10, 3))
        X_scaled_mlxtend = minmax_scaling(X, columns=[0, 1, 2])
        scaler = MinMaxScaler()
        X_scaled_sklearn = scaler.fit_transform(X)

        save_results_minmax(X_scaled_mlxtend, X_scaled_sklearn, "test_minmax_scaling_large_range", i)

        assert X_scaled_mlxtend.shape == X_scaled_sklearn.shape, "Oblik (shape) povratnih vrednosti se ne podudara!"
        assert np.allclose(X_scaled_mlxtend, X_scaled_sklearn), "MinMax skaliranje nije ispravno za vrednosti sa velikim opsegom!"


def test_minmax_scaling_negative_values():
    for i in range(100):
        X = np.random.uniform(low=-1000, high=0, size=(10, 3))
        X_scaled_mlxtend = minmax_scaling(X, columns=[0, 1, 2])
        scaler = MinMaxScaler()
        X_scaled_sklearn = scaler.fit_transform(X)

        save_results_minmax(X_scaled_mlxtend, X_scaled_sklearn, "test_minmax_scaling_negative_values", i)

        assert X_scaled_mlxtend.shape == X_scaled_sklearn.shape, "Oblik (shape) povratnih vrednosti se ne podudara!"
        assert np.allclose(X_scaled_mlxtend, X_scaled_sklearn), "MinMax skaliranje nije ispravno za negativne vrednosti!"


def test_minmax_scaling_single_row():
    for i in range(100):
        X = np.random.uniform(low=0, high=1000, size=(1, 3))
        X_scaled_mlxtend = minmax_scaling(X, columns=[0, 1, 2])
        scaler = MinMaxScaler()
        X_scaled_sklearn = scaler.fit_transform(X)

        save_results_minmax(X_scaled_mlxtend, X_scaled_sklearn, "test_minmax_scaling_single_row", i)

        assert X_scaled_mlxtend.shape == X_scaled_sklearn.shape, "Oblik (shape) povratnih vrednosti se ne podudara!"
        assert np.allclose(X_scaled_mlxtend, X_scaled_sklearn), "MinMax skaliranje nije ispravno kada se obrađuje samo jedan red podataka!"


def test_minmax_scaling_empty_data():
    X = np.array([])

    # kako sklearn reaguje na praznu listu
    scaler = MinMaxScaler()
    try:
        X_scaled_sklearn = scaler.fit_transform(X)
        sklearn_raises_error = False
    except ValueError:
        sklearn_raises_error = True

    # kako mlxtend reaguje na praznu listu
    try:
        X_scaled_mlxtend = minmax_scaling(X, columns=[0])
        mlxtend_raises_error = False
    except ValueError:
        mlxtend_raises_error = True

    # problem je ako sklearn javlja grešku, a mlxtend ne
    if sklearn_raises_error:
        assert mlxtend_raises_error, "mlxtend nije javio grešku kada je očekivano po sklearn standardu iz sklearn!"
    else:
        # Ako sklearn ne javlja grešku, uporedi rezultate
        save_results_minmax(X_scaled_mlxtend, X_scaled_sklearn, "test_minmax_scaling_empty_data", 0)
        assert np.allclose(X_scaled_mlxtend, X_scaled_sklearn), "MinMax skaliranje nije ispravno kada se obrađuje prazna lista!"


def test_minmax_scaling_nan_values():
    for i in range(100):
        X = np.random.uniform(low=0, high=1000, size=(10, 3))
        X[0, 0] = np.nan

        # kako sklearn reaguje na NaN vrednosti
        scaler = MinMaxScaler()
        try:
            X_scaled_sklearn = scaler.fit_transform(X)
            sklearn_raises_error = False
        except ValueError:
            sklearn_raises_error = True

        # kako mlxtend reaguje na NaN vrednosti
        try:
            X_scaled_mlxtend = minmax_scaling(X, columns=[0, 1, 2])
            mlxtend_raises_error = False
        except ValueError:
            mlxtend_raises_error = True

        # problem je ako sklearn javlja grešku, a mlxtend ne
        if sklearn_raises_error:
            assert mlxtend_raises_error, "mlxtend nije javio grešku kada je očekivano po standardu iz sklearn!"
        else:
            # ako sklearn ne javlja grešku, tek tada upoređujemo rezultate
            save_results_minmax(X_scaled_mlxtend, X_scaled_sklearn, "test_minmax_scaling_nan_values", i)
            assert np.allclose(X_scaled_mlxtend, X_scaled_sklearn), "MinMax skaliranje nije ispravno kada se obrađuju NaN vrednosti!"
