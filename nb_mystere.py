import random

print("Bienvenue dans le jeu du nombre mystère !")

oui = "oui"
non = "non"
rejouer = oui

while rejouer == oui:
    nbTentatives = 0
    nbMystere = random.randint(1, 50)
    print("Tu dois deviner le nombre mystère entre 1 et 50.")
    nombre = int(input("Quel est le nombre mystère ? "))
    while nombre != nbMystere:
        nbTentatives += 1
        if nombre < nbMystere:
            print("C'est plus !")
            nombre = int(input("Quel est le nombre mystère ? "))
        else:
            print("C'est moins !")
            nombre = int(input("Quel est le nombre mystère ? "))
        if nombre == nbMystere:
            print(
                f"Bravo ! Tu as trouvé le nombre mystère {nbMystere} "
                f"en {nbTentatives} tentatives."
            )
    rejouer = input(f"Voulez vous rejouer ? ({oui}/{non})")

if rejouer == non:
    print("Merci d'avoir joué !")
    exit()
