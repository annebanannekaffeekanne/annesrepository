# import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import random
from ml_data_analysis_methods import*


# methods to select relevant features
def get_relevant_features(norm_df, threshold=45):                # threshold is 45%
    class_0 = norm_df[norm_df['diagnosis'] == 1]                 # select rows with class 1
    class_1 = norm_df[norm_df['diagnosis'] == -1]                # select rows with class -1
    relevant_features = []                                       # empty list

    for feature in norm_df.columns[:-1]:                         # run through all columns exept the class-column
        hist_class_0, bin_edges = np.histogram(class_0[feature], bins=10, density=True)  # create histogram for class 1
        hist_class_1, _ = np.histogram(class_1[feature], bins=bin_edges, density=True)   # create hist for class -1

        intersection_percentage = histogram_intersection(hist_class_0, hist_class_1) # use method from data_analysis
        if intersection_percentage < threshold:                       # when intersection is lower than threshold
            relevant_features.append(feature)                         # add feature to list
            print(f"{feature} chosen with an intersection of {intersection_percentage:.2f} %")
    return relevant_features



def get_relevant_feature_dfs(norm_df, relevant_features):             # create df with relevant features
    relevant_feature_df = norm_df[relevant_features + ["diagnosis"]]
    #relevant_valid_feature_df = norm_valid_df[relevant_features] + ["diagnosis"]
    return relevant_feature_df





