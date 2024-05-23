import pandas as pd

from machine_learning import image_util
import os
import skimage
import matplotlib.pyplot as plt

# Aufgabe 1
# a
BASE_DIRECTORY = '/Users/anne/PycharmProjects/Semester4/machine_learning/exercises'
image = image_util.read(os.path.join(BASE_DIRECTORY,
                                     '/Users/anne/PycharmProjects/Semester4/machine_learning/images/image_00_014313_028576.png'),
                        as_gray=False)
image_util.show(image)

# b
df = pd.read_csv('/Users/anne/PycharmProjects/Semester4/machine_learning/data/tils.csv')  # dataframe = content of tils.csv
print(df)

# c
for _, row in df.iterrows():  # runs through all rows of dataframe
    row_start = row['row_start']  # provides access to the different components of a row
    row_end = row['row_end']
    col_start = row['col_start']
    col_end = row['col_end']

    rr, cc = skimage.draw.rectangle_perimeter((row_start, col_start),  # draws rectangle with given coordinates (df)
                                              end=(row_end, col_end), shape=image.shape)
    image[rr, cc] = (255, 0, 0, 255)  # color
image_util.show(image)  # shows image

# d
print("Reihen:", len(df))  # counts rows
print("Spalten:", len(df.columns))  # counts columns

# e
for row_start, column in df.iloc[:, :-1].items():  # runs through columns except the last
    print("Maximum:", column.max())  # returns max of the 4 columns
    print("Minimum:", column.min())
    print("Durchschnitt:", column.mean())
    print(" ")

# f
df.drop("annotator", axis=1, inplace=True)  # Possibility 1: deletes column with name 'annotator'
print(df)
# df = df.drop(df.columns[[4]], axis=1) #Possibility 2: deletes column with index 4 which ist the fifth
# print(df)


# g
df['Höhe'] = df['col_end'] - df['col_start']  # length of the line between col_end and col_start = height
df['Breite'] = df['row_end'] - df['row_start']  # "-" row_end and row_start = width
df['Fläche'] = df['Höhe'] * df['Breite']  # area is height*width
print(df)

# h
x = (df.Fläche >= 400)  # x as variable for areas >= 400
new_df = (df.loc[x, :])  # create new dataframe which returns boolean values for the area sizes
print(new_df)  # and selects only the 'True' rows
print(" ")

# i
# Usage: iloc based on position, loc based on name
wrong_value = new_df.iloc[7, -1]  # wrong value is located in column 7 in the last row
print("wrong value:", wrong_value)  # returns the value
new_df.iloc[7, -1] = wrong_value - 1  # sets new value for wrong_value (minus 1)
print(new_df)

# j
# ax = df.plot.hist(bins=10, alpha=0.5)
df['Fläche'].hist()  # creates histogram of the column area
plt.show()  # shows histogramm (pyplot)

# k
file = '../data/info_ML.xlsx'  # name of the excel file as variable file
with pd.ExcelWriter(file) as writer:  # converts dataframe to excel and
    df.to_excel(writer, sheet_name='Tabelle1', index=False)  # puts it in the given file and sheet
