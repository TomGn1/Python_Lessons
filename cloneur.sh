#!/bin/bash

if [ $# -lt 2 ]; then
    echo "Merci de fournir 2 arguments à ce script."
    echo "Utilisation : ./cloneur.sh /chemin/vers/dossier_original /chemin/vers/dossier_copie"
    exit 1
fi

original=$1
copies=$2

if [ ! -d $original ]; then
    echo "Erreur, $original n'est pas un dossier valide."
    exit 2
fi

if [ ! -d "$copies" ]; then
    mkdir $copies
    cp -rv $original/* $copies
else
    cp -rv $original/* $copies
fi

