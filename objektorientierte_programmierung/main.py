from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate():
    return render_template('generate.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/generate_analysis', methods=['POST'])
def generate_analysis():
    # Load and preprocess data
    train_df = pd.read_csv('breast-cancer_train.csv')
    df_wout_diagnosis = train_df.iloc[:, 1:30]
    norm_train_df = (df_wout_diagnosis - df_wout_diagnosis.mean()) / df_wout_diagnosis.std()
    column_0_copy = train_df["diagnosis"]
    norm_train_df["diagnosis"] = column_0_copy

    # Frequency of classes
    count_classes = train_df["diagnosis"].value_counts()
    count_class_neg = count_classes.get(-1)
    count_class_pos = count_classes.get(1)

    # Create pie chart
    labels = ["Class -1", "Class 1"]
    sizes = [count_class_neg, count_class_pos]
    explode = (0.1, 0)
    plt.figure(figsize=(7, 7))
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.savefig(os.path.join('static', 'pie_chart.png'))
    plt.close()

    # Heatmaps
    norm_valid_df = norm_train_df.sample(n=127).copy()
    norm_train_df.drop(norm_valid_df.index, inplace=True)
    sns.heatmap(data=norm_valid_df.iloc[:, :-1])
    plt.savefig(os.path.join('static', 'heatmap_valid.png'))
    plt.close()
    sns.heatmap(data=norm_train_df.iloc[:, :-1])
    plt.savefig(os.path.join('static', 'heatmap_train.png'))
    plt.close()

    # Error plot
    X = norm_train_df.iloc[:, :-1].values
    y = norm_train_df['diagnosis'].values
    n = X.shape[1]
    m = X.shape[0]
    eta = 0.05

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
        pd_w1 = np.dot(X.T, error) / m
        pd_w0 = np.mean(error)
        return pd_w1, pd_w0

    def update(w1, w0, pd_w1, pd_w0, eta):
        w1 -= eta * pd_w1
        w0 -= eta * pd_w0
        return w1, w0

    w1, w0 = initialize_parameter(n)
    error_list = []
    for i in range(100):  # Reduced to 100 iterations for brevity
        pd_w1, pd_w0 = grad(X, y, w1, w0)
        w1, w0 = update(w1, w0, pd_w1, pd_w0, eta)
        errors = error_function(X, y, w1, w0)
        error_list.append(errors)

    plt.figure(figsize=(10, 6))
    plt.plot(error_list, label="E(w)")
    plt.xlabel("Iteration")
    plt.ylabel("Error")
    plt.legend()
    plt.savefig(os.path.join('static', 'error_plot.png'))
    plt.close()

    return redirect(url_for('results'))


app.run(debug=True)


