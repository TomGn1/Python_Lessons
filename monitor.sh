#!/bin/bash

journalacces=/var/log/apache2/access.log
lastblog=~/lastblog.txt

read -p $'[1] Afficher les adresse IP les plus fréquentes sur apache2\n[2] Afficher les tentatives de connexions sur le système.\n' reponse

if [ "$reponse" = "1" ]; then
    for ipadresse in $journalacces; do
        #sudo head -10 $ipadresse | grep -E -o "^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)" # Pour les 10 dernères IP connectées.
        sudo awk '{a[$1]++} END {for (i in a) print a[i],i}' $journalacces | sort -rnk1 | head -10
    done

elif [ "$reponse" = "2" ]; then
    sudo lastb | head -n -2 > ~/lastblog.txt
    sudo awk '{a[$1]++} END {for (i in a) print a[i],i}' "$lastblog" | sort -rnk1 | head -10
fi