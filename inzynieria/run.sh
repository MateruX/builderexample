#!/bin/bash

# Sprawdź czy python jest zainstalowany
if ! command -v python3 &> /dev/null
then
    echo "Python could not be found, installing Python..."
    brew install python
fi

# Instalacja potrzebnych bibliotek, np. numpy (zakładając, że potrzebujesz numpy)
pip3 install numpy

# Uruchomienie skryptu Pythona
python3 programik.py
