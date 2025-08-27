#!/bin/bash

original=/home/user/dossier_original/*
copies=/home/user/dossier_copies/

if [ ! -d "$copies" ]; then
    mkdir $copies
fi

cp $original $copies