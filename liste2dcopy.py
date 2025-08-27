import os


def terrain(pos_x, pos_y):
    terrain_de_jeu = terrain_base[:]
    ligne = terrain_de_jeu[pos_y]
    terrain_de_jeu[pos_y] = ligne[:pos_x] + "☺" + ligne[pos_x+1:]
    return terrain_de_jeu


terrain_base = []
terrain_base.append("╔" + "═" * 18 + "╗")
for i in range(1, 9):
    terrain_base.append("║" + " " * 18 + "║")
terrain_base.append("╚" + "═" * 18 + "╝")

pos_x, pos_y = 5, 5
for ligne in terrain(pos_x, pos_y):
    print(ligne)

direction = input("Dans quelle direction veux-tu aller ? (z/q/s/d) ")

while True:
    os.system("cls")
    for ligne in terrain(pos_x, pos_y):
        print(ligne)

    direction = input("Dans quelle direction veux-tu aller ? (z/q/s/d) : ")

    if direction == "z" and pos_y > 1:
        pos_y -= 1
    elif direction == "s" and pos_y < 8:
        pos_y += 1
    elif direction == "q" and pos_x > 1:
        pos_x -= 1
    elif direction == "d" and pos_x < 18:
        pos_x += 1
    elif direction == "exit":
        print("Jeu terminé.")
        break
