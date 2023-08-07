import string
import random

#load words from a file
def load_words(filename):
    print("Loading word list from file...")
    with open(filename, 'r') as f:
        words = f.read().split()
    print(len(words), "words loaded.")
    return words

#choose a word randomly from the list
def choose_word(wordlist):
    return random.choice(wordlist)

#check if the word has been guessed
def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

#display the guessed word 
def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ''
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += '_ '
    return guessed_word

#get available letters that have not guessed yet
def get_available_letters(letters_guessed):
    available_letters = ''
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available_letters += letter
    return available_letters

def hangman(secret_word):
    warnings_remaining = 3 
    guesses_remaining = 6
    letters_guessed = []

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {warnings_remaining} warnings left.")
    print("-------------")

    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
        print(f"You have {guesses_remaining} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        guess = input("Please guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Oops! That is not a valid letter. You have {warnings_remaining} warnings left:", get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                print("Oops! That is not a valid letter. You have no warnings left, so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
        elif guess in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Oops! You've already guessed that letter. You have {warnings_remaining} warnings left:", get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                print("Oops! You've already guessed that letter. You have no warnings left, so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
        elif guess in secret_word:
            letters_guessed.append(guess)
            print(f"Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed.append(guess)
            print(f"Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))

        print("------------")

    if is_word_guessed(secret_word, letters_guessed):
        score = guesses_remaining * len(set(secret_word))
        print("Congratulations, you won!")
        print(f"Your total score for this game is: {score}")
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word)

if __name__ == "__main__":
    wordlist = load_words("words.txt")
    secret_word = choose_word(wordlist)
    hangman(secret_word)
