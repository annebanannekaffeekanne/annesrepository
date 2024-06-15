# import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import random

# methods for visualization
def generate_pie_chart(df):
    count_classes = df["diagnosis"].value_counts()                 # count all values of class-column
    labels = ["malignant", "benign"]
    sizes = [count_classes.get(-1, 0), count_classes.get(1, 0)]    # split counted classes in -1 and 1
    explode = (0.1, 0)

    plt.figure(figsize=(7, 7))
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.show()


def generate_heatmaps(norm_train_df, relevant_feature_df):
    fig, axes = plt.subplots(1, 2, figsize=(10, 8))                  # create subplots
    sns.heatmap(data=relevant_feature_df.iloc[:, :-1], ax=axes[0])   # heatmap for relevant features (normed)
    sns.heatmap(data=norm_train_df.iloc[:, :-1], ax=axes[1])         # heatmap for all features (normed)
    plt.show()


def plot_relevant_features(relevant_feature_df, relevant_features):
    count_relevant_features = len(relevant_features)                         # count number of relevant features
    plot_columns = 4                                                         # number columns of subplot
    plot_rows = (count_relevant_features + plot_columns - 1) // plot_columns # keep rows of subpplots variable

    fig, axes = plt.subplots(plot_rows, plot_columns, figsize=(15, plot_rows * 4))  # create subplots
    axes = axes.flatten()                                                           # flatten axes

    for i in range(count_relevant_features):                                 # iterate through relevant features
        feature = relevant_features[i]                                       # create histplot for each relevant feature
        sns.histplot(data=relevant_feature_df, x=feature, hue="diagnosis",
                     element="step", stat="density", common_norm=False, ax=axes[i])
    plt.show()


def generate_error_plot(error_list):
    plt.figure(figsize=(10, 6))
    plt.xlabel('epochs')
    plt.ylabel('error')
    plt.plot(error_list, label="E(w)")
    plt.show()



def generate_bar_chart(result_df):
    result_df.plot(kind='bar', figsize=(13, 8))
    plt.title(f'comparison of predicted and actual class')
    plt.xlabel('Row-count')
    plt.ylabel('Class')
    plt.xticks(rotation=0)
    plt.legend(loc='best')
    plt.show()

# confusion matrix
def generate_confusion_matrix(y_actual, y_pred):
    y_actual = y_actual.astype(int)
    y_pred = y_pred.astype(int)

    labels=np.unique(y_actual)

    conf_matrix = np.zeros((len(labels), len(labels)), dtype=int)

    for actual, predicted in zip(y_actual, y_pred):
        if actual == 1 and predicted == 1:
            conf_matrix[1,1] += 1
        elif actual == -1 and predicted == -1:
            conf_matrix[0,0] += 1
        elif actual == -1 and predicted == 1:
            conf_matrix[0,1] += 1
        elif actual == 1 and predicted == -1:
            conf_matrix[1,0] += 1

    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix, annot=True, fmt="d", xticklabels=labels, yticklabels=labels)
    plt.xlabel("predicted class")
    plt.ylabel("actual class")
    plt.title("confusion matrix")
    plt.show()