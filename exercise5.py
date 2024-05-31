#Aufgabe3
if __name__ == "__main__":
    n = int(input("enter number of cells:"))                    #gibt an, wie viele Zahlen eingegeben werden können
    cell_sequence = []                                          #erstellt Liste der Länge n
    for i in range(0, n):                                       #Schleife läuft von 0 bis n
        next_type = int(input("enter next cell type:"))         #ermöglicht Eingabe des Zelltyps
        cell_sequence.append(next_type)                         #fügt eingegebene Zelltypen in zuvor generierter
                                                                # Liste aneinander

    # a Anzahl der Zelltypen bestimmen
    typ1 = 0                                                    #Erzeugung 3er Variablen als mögliche Zelltypen
    typ2 = 0
    typ3 = 0
    for j in range(n):                                          #durchlaufen der Liste und untersuchen auf Möglichkeiten
        if cell_sequence[j] == 1:                               #entspricht Index der Liste dem Wert 1,
            typ1 += 1                                           #wird dessen Variable um 1 erhöht
        elif cell_sequence[j] == 2:                             #entspricht Index der Liste dem Wert 2,
            typ2 += 1                                           #wird dessen Variable um 1 erhöht
        elif cell_sequence[j] == 3:                             #entspricht Index der Liste dem Wert 3,
            typ3 += 1                                           #wird dessen Variable um 1 erhöht
        else:                                                   #wird kein definierter Typ erkannt,
            print("falscher Zelltyp")                           #bekommt Nutzer den Hinweis
    print("Typ1:", typ1, "x", ", Typ2:", typ2, "x", "und Typ3:", typ3, "x")

    #b prozentuale Verteilung der Zelltypen
    pTyp1=int((typ1 / n) * 100)                                     #Bestimmung der prozentualen Anteile der 3 Zelltypen
    pTyp2=int((typ2 / n) * 100)                                     #durch dividieren der Variablen durch Anzahl n
    pTyp3=int((typ3 / n) * 100)                                     #der Listenelemente und multiplizieren mit 100
    print("prozentualer Anteil Typ1:",pTyp1,"%")
    print("prozentualer Anteil Typ2:",pTyp2,"%")
    print("prozentualer Anteil Typ3:",pTyp3,"%")

    #c Bestimmung des häufigsten Zelltyps
    if pTyp1 > pTyp2 and pTyp1 > pTyp3:                         #Möglichkeit 1: Typ1 größer als 2 und 3
        print("Anteil Typ1 am größten")
    elif pTyp2 > pTyp1 and pTyp2 > pTyp3:                       #Möglichkeit 2: Typ2 größer als 1 und 3
        print("Anteil Typ2 am größten")
    elif pTyp3 > pTyp1 and pTyp3 > pTyp2:                       #Möglichkeit 3: Typ3 größer als 1 und 2
        print("Anteil Typ3 am größten")



#Zusatzaufgabe
    k = int(input("enter number of cell types:"))                     #Liste 1 mit Anzahl Zelltypen und deren Namen
    cell_types =[]                                                    #durch Nutzereingabe
    for h in range(1, k+1):
        possible_cell_type = int(input("enter name of the next possible cell type:"))
        cell_types.append(possible_cell_type)

    n = int(input("enter number of cells:"))                          #Liste 2 wie in Aufgabe3 ermglicht Eingabe
    cell_sequence = []                                                #der Anzahl an Zellen und um welche Zelltypen
    for i in range(0, n):                                             #es sich handelt
        cell_type = int(input("enter next cell type:"))
        cell_sequence.append(cell_type)

    matching_cells = []                                               #Liste 3 zählt Übereinstimmungen der Listen 1 & 2
    for j in range(len(cell_types)):                                  #Vergleich der ELemente aus Liste 1...
        for l in range(len(cell_sequence)):                           #...mit denen aus Liste 2
            if cell_types[j] == cell_sequence[l]:                     #Vergleich: wenn die Elemente sich entsprechen...
                matching_cells.append(cell_types[j])              #...wird der Liste das Element hinzugefügt
        p = matching_cells.count(cell_types[j])                #p zählt ob sich ein Element in Liste 3 wiederholt
        print(p,"mal typ",cell_types[j])
        x = int((p/n) * 100)                                  #berechnung des prozentualen Anteils
        print("prozentualer Anteil Typ", cell_types[j],":", x,"%")