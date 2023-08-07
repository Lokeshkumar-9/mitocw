def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ''
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word +=  letter + ''
        else:
            guessed_word += '_'
    return guessed_word

#example usage

secret_word = 'apple'
letters_guessed = ['e','i','k','p','r','s']
print(get_guessed_word(secret_word, letters_guessed))
