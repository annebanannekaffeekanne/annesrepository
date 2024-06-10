# import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import random

# load dataframe
train_df = pd.read_csv('/Users/anne/PycharmProjects/Semester4/machine_learning/semester_project'
                          '/breast-cancer_train.csv')

# create new dataframe with all columns exept the class-column with indice 0
df_wout_diagnosis = train_df.iloc[:,1:30]

# create normalized dataframe out of the selected columns
norm_train_df = (df_wout_diagnosis - df_wout_diagnosis.mean()) / df_wout_diagnosis.std()

# extract column 0 with the classes out of the original dataframe
column_0_copy = train_df["diagnosis"]

# insert copied column in the normalized dataframe
norm_train_df["diagnosis"] = column_0_copy

# split dataframe into Training Data and Validation Data (for Hyperparameter Tuning)
# select a third (1/3*381 = 127) of the rows randomly and 'cut' them out of the df into an new one
norm_valid_df = norm_train_df.sample(n=127).copy()

# create new training df with remaining data (normalized)
norm_train_df = norm_train_df.drop(norm_valid_df.index).reset_index(drop=True) # deletes the 127 rows from original df
                                                                               # which are now in the validation df

# 1. descriptive data-analysis of features and visualization
## get frequency of the classes -1 and 1
count_classes = train_df["diagnosis"].value_counts() # select class-column and count the total row-number
count_class_neg = count_classes.get(-1)              # get only the values for class -1 and count the rows
count_class_pos = count_classes.get(1)               # gett only the values for class 1 and count the rows
print(f"krebserkrankt:{count_class_neg}")
print(f"gesund:{count_class_pos}")

## pie chart for frequency
labels = ["Class -1", "Class 1"]
sizes = [count_class_neg, count_class_pos]
explode = (0.1, 0)

plt.figure(figsize=(7, 7))
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
plt.show()

print(" ")                                           # better overview
print(50 * "-")
print(" ")


## get maximum, minimum and average values of each column
for col, column in train_df.iloc[:, 1:].items():          # runs through all columns except the first (=class)
    print(f"Maximum von {col}:", column.max())            # returns max of the 30 columns
    print(f"Minimum von {col}", column.min())             # returns min of the 30 columns
    print(f"Durchschnitt von {col}:", column.mean())      # returns average of the 30 columns
    print(50 * "-")
print(" ")

## select relevant features
# calculate percentage of histogram-intersection of the different classes
class_0 = norm_train_df[norm_train_df['diagnosis'] == 1]  # selects only the values of the rows who belong to class 1
class_1 = norm_train_df[norm_train_df['diagnosis'] == -1] # selects only the values of the rows who belong to class -1

def histogram_intersection(h1, h2):                # calculates the intersection of two histograms
    minimum = np.minimum(h1, h2)                   # minimum of the given parameters
    intersection = np.sum(minimum)                 # intersection is the sum of the minima
    total_area = np.sum(h1)+np.sum(h2)             # total area of histogram is sum of the both areas
    percentage = (2* intersection /total_area)*100 # calculate percentage of intersection
    return percentage

relevant_features = []                      # list for relevant features
for feature in norm_train_df.columns[:-1]:  # runs through the last column with classes

    hist_class_0, bin_edges = np.histogram(class_0[feature], bins=10, density=True) # plots histograms for class 1
    hist_class_1, _ = np.histogram(class_1[feature], bins=bin_edges, density=True)  # plots histograms for class -1

    intersection_percentage = histogram_intersection(hist_class_0, hist_class_1) # intersection percentage is the
                                                       # method with the plotted histograms as h1 and h2
    if intersection_percentage < 45:                   # select only the columns, in which the intersection between the
        relevant_features.append(feature)              # classes is below 42 %. if that's given, add element to list
        print(f"{feature} ausgewählt mit einer Überschneidung "
              f"von {intersection_percentage:.2f} %")

## dataframes for further processing
relevant_feature_df = norm_train_df[relevant_features + ["diagnosis"]]# create dataframe with only the relevant features
valid_relevant_feature_df = norm_valid_df[relevant_features + ["diagnosis"]] # validation df with only relevant features

## create diagramms
count_relevant_features = len(relevant_features)                               # count relevant features
plot_columns = 4                                                               # columns of the subplots
plot_rows = (count_relevant_features + plot_columns -1) // plot_columns        # keep rows of subplots variable

fig, axes = plt.subplots(plot_rows, plot_columns, figsize=(15, plot_rows * 4)) # create subplots
if plot_rows == 1:
    axes = axes.flatten()                    # return a copy of the rows whose axes are flatten into 1-dimensional
else:
    axes = axes.flatten()

for i in range(count_relevant_features):                                          # runs through relevant features
    feature = relevant_features[i]                                                # creates i seaborn-histplots
    sns.histplot(data=relevant_feature_df, x=feature, hue= "diagnosis",
                 element="step", stat="density", common_norm=False, ax=axes[i])
plt.show()


fig, axes = plt.subplots(1, 2, figsize=(13,8))                 # create subplot
sns.heatmap(data=norm_valid_df[relevant_features], ax=axes[0]) # plot heatmap for relevant feature df
sns.heatmap(data=norm_train_df, ax=axes[1])                    # plot heatmap for normalized df
plt.show()

print(" ")        # better overview
print(50 * "-")
print(" ")


# 2. development of machine-learning approach
## implement gradient-descent-algorithm
X = relevant_feature_df.iloc[:,:-1].values             # df without last column (features)
y = relevant_feature_df.loc[:,"diagnosis"].values      # only last column (class)

n = X.shape[1]            # number of columns
m = X.shape[0]            # number of rows
eta = 0.05                # learning_rate

## methods which are useful for the gradient descent
# initialize weight-parameter
def initialize_parameter(n):
    w1 = np.random.uniform(0.0, 0.1, n)  # create random weight
    w0 = np.random.uniform(0.0, 0.1)     # create random bias
    return w1, w0

# predict class (y)
def predict(X, w1, w0):
    return np.dot(X, w1) + w0                                # scalarproduct of feature-value and weight-factor + bias

# square-error-function (to be minimized)
def error_function(X, y, w1, w0):
    return 1/2 * np.mean((y - predict(X, w1, w0)) ** 2)      # uses predicted value from method above and subtracts it
                                                             # from original class; 1/2 is a scaling factor
# calculate gradient through calculating
# partial derivatives for each w
def grad(X, y, w1, w0):
    y_pred = predict(X, w1, w0)       # method predict saved in variable y_pred
    error = y_pred - y                # error is predicted value for y minus original value
    pd_w1 = np.dot(X.T, error) / m    # partial derivative of w1 is scalarproduct of X (transposed) and the error
    pd_w0 = np.mean(error)            # partial derivative of w0 is the arithmetic mean of error
    return pd_w1, pd_w0

# update weights
def update(w1, w0, pd_w1, pd_w0, eta):
    w1 -= eta * pd_w1                  # recalculate w1: learning_rate multiplied with partial derivative of w1
    w0 -= eta * pd_w0                  # recalculate w0: learning_rate multiplied with partial derivative of w0
    return w1, w0

## application of algorithm
w1, w0 = initialize_parameter(n)    # initialize w1 and w0 with method
error_list =[]                      # empty list to see the error-development during running the algorithm
for i in range(n):                                  # runs through all columns
    for j in range(m):                              # runs through all rows
        pd_w1, pd_w0 = grad(X, y, w1, w0)           # save new partial derivatives using method grad
        w1, w0 = update(w1, w0, pd_w1, pd_w0, eta)  # save new weight-factors using the update method
        errors = error_function(X, y, w1, w0)       # save errors using the error method
        error_list.append(errors)                   # add errors to list

print(f"geringster Fehler: {error_list[m]}")
plt.figure(figsize=(10, 6))              # create plot to folow the error-development
plt.plot(error_list, label="E(w)")       # error development over the training-process
plt.show()
print(" ")
print(f"gewichtungsfaktor w1 pro Spalte: {w1}")
print(" ")
print(f"bias w0: {w0}")
print(50 * "-")
print(" ")

# 3. hyperparameter-tuning
## use validation data (norm_valid_df) to evaluate model and tune hyperparameter
## hyperparameter is learning-rate (eta)
X_val = valid_relevant_feature_df.iloc[:,:-1].values            # use all columns except the last
y_val = valid_relevant_feature_df.loc[:,"diagnosis"].values     # extract column

n_val = X_val.shape[1]            # number of columns
m_val = X_val.shape[0]            # number of rows

# class prediction for validation data
y_val_pred = predict(X_val, w1, w0)
y_val_pred_class = (np.where(y_val_pred >= 0, 1, -1))
val_error = error_function(X_val, y_val, w1, w0)
val_accuracy = np.mean(y_val_pred_class == y_val)

print(f"Klassenvorhersage für den Validierungsdatensatz: {y_val_pred_class}")
print(" ")
print(f"Genauigkeit auf Validierungsdatensatz: {val_accuracy}")
print(" ")
print(f"geringster Fehler der Validierungsdaten: {val_error}")

# dataframe with actual and predicted classes
result_df = pd.DataFrame({"actual diagnosis": y_val, "predicted diagnosis": y_val_pred_class})



