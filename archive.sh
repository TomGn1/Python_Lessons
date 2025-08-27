#!/bin/bash

archives=/home/user/dossier_copies/
destination=/home/user/dossier_archives/
date=$(date +"%H:%M:%S")

if [ ! -d "$destination" ]; then
    mkdir $destination
fi

for fichiers in $archives*; do
    name=$(basename $fichiers)
    tar -cvf $fichiers.tar.gz $archives && mv $fichiers.tar.gz $destination$name-$date.tar.gz
done
