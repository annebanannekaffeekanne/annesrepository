from matplotlib import pyplot as plt
from draw_util import setup_plot, draw_line, draw_disk, draw_square_centered

if __name__ == '__main__':

    # draw figure
    def aufgabe1():
        setup_plot()                                       # setup plot
        for i in range(0, 14, 1):                          # linien:
            draw_line(0, 0.5+i, 13, 0.5+i, color='gray')   # senkrechte linien
            draw_line(0.5+i, 0, 0.5+i, 13, color='gray')   # waagerechte linien
            draw_line(12-i, 0, 13, 1+i, color='gray')      # diagonale linien von links oben nach rechts unten Richtung
            draw_line(0, 12-i, 1+i, 13, color='gray')      # geht nur bis null, deshalb das Gleiche in die andere
            draw_line(1+i, 0, 0, 1+i, color='gray')        # diagonale linien von rechts oben nach links unten
            draw_line(13, 12-i, 12-i, 13, color='gray')
        for o in range(0, 14, 4):                          # punkte
            for p in range(0, 14, 4):
                draw_disk(0.5+p, 0.5+o, 0.1, color='black')
        plt.show()                                         # show plot
    aufgabe1()


    def zusatz():
        setup_plot(range_dim1=(0, 15), range_dim2=(0,15))                 # setup plot
        for i in range(15):                                               # Schachbrettmuster:
            for j in range(15):
                if (i+j) % 2 == 0:                                        # nur jedes zweite Feld wird schwarz ausgemalt
                    draw_square_centered(0.5+i, 0.5+j, 1, color='black')
        for k in range(13):                                                           # kleine Quadrate
            for l in range(13):
                if (k+l) %2 != 0:                                                     # schwarz
                    if (k < 6 and l < 6) or (k > 6 and l > 6):                        # 2. und 4. Quadrant
                        draw_square_centered(1.2+k, 1.8+l, 0.15, color='black')       # Quadrat rechts oben
                        draw_square_centered(1.8 + k, 1.2 + l, 0.15, color='black')   # Quadrat links unten
                    if (k < 6 and l > 6) or (k > 6 and l < 6):                        # 1. und 3. Quadrant
                        draw_square_centered(1.2 + k, 1.2 + l, 0.15, color='black')   # Quadrat links oben
                        draw_square_centered(1.8 + k, 1.8 + l, 0.15, color='black')   # Quadrat rechts unten
                    if (k < 6 and l < 6.5) or (k > 5.5 and l > 6):                    #x-Achse und y-Achse links unten
                        draw_square_centered(1.8+k, 1.2+l, 0.15, color='black')
                    if (k > 6 and l > 5.5) or (k < 6.5 and l < 6):                    #x-Achse und y-Achse rechts oben
                        draw_square_centered(1.2 + k, 1.8 + l, 0.15, color='black')
                    if (k > 6 and l < 6.5) or (k < 6.5 and l > 6):                    # x-Achse und y-Achse links oben
                        draw_square_centered(1.2 + k, 1.2 + l, 0.15, color='black')
                    if (k > 5.5 and l < 6) or (k < 6 and l > 5.5):                    # x-Achse und y-Achse rechts unten
                        draw_square_centered(1.8 + k, 1.8 + l, 0.15, color='black')

                else:                                                                 # weiß
                    if (k < 6 and l < 6) or (k > 6 and l > 6):                        # 2. und 4. Quadrant
                        draw_square_centered(1.2 + k, 1.8 + l, 0.15, color='white')
                        draw_square_centered(1.8 + k, 1.2 + l, 0.15, color='white')
                    if (k < 6 and l > 6) or (k > 6 and l < 6):                        # 1. und 3. Quadrant
                        draw_square_centered(1.2 + k, 1.2 + l, 0.15, color='white')
                        draw_square_centered(1.8 + k, 1.8 + l, 0.15, color='white')
                    if (k < 6 and l < 6.5) or (k > 5.5 and l > 6):                    # x-Achse und y-Achse links unten
                        draw_square_centered(1.8 + k, 1.2 + l, 0.15, color='white')
                    if (k > 6 and l > 5.5) or (k < 6.5 and l < 6):                    # x-Achse und y-Achse rechts oben
                        draw_square_centered(1.2 + k, 1.8 + l, 0.15, color='white')
                    if (k > 6 and l < 6.5) or (k < 6.5 and l > 6):                    # x-Achse und y-Achse links oben
                        draw_square_centered(1.2 + k, 1.2 + l, 0.15, color='white')
                    if (k > 5.5 and l < 6) or (k < 6 and l > 5.5):                    # x-Achse und y-Achse rechts unten
                        draw_square_centered(1.8 + k, 1.8 + l, 0.15, color='white')
        plt.show()                                                                    #show plot
    zusatz()