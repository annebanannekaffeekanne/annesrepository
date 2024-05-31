#Aufgabe1
#iterative Lösung
def power_iterative(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    return result

#rekursive Lösung
def power_recursive(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power_recursive(base,exponent-1)

base = int(input("gib eine Basis ein:"))
exponent = int(input("gib einen Exponenten ein:"))
print(base,"hoch", exponent, "ergibt:",power_recursive(base,exponent))


#Aufgabe2
def Distanz():
    CITY_DISTANCES = [
        [0, 1108, 708, 1430, 732, 791, 2191, 663, 854, 748, 2483, 2625],       # 2d-Array: eine reihe stellt alle distanzen von
        [1108, 0, 994, 1998, 799, 1830, 3017, 1520, 222, 315, 3128, 3016],     # einer stadt zu allen anderen dar
        [708, 994, 0, 1021, 279, 1091, 2048, 1397, 809, 785, 2173, 2052],
        [1430, 1998, 1021, 0, 1283, 1034, 1031, 2107, 1794,1739,1255,1341],
        [732, 799, 279, 1283, 0, 1276, 2288, 1385, 649, 609, 2399, 2327],
        [791, 1830, 1091, 1034, 1276, 0, 1541, 1190, 1610, 1511,1911,2369],
        [2191, 3017, 2048, 1031, 2288, 1541, 0, 2716, 2794, 2703,387,1134],
        [663, 1520, 1397, 2107, 1385, 1190, 2716, 0, 1334, 1230,3093,3303],
        [854, 222, 809, 1794, 649, 1610, 2794, 1334, 0, 101, 2930, 2841],
        [748, 315, 785, 1739, 609, 1511, 2703, 1230, 101, 0, 2902, 2816],
        [2483, 3128, 2173, 1255, 2399, 1911, 387, 3093, 2930, 2902, 0,810],
        [2625, 3016, 2052, 1341, 2327, 2369, 1134, 3303, 2841, 2816,810,0],
    ]

    CITY_NAMES = ["Atlanta", "Boston", "Chicago", "Denver", "Detroit", "Houston", "Los Angeles", # namen stehen nacheinander vor den reihen
                  "Miami", "New York", "Philadelphia", "San Francisco", "Seattle"]               # atlanta hat index 0 und die distanzen zu den
                                                                                                 # anderen städten sind in der ersten reihe des 2d
    stadt1 = input("Städtename eingeben:")                                                       # array zu finden (gleicher index)
    stadt2 = input("nächsten Städtename eingeben:")
    index1 = 0
    index2 = 0

    for i in range(0,len(CITY_NAMES)): # durchläuft städtenamen-liste
        if stadt1 == CITY_NAMES[i]:    # wenn der input-name dem index der städtenamen-liste entspricht...
            index1 = i                 # ...variable index1 entspricht dem Spaltenindex der 1. stadt im 2d-array

    for j in range(0,len(CITY_NAMES)): # durchläuft städtenamen-liste
        if stadt2 == CITY_NAMES[j]:    # wenn der input-name dem index der städtenamen-liste entspricht...
            index2 = j                 # ...variable index2 entspricht dem Reihenindex der 2. Stadt im 2d-array

    distanz = CITY_DISTANCES[index1][index2]                         # Zugriff auf Spalte und Zeile -> gesuchter Wert der Distanz
    print("die Distanz der beiden Städte beträgt",distanz,"Meilen")

Distanz()


#Aufgabe3
import random
from PIL import Image, ImageDraw
def draw_mondrian(image_draw, x1, y1, x2, y2):
    if x1 < x2 and y1 < y2:
        random_color = tuple(random.choices(range(256),k=3))           # variable random_color wird definiert
        image_draw.rectangle(((x1, y1), (x2, y2)), fill=random_color)  # zeichnet rechteck mit random color
        if x1 == x2:
            return False
        else:
            return image_draw.rectangle((x1,y1),(x2,0.5*y2)) or \
                image_draw.rectangle((x1,y1),(0.5*x2,y2)) or False

#Aufruf der Methode:
if __name__ == '__übung7__':
    width, height = 500, 500                               # legt länge und höhe des ausgangsrechtecks fest
    image = Image.new("RGB",(width,height),color='white')  # kreiert weißes Bild, das es als Variable image speichert
    image_draw = ImageDraw.Draw(image)                     # Variable image_draw zeichnet das image
    draw_mondrian(image_draw, 0, 0, width, height)         # ruft Methode auf
    image.show()                                           # zeichnet