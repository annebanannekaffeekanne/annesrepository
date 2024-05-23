import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# a
df = pd.read_csv('/Users/anne/PycharmProjects/Semester4/machine_learning/data/heart-2020-cleaned.csv')
# print(df)

# b
sns.set_theme(style='darkgrid')

# c
sns.displot(data=df, x="HeartDisease")
plt.show()

# d
sns.displot(data=df, x="HeartDisease", hue='Sex', stat='density')  # sum male and female=1
plt.show()
sns.displot(data=df, x="HeartDisease", hue='Sex', stat='density',
            common_norm=False)                                     # multiple='dodge' divides multiple layers; sum female=1, sum male=1
plt.show()

# e
fig, axes = plt.subplots(1, 2)                                     # creates 1 row and 2 columns for plots
sns.histplot(data=df, x="Smoking", ax=axes[0])                     # 2 histplots are divided by the ax-indice
sns.histplot(data=df, x="AlcoholDrinking", ax=axes[1])
plt.show()

# f
sns.scatterplot(data=df, x="PhysicalHealth", y="MentalHealth",
                hue="HeartDisease")                                # scatterplot=bullets, heartDiseases separated in different colors
plt.show()

# g
sns.boxplot(data=df, y="BMI", hue="HeartDisease")
plt.show()

# h
sns.histplot(data=df, x="GenHealth", hue="Sex", multiple="dodge")
plt.show()


sns.relplot(data=df, x="GenHealth", y="AgeCategory", hue="MentalHealth", size="PhysicalHealth")
plt.show()
