# import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import random

# gradient descent algorithm
def gradient_descent(X, y, eta, epochs):
    n = X.shape[1]                                          # number of columns
    m = X.shape[0]                                          # number of rows
    w1 = np.random.uniform(0.0, 0.1, n)                     # initialize n random weight-factors for each column
    w0 = np.random.uniform(0.0, 0.1)                        # initialize random bias

    def predict(X, w1, w0):
        return np.dot(X, w1) + w0                           # scalarproduct of feature-value and weight-factor + bias

    def error_function(X, y, w1, w0):
        return 1/2 * np.mean((y - predict(X, w1, w0)) ** 2) # uses predicted value from method above and subtracts it
                                                            # from original class; 1/2 is a scaling factor

    def grad(X, y, w1, w0):
        y_pred = predict(X, w1, w0)         # method predict saved in variable y_pred
        error = y_pred - y                  # error is predicted value for y minus original value
        pd_w1 = np.dot(X.T, error) / m      # partial derivative of w1 is scalarproduct of X (transposed) and the error
        pd_w0 = np.mean(error)              # partial derivative of w0 is the arithmetic mean of error
        return pd_w1, pd_w0

    def update(w1, w0, pd_w1, pd_w0, eta):
        w1 -= eta * pd_w1                   # recalculate w1: learning_rate multiplied with partial derivative of w1
        w0 -= eta * pd_w0                   # recalculate w0: learning_rate multiplied with partial derivative of w0
        return w1, w0
# epochs
    #epochs = 1000
    error_list = []                         # empty list to see the error-development during running the algorithm
    for i in range(epochs):                      # runs through all columns
        pd_w1, pd_w0 = grad(X, y, w1, w0)              # save new partial derivatives using method grad
        w1, w0 = update(w1, w0, pd_w1, pd_w0, eta)     # save new weight-factors using the update method
        errors = error_function(X, y, w1, w0)          # save errors using the error method
        error_list.append(errors)                      # add errors to list
    return w1, w0, error_list


# isolated methods of gradient descent
def predict(X, w1, w0):
    return np.dot(X, w1) + w0                                # scalarproduct of feature-value and weight-factor + bias

# square-error-function (to be minimized)
def error_function(X, y, w1, w0):
    return 1/2 * np.mean((y - predict(X, w1, w0)) ** 2)      # uses predicted value from method above and subtracts it

