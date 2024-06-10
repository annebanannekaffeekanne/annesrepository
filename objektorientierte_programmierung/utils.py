# utils.py

import numpy as np

def initialize_parameter(n):
    w1 = np.random.uniform(0.0, 0.1, n)
    w0 = np.random.uniform(0.0, 0.1)
    return w1, w0

def predict(X, w1, w0):
    return np.dot(X, w1) + w0

def error_function(X, y, w1, w0):
    return 0.5 * np.mean((y - predict(X, w1, w0)) ** 2)

def grad(X, y, w1, w0):
    y_pred = predict(X, w1, w0)
    error = y_pred - y
    pd_w1 = np.dot(X.T, error) / X.shape[0]
    pd_w0 = np.mean(error)
    return pd_w1, pd_w0

def update(w1, w0, pd_w1, pd_w0, eta):
    w1 -= eta * pd_w1
    w0 -= eta * pd_w0
    return w1, w0

