# import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math

# load dataframe
df = pd.read_csv('/Users/anne/PycharmProjects/Semester4/machine_learning/semester_project/breast-cancer_train.csv')

# 1. descriptive data-analysis of features
## create new dataframe for each category (_mean, _se, _worst)
df_means = df.iloc[:, [0,1,2,3,4,5,6,7,8,9,10]].copy()
df_ses = df.iloc[:,[0,11,12,13,14,15,16,17,18,19,20]].copy()
df_worsts = df.iloc[:,[0,21,22,23,24,25,26,27,28,29,30]].copy()

## visualize data to estimate which feature is relevant to look at
fig, axes = plt.subplots(2, 5, figsize=(15,10))                                      # create 10 subplots
sns.boxplot(data=df_means, x="radius_mean", hue="diagnosis", ax=axes[0,0])           # plot for every feature of category _mean
sns.boxplot(data=df_means, x="texture_mean", hue="diagnosis", ax=axes[0,1])
sns.boxplot(data=df_means, x="perimeter_mean", hue="diagnosis", ax=axes[0,2])
sns.boxplot(data=df_means, x="area_mean", hue="diagnosis", ax=axes[0,3])
sns.boxplot(data=df_means, x="smoothness_mean", hue="diagnosis", ax=axes[0,4])
sns.boxplot(data=df_means, x="compactness_mean", hue="diagnosis", ax=axes[1,0])
sns.boxplot(data=df_means, x="concavity_mean", hue="diagnosis", ax=axes[1,1])
sns.boxplot(data=df_means, x="concave points_mean", hue="diagnosis", ax=axes[1,2])
sns.boxplot(data=df_means, x="symmetry_mean", hue="diagnosis", ax=axes[1,3])
sns.boxplot(data=df_means, x="fractal_dimension_mean", hue="diagnosis", ax=axes[1,4])
plt.show()

fig, axes = plt.subplots(2, 5, figsize=(15,10))                                  # create 10 subplots
sns.boxplot(data=df_ses, x="radius_se", hue="diagnosis", ax=axes[0,0])           # plot for every feature of category _se
sns.boxplot(data=df_ses, x="texture_se", hue="diagnosis", ax=axes[0,1])
sns.boxplot(data=df_ses, x="perimeter_se", hue="diagnosis", ax=axes[0,2])
sns.boxplot(data=df_ses, x="area_se", hue="diagnosis", ax=axes[0,3])
sns.boxplot(data=df_ses, x="smoothness_se", hue="diagnosis", ax=axes[0,4])
sns.boxplot(data=df_ses, x="compactness_se", hue="diagnosis", ax=axes[1,0])
sns.boxplot(data=df_ses, x="concavity_se", hue="diagnosis", ax=axes[1,1])
sns.boxplot(data=df_ses, x="concave points_se", hue="diagnosis", ax=axes[1,2])
sns.boxplot(data=df_ses, x="symmetry_se", hue="diagnosis", ax=axes[1,3])
sns.boxplot(data=df_ses, x="fractal_dimension_se", hue="diagnosis", ax=axes[1,4])
plt.show()

fig, axes = plt.subplots(2, 5, figsize=(15,10))                                        # create 10 subplots
sns.boxplot(data=df_worsts, x="radius_worst", hue="diagnosis", ax=axes[0,0])           # plot for every feature of category _worst
sns.boxplot(data=df_worsts, x="texture_worst", hue="diagnosis", ax=axes[0,1])
sns.boxplot(data=df_worsts, x="perimeter_worst", hue="diagnosis", ax=axes[0,2])
sns.boxplot(data=df_worsts, x="area_worst", hue="diagnosis", ax=axes[0,3])
sns.boxplot(data=df_worsts, x="smoothness_worst", hue="diagnosis", ax=axes[0,4])
sns.boxplot(data=df_worsts, x="compactness_worst", hue="diagnosis", ax=axes[1,0])
sns.boxplot(data=df_worsts, x="concavity_worst", hue="diagnosis", ax=axes[1,1])
sns.boxplot(data=df_worsts, x="concave points_worst", hue="diagnosis", ax=axes[1,2])
sns.boxplot(data=df_worsts, x="symmetry_worst", hue="diagnosis", ax=axes[1,3])
sns.boxplot(data=df_worsts, x="fractal_dimension_worst", hue="diagnosis", ax=axes[1,4])
plt.show()
## relevant features: the classes 1 and -1 are clearly seperated (the less the intersection, the better)

## extract relevant features an create diagramms for corresponding ones
fig, axes = plt.subplots(3, 3, figsize=(13, 8))
## radius and area
sns.scatterplot(data=df, x="radius_mean", y="area_mean", hue="diagnosis", ax=axes[0,0])
sns.scatterplot(data=df, x="radius_worst", y="area_worst", hue="diagnosis", ax=axes[0,2])
## texture and area
sns.scatterplot(data=df, x="texture_mean", y="area_mean", hue="diagnosis", ax=axes[0,1])
## compactness and perimeter
sns.scatterplot(data=df, x="compactness_mean", y="perimeter_mean", hue="diagnosis", ax=axes[1,0])
sns.scatterplot(data=df, x="compactness_worst", y="perimeter_worst", hue="diagnosis", ax=axes[1,1])
## perimeter and concave points
sns.scatterplot(data=df, x="perimeter_se", y="concave points_se", hue="diagnosis", ax=axes[1,2])
## concavity and fractal dimension
sns.scatterplot(data=df, x="fractal_dimension_mean", y="concavity_mean", hue="diagnosis", ax=axes[2,0])
## concavity and concave points
sns.scatterplot(data=df, x="concavity_mean", y="concave points_mean", hue="diagnosis", ax=axes[2,1])
sns.scatterplot(data=df, x="concave points_worst", y="concavity_worst", hue="diagnosis", ax=axes[2,2])
plt.show()


## knn-Algorithmus: Distanzen von einem Wert aus dem Testdatensatz zu allen Werten aus dem trainingdatensatz berechnen
## In Liste oder Dict speichern und sortieren, um die k=3 nächsten Nachbarn zu bestimmen.
## die Klassen dieser k=3 Nachbarn werden analysiert und dem Testdatensatz die entsprechende Klasse zugeordnet,
## die innerhalb der Nachbarn am meisten vertreten ist.

