#!/bin/bash

if ! [[ -x "$(command -v python3)"]]
then
    echo "ERROR: Python 3 is not installed. This is a requirement for the application. For a guide to install Python 3 , please see the README file. Alternatively, visit this link https://realpython.com/installing-python/ >&2
    exit 1
fi

if ! [[ -x "$(command -v pip3)" ]]
then
    echo "ERROR: Pip 3 is not installed. This is a requirement for the application. For a guide to install Pip 3, please see the README file. Alternatively, visit this link https://pypi.org/project/pip/ >&2
exit 1
fi


pip3 install -r requirements.txt 
python3 main.py