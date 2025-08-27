#!/bin/bash

liste_utilisateurs=~/Documents/user.csv

read -p $'[1] Voulez vous importer un ou plusieurs utilisateurs depuis un fichier ?\n[2] Voulez vous ajouter un seul utilisateur ?\n' reponse

if [ "$reponse" = "2" ]; then
    echo "Ajouter un nouvel utilisateur."
    read -p "Nom d'utilisateur : " utilisateur

    echo "$utilisateur" 
    sudo useradd -m "$utilisateur"

    password=$(</dev/urandom tr -dc '12345!@#$%^&*()_A-Z-a-z-0-9'| fold -w10 | head -1)

    echo "$password"
    echo "$utilisateur:$password" | sudo chpasswd


elif [ "$reponse" = "1" ]; then
    tail -n +2 "$liste_utilisateurs" | while IFS=, read -r username passwordcsv; do
        sudo useradd -m "$username"
        echo "$username:$passwordcsv" | sudo chpasswd
    done
fi
