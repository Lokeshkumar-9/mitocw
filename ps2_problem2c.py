import string
def get_available_letters(letters_guessed):
    available_letters = ''
    all_letters = string.ascii_lowercase
    for letter in all_letters:
        if letter not in letters_guessed:
            available_letters += letter
    return available_letters

#example usage
letters_guessed =['e','i','k','p','r','s']
print(get_available_letters(letters_guessed))
