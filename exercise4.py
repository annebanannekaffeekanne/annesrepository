#Aufgabe1
import random

def Party(n):
    count = 0                                        #Variable count wird eingeführt und gleich null gesetzt,
                                                     #sie zählt die Übereinstimmungen
    for l in range(100):                             #bei 100 durchläufen muss nur die Anzahl an Übereinstimmungen
                                                     #gezählt werden, um auf den Prozentwert zu kommen
        AnzahlGäste=[]                               #generiert Liste der Länge n mit Zahlen zwischen 0 und 364
        for q in range(n):
            AnzahlGäste.append(random.randrange(0,365))

        dopplungen = []                              #neue liste zählt Dopplungen
        i = len(AnzahlGäste)                         #i wird als Länge der generierten Liste definiert
        for j in range(i):                           #ist die innere Schleife durch, wird das nächste element
                                                     #der Liste als Vergleichswert angenommen
                                                     #der erste Wert für i wird festgelegt, mit dem die anderen
                                                     #verglichen werden sollen

            for k in range(j+1, i):                  #liste wird ab position nach j(=i) durchlaufen und so alle
                                                     # anderen Listenelemente mit dem festgelegten verglichen

                if AnzahlGäste[j]==AnzahlGäste[k]:   #prüft, ob zu vergleichendes element j mit listenelement
                                                     #übereinstimmt
                    dopplungen.append(1)
                                                     #fügt übereinstimmung(en) in Liste ein
        if len(dopplungen)>= 1:                      #besteht mind. eine Übereinstimmung wird variable count um 1 erhöht
            count += 1                               #variable count wird um 1 erhöht

    print("Die W-keit für mind. eine Übereinstimmung beträgt", count, "%.")

n = 200
for p in range(2, n):
    Party(p)

#Party(10)                                            #Methode wird aufgegriffen
#Party(20)
#Party(22)
#Party(23)
# Party(25)
# Party(50)
# Party(100)


#Aufgabe2
#def Trinkgeld():
#    Münzen=[1,5,10,20,50]