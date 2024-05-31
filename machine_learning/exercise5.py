import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import pandas as pd

#Aufgabe 1
#a
data = np.loadtxt('/Users/anne/PycharmProjects/Semester4/machine_learning/data/diabetes.txt', comments=('%','@'), delimiter=',') # ignore 'at' and '%'

#b
random.shuffle(data)
#print(data)

#c
n = [1, 2, 3, 5, 10, 20]                                 # values for n in a list
for i in range(len(n)):                                  # values for n one after another
    folds = np.array_split(data, n[i])                   # splits data into n pieces
    print("")
    print("Fehler für jedes der n =", n[i],"Teile:")

#d
    list = []
    for j in range(len(folds)):                                                 # length of the n folds in range
        z = (folds[j][:, 8]).astype(int)                                                     # z is the position of column 9 at the given index
        pred = 19.867 + 0.027 * (folds[j][:, 5] - 58.153) ** 2 - folds[j][:, 7] # bmi values in column 6, age values in column 8
        pred_value = np.where(pred >= 0, 0, 1)                                  # predicition_value is 0 when prediction is >= 0
        training_error = np.sum(z != pred_value)/z.shape[0]                     # error calculation
        #print(training_error)
        list.append(training_error)                                             # creates list with the values of the errors
    print(list)

#e
    sns.boxplot(data=list)                                                      # create boxplot with list
    plt.xlabel(i)                                                               # label of x-axis is the index of the values of n
    plt.title(f"n = {n[i]}")                                                    # title is the values of n
    plt.show()

#f
# die Fehlerrange wird größer. je kleiner die Teildatensätze sind und je mehr Unterteilungen
# vorliegen, desto größer wird die Fehlervarianz (Boxplotgrenzen weiter auseinander)


#Zusatz
#a
def random_shuffle(data):                      # pass data
    n = len(data)                              # n is length of data
    for i in range(n):                         # iterate through data
        random_indices = random.randint(0, i)  # create random values with 'random.randint' between 0 and i
        new_indice = data[random_indices]      # new position of the row is the random_indice -> assign
        #print(new_indice)
random_shuffle(data)


#b
n = [2, 3, 5, 10, 20]                                                            # values for n in a list
new_array = []                                                                   # create empty array
for i in range(len(n)):                                                          # values for n one after another
    folds = np.array_split(data, n[i])                                           # splits data into n pieces

    list = []                                                                    # create empty list
    for j in range(len(folds)):                                                  # length of the n folds in range
        z = folds[j][:, 8]                                                       # z ist die Stelle der Spalte neun mit dem gegebenem index
        pred = 19.867 + 0.027 * (folds[j][:, 5] - 58.153) ** 2 - folds[j][:, 7]  # bmi values in column 6, age values in column 8
        pred_value = np.where(pred >= 0, 0, 1)                                   # predicition_value is 0 when prediction is >= 0 otherwise it's 1
        training_error = np.sum(z != pred_value) / z.shape[0]                    # error calculation

        list.append(training_error)                                              # adds the values of the errors to the list
    new_array.append(list)                                                       # adds the lists to the array
#print(new_array)
sns.boxplot(data=new_array)                                                      # create boxplot with array-data
plt.title(f"Boxplots für n = 2, 3, 5, 10 und 20")
plt.ylim(0, 1)                                                                   # sets upper border (=1) and lower border (=0)
plt.show()