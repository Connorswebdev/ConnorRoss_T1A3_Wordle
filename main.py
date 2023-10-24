import random
from nltk.corpus import words
import string
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)
def load_words_from_file(filename):
    with open(filename, 'r') as f:
# Reading the file, splitting by commas or newlines, and convertting into a set
        words = set(word.strip() for word in f.read().split(","))
    return words

valid_words = load_words_from_file('word_list.txt')

def get_feedback(secret_word, guess):
    feedback = ['R'] * len(secret_word)
    unused_indices = list(range(len(secret_word)))

    # Check for green feedback (correct letter, correct position)
    for i, (s, g) in enumerate(zip(secret_word, guess)):
        if s == g:
            feedback[i] = 'G'
            unused_indices.remove(i)

    # Check for yellow feedback (correct letter, wrong position)
    for i, g in enumerate(guess):
        if feedback[i] == 'R' and g in secret_word:
            for ui in unused_indices:
                if secret_word[ui] == g:
                    feedback[i] = 'Y'
                    unused_indices.remove(ui)
                    break
                    
    return feedback

def play_wordle():
    # Get a list of 5-letter words
    five_letter_words = [word for word in words.words() if len(word) == 5 and word[0] not in string.ascii_uppercase]
    secret_word = random.choice(five_letter_words)
    
    attempts = 6
    while attempts > 0:
        guess = input(f"Attempt {7 - attempts}: Guess a 5-letter word: ").lower()
        
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
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