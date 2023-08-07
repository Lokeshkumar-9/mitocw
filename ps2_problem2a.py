def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

#example usage
secret_word = 'apple'
letters_guessed = ['e','i','k','p','r','s']
print(is_word_guessed(secret_word, letters_guessed))

