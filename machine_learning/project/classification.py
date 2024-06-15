## import necessary methods
import pandas as pd

from ml_select_features_methods import*
from ml_data_analysis_methods import*
from ml_visualization_methods import*
from ml_gradient_descent_methods import*
from ml_tuning_methods import*

## 0. load dataframe
train_df = pd.read_csv('/Users/anne/PycharmProjects/Semester4/machine_learning/semester_project'
                          '/breast-cancer_train.csv')


## 1. Data Analysis
norm_df = load_and_normalize_data('/Users/anne/PycharmProjects/Semester4/'                       # normalize data
                                  'machine_learning/semester_project/breast-cancer_train.csv')

norm_train_df, norm_valid_df = split_data(norm_df, validation_size=0.33)  # split data into training and validation

max, min, mean = get_statistics(train_df)                                 # calculate basic statistics (max, min & mean)
print(max, min, mean)

print(" ")
print(50 * "-")


## 2. select relevant features and create new dataframes
relevant_features = get_relevant_features(norm_train_df, threshold=45)    # choose relevant features with less than
                                                                          # 45% of histogram intersection

relevant_feature_df = get_relevant_feature_dfs(norm_train_df, relevant_features)       # the relevant features# create dataframes only with
relevant_valid_feature_df = get_relevant_feature_dfs(norm_valid_df, relevant_features)

X, y = seperate_data(relevant_feature_df)                                # seperate traindata in feature and class
X_val, y_val = seperate_data(relevant_valid_feature_df)                  # same for validation data

print(" ")
print(50 * "-")


## 3. tune hyperparameter (learning rate)
best_eta, best_epoch, accuracy = tune_eta_and_epochs(X, y, X_val, y_val)      # choose best learning rate and epochs


## 4. Apply algorithm to train the model with best learning rate
w1, w0, error_list = gradient_descent(X, y, best_eta, best_epoch)     # calculate weights with traindata

y_val_pred = predict(X_val, w1, w0)                                   # use weights from  traindata for validation
y_val_pred_class = (np.where(y_val_pred >= 0, 1, -1))                 # predict class for validation data

val_error = error_function(X_val, y_val, w1, w0)                      # calculate 'last'/best error
val_accuracy = np.mean(y_val_pred_class == y_val)                     # calculate best accuracy

print(f"lowest error of validation data: {val_error}")
print(" ")
print(50 * "-")


result_df = pd.DataFrame({"actual_diagnosis": y_val,                  # df comparing predicted and actual class
                          "predicted_diagnosis": y_val_pred_class})



## 5. Visualize relevant results
generate_pie_chart(norm_df)                                           # pie chart of class distribution

generate_heatmaps(norm_train_df, relevant_feature_df)                 # heatmaps for normalized data
generate_heatmaps(relevant_feature_df, relevant_valid_feature_df)

plot_relevant_features(relevant_feature_df, relevant_features)        # create histograms of the relevant features

generate_error_plot(error_list)                                       # visualize error-development during algorithm-run

generate_bar_chart(result_df)


## 6. Apply on test data
# load test dataframe
test_df = pd.read_csv('/Users/anne/PycharmProjects/Semester4/machine_learning'
                      '/semester_project/breast-cancer_test.csv')
# normalize
norm_test_df = load_and_normalize_data('/Users/anne/PycharmProjects/Semester4/'
                                       'machine_learning/semester_project/breast-cancer_test.csv')

max, min, mean = get_statistics(test_df)                          # calculate basic statistics (max, min & mean)
print(max, min, mean)

# select relevant features

# create new dataframe
relevant_test_feature_df = get_relevant_feature_dfs(norm_valid_df, relevant_features) #attention! same relevant features as train df!

X_test, y_test = seperate_data(relevant_test_feature_df)                    # seperate testdata in feature and class

# apply algorithm
y_test_pred = predict(X_test, w1, w0)                                   # use weights from  traindata for test
y_test_pred_class = (np.where(y_val_pred >= 0, 1, -1))                  # predict class for test data

test_error = error_function(X_test, y_test, w1, w0)                      # calculate 'last'/best error
test_accuracy = np.mean(y_test_pred_class == y_test)                     # calculate best accuracy

print(f"lowest error of the test data: {test_error}.")
print(" ")
print(f"accuracy of the test data: {test_accuracy}.")
print(" ")
print(50 * "-")

# create result-df
test_result_df = pd.DataFrame({"actual_diagnosis": y_test,                  # df comparing predicted and actual class
                          "predicted_diagnosis": y_test_pred_class})

# visualize
generate_pie_chart(norm_test_df)

generate_bar_chart(test_result_df)

generate_confusion_matrix(y_test, y_test_pred_class)