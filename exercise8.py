#Aufgabe1

def is_potential_gene(dna):
    if len(dna)%3 != 0:
        print("Sequenz besteht nicht aus Tripeln")
        return False
    if not dna.startswith("ATG"):
        print("Sequenz startet nicht mit Startcodon")
        return False
    if not dna.endswith("TAA") and not dna.endswith("TAG") and not dna.endswith("TGA"):
        print("Sequenz endet nicht mit Stoppcodon.")
        return False

    for i in range (3, len(dna)-3,3):
        if dna[i:i+3] == "TAA" or dna[i:i+3]== "TAG" or dna[i:i+3]=="TGA":
            print("enthält kein Stoppcodon in der Sequenz")
            return False
    else:
        print("Es handelt sich um eine DNA-Sequenz")
        return True


dna = input("Gensequenz eingeben:")
is_potential_gene(dna)


def zahlenraten(lowerindex, upperindex):
    if lowerindex > upperindex:
        return False
    else:
        center = (lowerindex + upperindex)//2
        print(f"ist die Zahl {center}?")
        antwort = input("Antwort")
        if antwort == "richtig":
            print("Juhuu!")
            return center
        elif antwort == "zu klein":
            return zahlenraten(center+1, upperindex)
        elif antwort == "zu groß":
            return zahlenraten(lowerindex, center-1)

zahlenraten(1,1000)