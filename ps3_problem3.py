def is_valid_word(word, hand, word_list):
    word = word.lower()
    if word not in word_list:
        return False
    word_letter_count = {}
    for letter in word:
        word_letter_count[letter] = word_letter_count.get(letter, 0) + 1
        
    for letter, count in word_letter_count.items():
            if count > hand.get(letter, 0):
                return False
    return True

word = "quail"
hand ={'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
word_list = ["apple", "pear", "banana", "orange", "abater"]
print(is_valid_word(word, hand, word_list))

