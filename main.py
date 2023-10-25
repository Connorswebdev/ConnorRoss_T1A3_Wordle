import random
from nltk.corpus import words
import string
from colorama import init, Fore
            
    
# Initialize colorama
init(autoreset=True)
def load_words_from_file(filename):
    with open(filename, 'r') as f:
        word_content = f.read().split("\n")
        words = {word.strip().lower() for word in word_content}
    return words

valid_words = load_words_from_file("word_list.txt")
print(f"Loaded {len(valid_words)} valid words.")


def get_feedback(secret_word, guess):
    feedback = []

    for i, g in enumerate(guess):
        if g == secret_word[i]:
            feedback.append('G')
        elif g in secret_word:
            feedback.append('Y')
        else: feedback.append('R')
                    
    return feedback

def choose_game_difficulty():
    while True:
        choice = input("Would you like to play (regular) or (hard) mode?").lower()
        if choice in ["regular", "hard"]:
            return choice
        print("Invalid choice. Select either 'regular' or 'hard'.")
            
def word_list_based_on_mode(mode):
    if mode == 'regular':
        return [word.lower() for word in valid_words if len(word) == 5]
    elif mode == 'hard':
        return [word.lower() for word in valid_words if len(word) == 7]

def play_wordle():
    #defining the wordle mode and picking a random word from the list matching the criteria
    mode = choose_game_difficulty()
    word_list = word_list_based_on_mode(mode)
    print(len(word_list))
    
    secret_word = random.choice(word_list)
    
    attempts = 6 if mode == 'regular' else 5
    while attempts > 0:
        guess = input(f"Attempt {7 if mode == 'regular' else 6 - attempts}: Guess a {len(secret_word)}-letter word: ").lower()
        
        if len(guess) != len(secret_word) or ' ' in guess:
            print(f"Please enter a {len(secret_word)}-letter word.")
            continue
        elif guess not in valid_words:
            print("Please enter a real word.")
            continue

        feedback = get_feedback(secret_word, guess)
        
        colored_output = ""
        for i, (f, g) in enumerate(zip(feedback, guess)):
            if f == 'G':
                colored_output += Fore.GREEN + g + " "
            elif f == 'Y':
                colored_output += Fore.YELLOW + g + " "
            else:
                colored_output += Fore.RED + g + " "
                
        print(colored_output)

        if feedback == ['G'] * 5:
            print(Fore.GREEN + f"Congratulations! You've guessed the word: {secret_word}")
            break

        attempts -= 1

    if attempts == 0:
        print(Fore.RED + f"You've run out of attempts. The secret word was: {secret_word}")
play_wordle()