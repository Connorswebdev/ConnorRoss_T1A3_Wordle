# Python Wordle

This application is a reimagined version of the popular game, Wordle, redesigned to be functional in a python terminal with a twist.

## Link to Github ##

[Github] (https://github.com/Connorswebdev/ConnorRoss_T1A3_Wordle)

## Link to Trello ##

[Trello] (https://trello.com/b/fLWKXXeA/wordle-game)

## Code Style Guide ##

[PEP8] (https://peps.python.org/pep-0008/#documentation-strings)

### Hardware Requirements
This program recommends a modern operating system with either:
* Windows 10
* Mac OS Monterey
* Ubuntu 20.04
- This program also recommends at least 2GB RAM and 1 GB of Free Disk Space as recommended by VS Code

#### [VS CODE](https://vscode-docs.readthedocs.io/en/latest/supporting/requirements/#:~:text=VS%20Code%20is%20lightweight%20and,1%20GB%20of%20RAM)

## Installation

* For an easy install. Simply run the following command: 'bash wordle_script.sh' -OR- 'source wordle_script.sh' -OR- '. wordle_script.sh' --- This script will check and install all prerequisites and dependencies to ensure that the system can run the program.

For other installation instructions, they have been listed below.

1. Ensure Python 3 is installed. If it is not installed, please follow this link and find the correct installer for your operating system: https://www.python.org/downloads/
2. Ensure Pip 3 is installed. If it is not installed, please follow this link and find the correct installer for your operating system: https://pypi.org/project/pip/
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Software Requirements

* By running the easy install script, you will be able to determine if your software is up to date and valid.

If you require a manual input you should:
1. Check if python is installed and up to date. Python must be 3.10.0 or greater to run the application. Check this by running:
```python --version```
You should see a message returned that looks like ```Python 3.10.12```

If python is not installed or up to date, please visit the Python [Download Page](https://www.python.org/downloads/) and find the correct installer for your device.

2. The terminal required a minimum width of 100 columns for the best user experience.

## Features

1. Two Modes: Regular or Hard - Regular is standard wordle, 5 letter words and 6 guesses. Hard mode is 7 letter words and only 5 guesses. Inside of the making_words.py file, you will find a script I generated to pull all 5 and 7 letter words from the NLTK word library which is more comprehensive than the Oxford dictionary. The script then writes all the words into the word_list.txt file.
2. Color Coded Output - Just like the wordle game, this application tells the user if their guess is in the correct spot and correct letter(Coloured green) or in the incorrect spot but correct letter(Coloured Yellow) or if the letter is not in the word at all (Coloured Red). This is measured by the application using a for loop and checking each letter and its position against the "secret word".
3. Replayability - A replay function was added so the user can play multiple rounds. This feature is nested within the main game loop. It will appear once the game is over so the user can generate a new word and play it again. If they do not wish to play again, the console will output a "Thanks for playing!" message and the game will end.
4. ASCII Art - Giving the terminal a bit more visual appearance by introducing an ASCII art when the user begins playing the game. This was aimed to be reminiscent of a main menu screen seen in video games. This is only displayed on the inital launch of the application. If the character chooses to replay they will not receive this screen again.

## Installation

* For an easy install. Simply run the following command: 'bash wordle_script.sh' -OR- 'source wordle_script.sh' -OR- '. wordle_script.sh' --- This script will check and install all prerequisites and dependencies to ensure that the system can run the program.

For other installation instructions, they have been listed below.

1. Ensure Python 3 is installed. If it is not installed, please follow this link and find the correct installer for your operating system: https://www.python.org/downloads/
2. Ensure Pip 3 is installed. If it is not installed, please follow this link and find the correct installer for your operating system: https://pypi.org/project/pip/
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## How to Play

1. If you used the easy install the game will automatically begin. 
2. If you used the manual install, run the game from the terminal:
```bash
python3 main.py
```
3. Choose a difficulty from regular or hard. Regular is the standard wordle we know and love with 5 letter words and 6 guesses. Hard mode is slightly more difficult with 7 letter words and only 5 guesses.
4. Guess the word according to the colour coordination of the terminal. If the letter is green it is in the correct spot and correct letter. If the colour is yellow it is in the incorrect spot but it is the correct letter. If the colour is red it is not in the word at all.
5. If you win or lose, you can decide to replay the game which will bring you back to step 3. If you wish to quit, simply type 'no' on the replay screen.

## Requirements

* Note that these are installed once the ```wordle_script.sh``` script is activated or the ```pip install -r requirements.txt``` is activated.

```
NLTK Library == 3.8.1
PyEnchant == 3.2.2
Colorama == 0.4.6
```