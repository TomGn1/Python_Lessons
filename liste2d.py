import os

chaine = str(" " * 20)
terrain_de_jeu = [chaine] * 10

terrain_de_jeu[0] = chaine[:1] + "╔" + chaine[2:19] + "╗"
for i in range(1, 10):
    terrain_de_jeu[i] = chaine[:1] + "║" + chaine[2:19] + "║"
terrain_de_jeu[9] = chaine[:1] + "╚" + chaine[2:19] + "╝"
for i in range(2, 19):
    terrain_de_jeu[0] = terrain_de_jeu[0][:i] + "═" + terrain_de_jeu[0][i+1:]
    terrain_de_jeu[9] = terrain_de_jeu[9][:i] + "═" + terrain_de_jeu[9][i+1:]
pos_x = 4
pos_y = 5
for ligne in terrain(pos_x, pos_y):
    print(ligne)
terrain_de_jeu[pos_y] = chaine[:1] + "║" + chaine[:pos_x] + "☺" + chaine[2:14] + "║" +\
    chaine[pos_x+1:]

direction = input("Dans quelle direction veux-tu aller ? (z/q/s/d) ")

while direction == "z" or direction == "q" or direction == "s" or direction == "d":
    terrain_de_jeu[pos_y] = chaine[:pos_x] + " " + chaine[pos_x+1:]
    if direction == "z":
        if pos_y == 0:
            print("Tu ne peux pas aller plus haut !")
            direction = input(
                "Dans quelle direction veux-tu aller ? (z/q/s/d) ")
            os.system("cls")
            for ligne in terrain_de_jeu:
                print(ligne)
            continue
        else:
            pos_y -= 1
            ligne = chaine[:pos_x] + "☺" + chaine[pos_x+1:]
            terrain_de_jeu[pos_y] = ligne

    if direction == "s":
        if pos_y == 9:
            print("Tu ne peux pas aller plus bas !")
            direction = input(
                "Dans quelle direction veux-tu aller ? (z/q/s/d) ")
            os.system("cls")
            for ligne in terrain_de_jeu:
                print(ligne)
            continue
        else:
            pos_y += 1
            ligne = chaine[:pos_x] + "☺" + chaine[pos_x+1:]
            terrain_de_jeu[pos_y] = ligne

    if direction == "q":
        if pos_x == 0:
            print("Tu ne peux pas aller plus à gauche !")
            direction = input(
                "Dans quelle direction veux-tu aller ? (z/q/s/d) ")
            os.system("cls")
            for ligne in terrain_de_jeu:
                print(ligne)
            continue
        else:
            pos_x -= 1
            ligne = chaine[:pos_x] + "☺" + chaine[pos_x+1:]
            terrain_de_jeu[pos_y] = ligne

    if direction == "d":
        if pos_x == 19:
            print("Tu ne peux pas aller plus à droite !")
            direction = input(
                "Dans quelle direction veux-tu aller ? (z/q/s/d) ")
            os.system("cls")
            for ligne in terrain_de_jeu:
                print(ligne)
            continue
        else:
            pos_x += 1
            ligne = chaine[:pos_x] + "☺" + chaine[pos_x+1:]
            terrain_de_jeu[pos_y] = ligne

    direction = input("Dans quelle direction veux-tu aller ? (z/q/s/d) ")
    os.system("cls")
    for ligne in terrain_de_jeu:
        print(ligne)
    continue

if direction != "z" and direction != "q" and direction != "s" and direction != "d":
    print("Direction invalide !")
    exit()
