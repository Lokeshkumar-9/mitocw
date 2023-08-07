import random

#load words
def load_words(filename):
    with open(filename, 'r') as file:
        words = file.read().splitlines()
    return [word.lower() for word in words]

#choose random word
def choose_word(word_list):
    return random.choice(word_list)

#initialize game parameters
def initialize_game():
    secret_word = choose_word(load_words('words.txt'))
    guessed_letters = []
    guesses_left = 6
    return secret_word, guessed_letters, guesses_left

#game Loop
def play_hangman():
    secret_word, guessed_letters , guesses_left = initialize_game()
    while guesses_left > 0:
        display_word(secret_word, guessed_letters)
        print(f"Guesses_left: {guesses_left}")
        guess = input("Guess a letter: ").lower()
        if guess in secret_word:
            guessed_letters.append(guess)
        else:
            guesses_left -= 1
        if all(letter in guessed_letters for letter in secret_word):
            display_word(secret_word, guessed_letters)
            print("Congratulations, you've won!")
            break

    if guesses_left == 0:
        print(f"Sorry, you've run out of guesses. The word was '{secret_word}'.")

def display_word(secret_word, guessed_letters):
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    print(display)

#play again
def play_again():
    return input("Do you want to play again? (yes/no): ").lower() == "yes"

#game loop
while True:
    play_hangman()
    if not play_again():
        print("Thanks for playing!")
        break
