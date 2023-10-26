import random
from nltk.corpus import words
import math
from colorama import init, Fore
            
    
# Initialize colorama
init(autoreset=True)
def load_words_from_file(filename):
    with open(filename, 'r') as f:
        word_content = f.read().split("\n")
        words = {word.strip().lower() for word in word_content}
    return words

valid_words = load_words_from_file("word_list.txt")

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
    while True:
    #defining the wordle mode and picking a random word from the list matching the criteria

        mode = choose_game_difficulty()
        word_list = word_list_based_on_mode(mode)
        secret_word = random.choice(word_list)
        max_attempts = 6 if mode == 'regular' else 5
        attempts_left = max_attempts

        while attempts_left > 0:
            attempt_number = max_attempts - attempts_left + 1
            guess = input(f"Attempt {attempt_number}: Guess a {len(secret_word)}-letter word: ").lower()
        
            if len(guess) != len(secret_word) or ' ' in guess:
                print(f"Please enter a {len(secret_word)}-letter word.")
                continue
            
            elif guess not in valid_words:
                print("Please enter a real word.")
                continue

            attempts_left -= 1
            
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

            if attempts_left == 0:
                print(Fore.RED + f"You've run out of attempts. The secret word was: {secret_word}")

                play_again = input("Do you wish to play again? (yes/no): ").lower()
                if play_again != "yes":
                    print("Thanks for playing!")
                break
play_wordle()
