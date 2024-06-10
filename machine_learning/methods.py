# import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import random


def load_and_normalize_data(filepath):
    df = pd.read_csv(filepath)
    df_wout_diagnosis = df.iloc[:, 1:30]
    norm_df = (df_wout_diagnosis - df_wout_diagnosis.mean()) / df_wout_diagnosis.std()
    norm_df["diagnosis"] = df["diagnosis"]
    return norm_df

def split_data(df, validation_size=0.33):
    norm_valid_df = df.sample(frac=validation_size).copy()
    norm_train_df = df.drop(norm_valid_df.index).reset_index(drop=True)
    return norm_train_df, norm_valid_df

def generate_pie_chart(df):
    count_classes = df["diagnosis"].value_counts()
    labels = ["Class -1", "Class 1"]
    sizes = [count_classes.get(-1, 0), count_classes.get(1, 0)]
    explode = (0.1, 0)

    plt.figure(figsize=(7, 7))
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.show()

def generate_heatmaps(train_df, valid_df):
    fig, axes = plt.subplots(1, 2, figsize=(13, 8))  # create subplot
    sns.heatmap(data=valid_df.iloc[:, :-1], ax=axes[0])

    sns.heatmap(data=train_df.iloc[:, :-1], ax=axes[1])
    plt.show()


def get_statistics(df):
    stats = {}
    for col in df.columns[1:]:
        stats[col] = {
            "max": df[col].max(),
            "min": df[col].min(),
            "mean": df[col].mean()
        }
    return stats


def histogram_intersection(h1, h2):
    minimum = np.minimum(h1, h2)
    intersection = np.sum(minimum)
    total_area = np.sum(h1) + np.sum(h2)
    percentage = (2 * intersection / total_area) * 100
    return percentage


def get_relevant_features(norm_train_df, threshold=45):
    class_0 = norm_train_df[norm_train_df['diagnosis'] == 1]
    class_1 = norm_train_df[norm_train_df['diagnosis'] == -1]
    relevant_features = []

    for feature in norm_train_df.columns[:-1]:
        hist_class_0, bin_edges = np.histogram(class_0[feature], bins=10, density=True)
        hist_class_1, _ = np.histogram(class_1[feature], bins=bin_edges, density=True)

        intersection_percentage = histogram_intersection(hist_class_0, hist_class_1)
        if intersection_percentage < threshold:
            relevant_features.append(feature)
            print(f"{feature} ausgewählt mit einer Überschneidung von {intersection_percentage:.2f} %")

    return relevant_features

def plot_relevant_features(relevant_feature_df, relevant_features):
    count_relevant_features = len(relevant_features)  # Anzahl der relevanten Features zählen
    plot_columns = 4                                  # Spalten der Subplots
    plot_rows = (count_relevant_features + plot_columns - 1) // plot_columns  # Zeilen der Subplots variabel halten

    fig, axes = plt.subplots(plot_rows, plot_columns, figsize=(15, plot_rows * 4))  # Subplots erstellen
    axes = axes.flatten()  # Achsen flach machen, unabhängig von der Anzahl der Reihen

    for i in range(count_relevant_features):  # Durch relevante Features iterieren
        feature = relevant_features[i]  # Erstelle Histogramm-Plots für jedes relevante Feature
        sns.histplot(data=relevant_feature_df, x=feature, hue="diagnosis",
                     element="step", stat="density", common_norm=False, ax=axes[i])
    plt.show()

def get_relevant_feature_dfs(norm_train_df, norm_valid_df, relevant_features):
    relevant_feature_df = norm_train_df[relevant_features + ["diagnosis"]]
    valid_relevant_feature_df = norm_valid_df[relevant_features + ["diagnosis"]]
    return relevant_feature_df, valid_relevant_feature_df

def train_model(X, y, eta=0.05):
    n = X.shape[1]
    m = X.shape[0]
    w1 = np.random.uniform(0.0, 0.1, n)
    w0 = np.random.uniform(0.0, 0.1)

    def predict(X, w1, w0):
        return np.dot(X, w1) + w0

    def error_function(X, y, w1, w0):
        return 0.5 * np.mean((y - predict(X, w1, w0)) ** 2)

    def grad(X, y, w1, w0):
        y_pred = predict(X, w1, w0)
        error = y_pred - y
        pd_w1 = np.dot(X.T, error) / m
        pd_w0 = np.mean(error)
        return pd_w1, pd_w0

    def update(w1, w0, pd_w1, pd_w0, eta):
        w1 -= eta * pd_w1
        w0 -= eta * pd_w0
        return w1, w0

    error_list = []
    for i in range(n):
        for j in range(m):
            pd_w1, pd_w0 = grad(X, y, w1, w0)
            w1, w0 = update(w1, w0, pd_w1, pd_w0, eta)
            errors = error_function(X, y, w1, w0)
            error_list.append(errors)
    print(f"geringster Fehler: {error_list[m]}")
    return w1, w0, error_list

def generate_error_plot(error_list):
    plt.figure(figsize=(10, 6))
    plt.plot(error_list, label="E(w)")
    plt.legend()
    plt.show()