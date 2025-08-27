#!/bin/bash

nombre_mystere=$((1 + RANDOM % 100))
tentative=0
oui="o"
non="n"
rejouer="o"
while [ $rejouer == $oui ]; do
    nombre_mystere=$((1 + RANDOM % 100))
    tentative=0
    echo "Je pense à un nombre entre 1 et 100. Devine lequel !"
 
    read -p "Entre un nombre entre 1 et 100 ! " nombre_utilisateur

    while [ $nombre_utilisateur -ne $nombre_mystere ]; do
        tentative=$((tentative + 1))
        if [ $nombre_utilisateur -lt $nombre_mystere ]; then
            echo "c'est plus !"
        elif [ $nombre_utilisateur -gt $nombre_mystere ]; then
            echo "c'est moins !"
        fi
        read -p "Entre un nombre entre 1 et 100 ! " nombre_utilisateur
    done
    echo "Bravo ! Tu as trouvé le nombre mystère $nombre_mystere en $tentative tentatives !"
    read -p "Veux-tu rejouer ? (o/n) " rejouer
done