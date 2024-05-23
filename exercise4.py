import numpy as np
import matplotlib.pyplot as plt


#Aufgabe 1
nx1, nx2 = (25, 25)                          # number of points per axe
x1 = np.linspace(15, 70, nx1)                # generates 25 values between 15 and 70
x2 = np.linspace(0, 80, nx2)                 # generates 25 values between 0 and 80
X1, X2 = np.meshgrid(x1, x2, indexing ='xy') # creates meshgrid

def classification_border(X1, X2):                   # method to calculate the values for classification border
    return 19.867 + 0.027 * (X1 - 58.153) ** 2 - X2  # calculation

class_limit_value = classification_border(X1, X2)

plt.contour(X1, X2, class_limit_value, levels=[0], colors='red') # only draws border

plt.scatter(X1[class_limit_value >= 0], X2[class_limit_value >= 0], color='b', label='Diabetes negativ') # set different colors
plt.scatter(X1[class_limit_value < 0], X2[class_limit_value < 0], color='r', label='Diabetes positiv')   # with condition for class_limit_value
plt.xlabel('BMI')
plt.ylabel('Age')
plt.legend()
plt.show()


# Aufgabe 2
#a
# load data
text = np.loadtxt('/Users/anne/PycharmProjects/Semester4/machine_learning/data/diabetes.txt', comments=('%','@'), delimiter=',') # ignore 'at' and '%'
#print(text)

#b
# visualize (bmi and age)
x = text[:, 5] # bmi values in column 6
y = text[:, 7] # age values in column 8
z = text[:, 8] # class 0 or 1 in column 9

plt.xlabel('BMI')
plt.ylabel('Age')
plt.scatter(x[z == 1], y[z == 1], color='b') # set different colors
plt.scatter(x[z == 0], y[z == 0], color='r') # with condition for z
plt.show()


#c
pred = 19.867 + 0.027 * (x - 58.153) ** 2 - y       # calculate prediction with given formula for h
pred_value = np.where(pred >= 0, 0, 1)              # predicition_value is 0 when prediction is >= 0 otherwise it's 1
training_error = np.sum(z != pred_value)/z.shape[0] # calculate the training_error: when z not equal to prediction_value divide through total-length of column
print(training_error)
