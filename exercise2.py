import numpy as np
import pandas as pd
import seaborn as sns
from machine_learning import image_util
import os
import matplotlib.pyplot as plt

# a
BASE_DIRECTORY = '/Users/anne/PycharmProjects/Semester4/'
image = image_util.read(os.path.join(BASE_DIRECTORY, 'machine_learning/images/image_00_014313_028576.png'),
                        as_gray=False)
image_util.show(image)

# b
df = pd.read_excel(
    '/Users/anne/PycharmProjects/Semester4/machine_learning/data/tils.xlsx')  # dataframe = content of tils.csv
print(df)

# c
df_num = df.to_numpy()  # convert dataframe into numpy-array
print(df_num)
print(df_num.dtype)

# d
mean = np.mean(df_num[:, -1])  # mean of column 'area'
print(mean)
median = np.quantile(df_num[:, -1], 0.5)  # median = 0.5-Quantil
print(median)
print(" ")

# e
means = np.mean(df_num, axis=0)  # mean of every column
print(means)
medians = np.quantile(df_num, 0.5, axis=0)
print(medians)
print(" ")

# f
x_zentrum = (df_num[:, 1] + df_num[:, 0]) // 2  # center between every row_start and row_end
y_zentrum = (df_num[:, 3] + df_num[:, 2]) // 2  # center between every column_start and column_end

print(x_zentrum)
print(" ")
print(y_zentrum)

# g
new_dimension_x = x_zentrum[..., np.newaxis]  # add dimension -> array as a column, prints one value in one row
new_dimension_y = y_zentrum[..., np.newaxis]  # add dimension
print(new_dimension_x)
print(new_dimension_y)
print(df_num[..., np.newaxis].shape)

# h
add_x_center = np.hstack((df_num, new_dimension_x))  # adds a new column with the values of 'new_dimension_x'
print(add_x_center)

new_df_num = np.hstack((add_x_center, new_dimension_y))  # adds a new column with the values of 'new_dimension_y'
print(new_df_num)

# i
print(new_df_num.dtype)  # returns the datatype of the array -> integer

# j
# install seaborn as sns

# k
plt.imshow(image)  # draws following data in the given image (a)
x = new_df_num[:, 8]  # x-coordinates from column 7 new_dimension_y
y = new_df_num[:, 7]  # y-coordinates from column 6 new_dimension_x
sns.scatterplot(x=x, y=y)  # plots data
plt.show()

# l
plt.imshow(image)  # draws following data in the given image
sns.kdeplot(x=x, y=y, fill=True, color="red", alpha=0.5)  # alpha = Transparency; x and y are defined in k)
plt.show()
