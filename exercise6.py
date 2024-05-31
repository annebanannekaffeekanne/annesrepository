#Aufgabe2
def summeQuadratzahlen(n):
    if n == 1:
        return 1
    else:
        return (n ** 2) + (summeQuadratzahlen(n-1))

n = int(input("Geben sie eine Zahl ein:"))
print(summeQuadratzahlen(n))


#Aufgabe3
def maxStueckzahl(s):
    if s == 0:
        return 1
    elif s == 1:
        return 2
    else:
        return s + maxStueckzahl(s-1)

s = int(input("geben sie eine Anzahl an Schnitten ein:"))
print(maxStueckzahl(s))