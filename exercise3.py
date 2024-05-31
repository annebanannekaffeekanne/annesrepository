#Aufgabe 2
def Bestellungen():
    #Aufforderung an Benutzer
    n = int(input("geben sie eine Anzahl an Bestellungen ein:"))
    #liste mit möglichen Verpackungseinheiten
    units =[500,200,50,20,10]

    #Schleife, die nacheinander listenelemente durchläuft und...
     #...die Nutzereingabe durch das 1. Listenelement ganzzahlig teilt...
     #...den Rest ermittelt...
     #... das ergebnis ausgibt und das nächste Listenelement annimmt
    for i in range(len(units)):
        x = n//units[i]
        n = n%units[i]
        print(units[i],"*",x)

Bestellungen()


#Aufgabe 3
#angabe beliebiger Verpackungseinheiten
def Verpackung():
    units=[]
    #Nutzereingabe: Anzahl Listenelemente/ Länge (eine Zahl: z.B 5)
    n=int(input("bitte geben sie eine Packungsanzahl ein:"))

    for i in range(n):
        #Nutzereingabe: Listenelemente (konkrete Zahlen; durch Schleife 5 separate Eingaben in Konsole)
        #mögliche Packungsgrößen werden festgelegt, also 500, 200,50,...
        units.append(input("bitte Packungsgröße eingeben:"))

        #Nutzereingabe: Stückzahl (=Bestellgröße: wie viele Objekte z.b. 1730
        #gleicher Teil wie Aufgabe 2
    k=int(input("bitte Stückzahl eingaben:"))
    for j in range(len(units)):
        x=k//int(units[j])
        k=k%int(units[j])
        print(x,"*",units[i])

Verpackung()
