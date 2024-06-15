# import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import random
from ml_gradient_descent_methods import*


## 2. Hyperparameter Tuning
def tune_eta_and_epochs(X, y, X_val, y_val):
    eta_values = [0.001, 0.01, 0.03, 0.05, 0.1]  # set examples for learning rate
    epoch_values = [100, 500, 1000, 1500, 2000]  # set examples for number of epochs
    best_eta = eta_values[0]  # define variables
    best_epoch = epoch_values[0]
    best_val_accuracy = 0

    for eta in eta_values:  # run through all given learning rates
        for epoch in epoch_values:  # and all given number of epochs
            w1, w0, error_list = gradient_descent(X, y, eta, epoch)  # apply algorithm

            y_val_pred = predict(X_val, w1, w0)  # predict weights for validation data
            y_val_pred_class = np.where(y_val_pred >= 0, 1, -1)  # predict class for validation data

            val_accuracy = np.mean(y_val_pred_class == y_val)  # calculate accuracy of the model

            if val_accuracy > best_val_accuracy:  # check if the current combination is better than the last
                best_val_accuracy = val_accuracy  # if it is, set new values
                best_eta = eta
                best_epoch = epoch
                #print(f"Neue beste Kombination: Lernrate = {eta}, Zyklen = {epoch}, Genauigkeit = {val_accuracy}")

    print(f"best learning-rate: {best_eta} with best amount of cycles: {best_epoch} and an accuracy of: {best_val_accuracy}")
    return best_eta, best_epoch, best_val_accuracy