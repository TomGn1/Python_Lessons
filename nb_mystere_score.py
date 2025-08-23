import random


print("Bienvenue dans le jeu du nombre mystère !")

ancien_joueur = "personne"
dernier_score = None
meilleur_score = 0
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

            if meilleur_score == 0 or nbTentatives < meilleur_score:
                meilleur_score = nbTentatives
                meilleur_joueur = input("Quel est ton nom ? ")
                print(f"Félicitations {meilleur_joueur} ! "
                      f"Tu as le nouveau meilleur score avec {meilleur_score} tentatives.")
                if meilleur_joueur != ancien_joueur and dernier_score is not None:
                    print(f"Le meilleur score à battre était de {dernier_score} "
                          f"tentatives par {ancien_joueur}.")
                ancien_joueur = meilleur_joueur
                dernier_score = nbTentatives
            else:
                print(f"Le meilleur score actuel est de {meilleur_score} ")

    rejouer = input(f"Voulez vous rejouer ? ({oui}/{non})")


if rejouer == non:
    print("Merci d'avoir joué !")
    exit()
