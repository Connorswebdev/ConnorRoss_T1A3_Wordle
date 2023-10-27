#!/bin/bash

if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. This is a requirement for the application. For a guide to install Python 3 please visit the following link https://realpython.com/installing-python/"
    exit 1
fi

if ! command -v pip3 &> /dev/null; then
    echo "Pip 3 is not installed. This is a requirement for the application, I will install it for you. For a guide to install Pip 3 manually, please see the README file. Alternatively, visit this link https://pypi.org/project/pip/"
exit 1
fi

python3 -m pip install --upgrade pip

python3 -m pip install -r requirements.txt

source .venv/bin/activate

python3 main.py

# Detecting OS for auto running
OS="$(uname)"

Case $OS in
    "Linux")
        if command -v gnome-terminal &> /dev/null; then
            gnome-terminal -- python3 ./main.py
        elif command -v xterm &> /dev/null; then
            xterm -e python3 ./main.py
        else 
            echo "Unknown terminal. Please run the game manually by typing 'Python3 main.py' in the terminal.'"
        fi
        ;;

    "Darwin")
    osascript -e 'tell app "Terminal" to do script "python3 ./main.py"'
    ;;