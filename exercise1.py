from pillow import Image, ImageDraw
import random
def demo():
    image=Image.new("RGB",(600,360), color='white')               #erstellt weißes Bild mit width=600 & height=360
    image_draw = ImageDraw.Draw(image)
    y=20                                                          #Variabe y als Variable der Höhe
    for i in range(5):                                            #5 blaue Streifen zeichnen
        image_draw.rectangle(((50, y), (350, y+20)), fill='blue') #y als Starthöhe festgelegt
        y=y+40                                                    #Variable erhöhen, um Balken woanders zu zeichnen

    image_draw.rectangle(((50,20), (165,110)), fill='blue')       #blaues Quadrat links oben zeichnen

    image_draw.rectangle(((95,20),(115,125)), fill='white')       #vertikaler weißer Streifen des Kreuz'
    image_draw.rectangle(((50,60),(165,80)), fill='white')        #horizontaler weißer Streifen des Kreuz'
    image.show()
if __name__ == '__main__':
    demo()

#2 Schleifen und Arrays
if __name__== '__main__':
    grades =[5.0,2.3,1.7,2.0,3.7,1.3,2.3,3.3] #Liste der Noten
    sum=0                                     #Variable sum=0 erstellen
    for grade in grades:                      #durchläuft Notenliste
        sum += grade                          #Summe um Listenelement erhöhen
    x = sum/len(grades)                       #Variable x ist Summe der Listenelemente/Listenlänge
    print(x)                                  #gibt Durchschnittsnote zurück


#3 Verschachtelte Schleifen - Grafik
def Pyramide(n):                                                       #n=Anzahl an Kästchen der Basis
    image=Image.new("RGB",(2200,600), color='white')                   #erstellt Bild mit width=2200 & height=600
    draw_image = ImageDraw.Draw(image)

    x=1600                                                             #x-Koordinate des Startpunkts
    y=500                                                              #y-Koordinate des Startpunktes
    x0=50+x                                                            #x0 legt Breite der Kästchen fest
    for i in range(n):
        random_color=tuple(random.choices(range(256), k=3))            #Kästchen werden in beliebiger Farbe angemalt
        y = y-25                                                       #man arbeitet sich nach oben um Kästchenhöhe=25
        x = x0-x+0.5*x0                                                #
        #draw_image.rectangle(((x,y),(x+50,y-25)), fill=random_color)
        for j in range(n-i-1):
            random_color = tuple(random.choices(range(256), k=3))
            x = x + 50
            draw_image.rectangle(((x,y),(x+50,y-25)), fill=random_color)
    image.show()
Pyramide(15)


#def Pyramide(n):
#    image=Image.new("RGB", (1000, 1000), color='white')
#    draw_image = ImageDraw.Draw(image)

#    y = 900 #Startpunkt
#    x = 100

#    for i in range(n):
#        random_color=tuple(random.choices(range(256), k=3))
#        draw_image.rectangle(((x, y), (x + 50, y - 25)), fill=random_color)
#        x += 50 #neuer Startpunkt, um Kästchen aneinanderreihen zu können
#        y -= 25
#        for j in range(n-1):
#            x = 0.5*x + x #einrücken
                #y -= 25       #erhöhen
#            draw_image.rectangle(((x, y), (x , y)), fill=random_color)

#    image.show()
#Pyramide(15)
