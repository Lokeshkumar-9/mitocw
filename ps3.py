# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """

#define scrabble_letter_values and get_word_score function

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def get_word_score(word, n):
     word = word.lower()
     first_component = sum(SCRABBLE_LETTER_VALUES[letter] for letter in word)    #first component is the sum of the points for letters in the word
     word_length = len(word)     #word length is the number of letters is used in the word
     second_component = max (7 * word_length - 3 * (n - word_length), 1)
     score = first_component * second_component      #the score for a word is product of two components
     return score

#testing

test_word = "abater"
total_letters = 7
score = get_word_score(test_word, total_letters)
print(f"The score for the  '{test_word}' is: {score}")


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
def get_frequency_dict(word):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for letter in word:
        freq[letter] = freq.get(letter,0) + 1
    return freq

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line
    
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

def update_hand(hand, word):
    new_hand = hand.copy()
    for letter in word.lower():
        if new_hand.get(letter, 0) > 0:
            new_hand[letter] -= 1
    return new_hand

# Example usage
hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
display_hand(hand)
new_hand = update_hand(hand, 'quail')
print(new_hand)
display_hand(new_hand)
display_hand(hand)

hand = {'j':2, 'o':1, 'l':1, 'w':1, 'n':2}
display_hand(hand)
hand = update_hand(hand, 'jolly')
print(hand)
display_hand(hand)

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
def get_frequency_dict(word):
    """
    Returns a dictionary where the keys are elements of the word and
    the values are the number of times that element occurs.
    word: string
    returns: dictionary
    """
    freq = {'h':1, 'e':1, 'l':2, 'o':1}
    for letter in word:
        freq[letter] = freq.get(letter,0) + 1
    return freq    

word_list = load_words()    
def is_valid_word(word, hand, word_list):
    if word not in word_list:
        return False
    else:
        letter_counts = {} 
    
        for letter in word:
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
        
            if letter not in hand:
                return False
            elif letter_counts[letter] > hand.get(letter, 0):
                return False
        
        return True
    
word = "hello"
handorig = get_frequency_dict(word)
handcopy = handorig.copy()
print(is_valid_word(word, handcopy, word_list))

hand = {'h':1, 'e':1, 'l':2, 'o':1}
word = "hello"
print(is_valid_word(word, hand, word_list))

hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
word = "Rapture"
print(is_valid_word(word, hand, word_list))

hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
word = "EVIL"
print(is_valid_word(word, hand, word_list))

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    return sum(hand.values())

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter, count in hand.items():
        for _ in range(count):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

def is_valid_word(word, hand, word_list):
    if word not in word_list:
        return False
    else:
        letter_counts = {} 
    
        for letter in word:
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
        
            if letter not in hand:
                return False
            elif letter_counts[letter] > hand.get(letter, 0):
                return False
        
        return True  

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
   
def get_word_score(word, n):
     word = word.lower()
     first_component = sum(SCRABBLE_LETTER_VALUES[letter] for letter in word)    #first component is the sum of the points for letters in the word
     word_length = len(word)     #word length is the number of letters is used in the word
     second_component = max (7 * word_length - 3 * (n - word_length), 1)
     score = first_component * second_component      #the score for a word is product of two components
     return score

def update_hand(hand, word):
    new_hand = hand.copy()
    for letter in word.lower():
        if new_hand.get(letter, 0) > 0:
            new_hand[letter] -= 1
    return new_hand
   
def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    total_score = 0         # Keep track of the total score
    
    while True:             # As long as there are still letters left in the hand:
        
        print("Current_hand:", end = " ")       # Display the hand
        display_hand(hand)
        
        user_input = input("Enter the word, or '!!'' to indicate that you are finished: ")       # Ask user for input
        
        if user_input == '!!':       # If the input is two exclamation points:
            
            break                   # End the game (break out of the loop)

        if is_valid_word(user_input, hand, word_list):    # If the word is valid:
            word_score = get_word_score(user_input, calculate_handlen(hand))    # Tell the user how many points the word earned,
            total_score += word_score   # and the updated total score
            print(f'"{user_input}" earned (word_score) points. Total: {total_score} points')
            hand = update_hand(hand, user_input)        # update the user's hand by removing the letters of their inputted word
        else:       # Otherwise (the word is not valid):
            print("That the word is not valid. Please choose another word.")    # Reject invalid word (print a message)
            
        if calculate_handlen(hand) == 0:
            print("Ran out of letters. total score:", total_score, "points")        #print a message that you have ran out of letters
            break       #break out of the loop


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    
    pass  # TO DO... Remove this line when you implement this function
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    print("play_game not implemented.") # TO DO... Remove this line when you implement this function
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """

#define scrabble_letter_values and get_word_score function

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def get_word_score(word, n):
     word = word.lower()
     first_component = sum(SCRABBLE_LETTER_VALUES[letter] for letter in word)    #first component is the sum of the points for letters in the word
     word_length = len(word)     #word length is the number of letters is used in the word
     second_component = max (7 * word_length - 3 * (n - word_length), 1)
     score = first_component * second_component      #the score for a word is product of two components
     return score

#testing

test_word = "abater"
total_letters = 7
score = get_word_score(test_word, total_letters)
print(f"The score for the  '{test_word}' is: {score}")


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
def get_frequency_dict(word):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for letter in word:
        freq[letter] = freq.get(letter,0) + 1
    return freq

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line
    
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

def update_hand(hand, word):
    new_hand = hand.copy()
    for letter in word.lower():
        if new_hand.get(letter, 0) > 0:
            new_hand[letter] -= 1
    return new_hand

# Example usage
hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
display_hand(hand)
new_hand = update_hand(hand, 'quail')
print(new_hand)
display_hand(new_hand)
display_hand(hand)

hand = {'j':2, 'o':1, 'l':1, 'w':1, 'n':2}
display_hand(hand)
hand = update_hand(hand, 'jolly')
print(hand)
display_hand(hand)

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
def get_frequency_dict(word):
    """
    Returns a dictionary where the keys are elements of the word and
    the values are the number of times that element occurs.
    word: string
    returns: dictionary
    """
    freq = {'h':1, 'e':1, 'l':2, 'o':1}
    for letter in word:
        freq[letter] = freq.get(letter,0) + 1
    return freq    

word_list = load_words()    
def is_valid_word(word, hand, word_list):
    if word not in word_list:
        return False
    else:
        letter_counts = {} 
    
        for letter in word:
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
        
            if letter not in hand:
                return False
            elif letter_counts[letter] > hand.get(letter, 0):
                return False
        
        return True
    
word = "hello"
handorig = get_frequency_dict(word)
handcopy = handorig.copy()
print(is_valid_word(word, handcopy, word_list))

hand = {'h':1, 'e':1, 'l':2, 'o':1}
word = "hello"
print(is_valid_word(word, hand, word_list))

hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
word = "Rapture"
print(is_valid_word(word, hand, word_list))

hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
word = "EVIL"
print(is_valid_word(word, hand, word_list))

#
# Problem #5: Playing a hand
#

def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    return sum(hand.values())

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter, count in hand.items():
        for _ in range(count):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line
    
def is_valid_word(word, hand, word_list):
    if word not in word_list:
        return False
    else:
        letter_counts = {} 
    
        for letter in word:
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
        
            if letter not in hand:
                return False
            elif letter_counts[letter] > hand.get(letter, 0):
                return False
        
        return True  

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
   
def get_word_score(word, n):
    word = word.lower()
    first_component = 0
    
    for letter in word:
        if letter in SCRABBLE_LETTER_VALUES:
            first_component += SCRABBLE_LETTER_VALUES[letter]
               
    wildcard_count = word.count('*')
    if wildcard_count > 0:
        first_component += wildcard_count * 0
    second_component = 7 * len(word) - 3 * (n - len(word))
    return first_component * max(1, second_component)

def update_hand(hand, word):
    new_hand = hand.copy()
    for letter in word.lower():
        if new_hand.get(letter, 0) > 0:
            new_hand[letter] -= 1
    return new_hand
   
def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    total_score = 0         # Keep track of the total score
    
    while calculate_handlen(hand) > 0:             # As long as there are still letters left in the hand:
        
        print("Current_hand:", end = " ")       # Display the hand
        display_hand(hand)
        
        user_input = input("Enter the word, or '!!'' to indicate that you are finished: ")       # Ask user for input
        
        if user_input == '!!':       # If the input is two exclamation points:
            
            break                   # End the game (break out of the loop)

        if is_valid_word(user_input, hand, word_list):    # If the word is valid:
            word_score = get_word_score(user_input, calculate_handlen(hand))    # Tell the user how many points the word earned,
            total_score += word_score   # and the updated total score
            print(f'"{user_input}" earned (word_score) points. Total: {total_score} points')
        else:       # Otherwise (the word is not valid):
            print("That the word is not valid. Please choose another word.")    # Reject invalid word (print a message)
            
        hand = update_hand(hand, user_input)        # update the user's hand by removing the letters of their inputted word
        
        print("Total score:", total_score)          #prtints total score points
    
        if calculate_handlen(hand) == 0:
            print("Ran out of letters. total score:", total_score, "points")        #print a message that you have ran out of letters
            break       #break out of the loop
        
#example usage1

hand = {'a':1, 'j':1, 'e':1, 'f':1, '*':1, 'r':1, 'x':1}
word_list = ['jar', 'f*x', 'fix', '*t']
play_hand(hand, word_list)

#example usage2

hand = {'a':1, 'c':1, 'f':1, 'i':1, '*':1, 't':1, 'x':1}
play_hand(hand, word_list)


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    print("Current_hand:", display_hand(hand))
    letter = input("Would you like to substitute a letter? ")
    
    if letter.lower() == 'yes':
        letter = input("Which letter would you like to replace: ")
        if substitute_letter(hand,letter):
            print("Current hand:", display_hand(hand))
    return hand

def substitute_letter(hand, letter):
    if letter in hand:
        new_letter = random.choice(VOWELS if letter in VOWELS else CONSONANTS)
        hand[new_letter] = hand.pop(letter)
        return True
    return False
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    total_score = 0
    num_hands = int(input("Enter total number of hands: "))
    
    for _ in range(num_hands):
        hand = deal_hand(HAND_SIZE)
        if hand is None:
            break
        
        print("Current_hand:", display_hand(hand))
        total_score += play_hand(hand, word_list)
        replay = input("Would you like to replay the hand? ")
        if replay.lower() == 'no':
            break
                
    print("Total score over all hands:", total_score)
    
def deal_hand(n):
    pass

def display_hand(hand):
    return ' '.join([f"{k}:{v}" for k,v in hand.items()])

def play_hand(hand, word_list):
    total_score = 0
    while True:
        print("Current_hand:", display_hand(hand))
        word = input("Enter the word, or '!!'' to indicate that you are finished: ")
        
        if word == '!!':
            print("Current_hand:", display_hand(hand))
            print("Total score:", total_score)
            break
        
        if is_valid_word(word, hand, word_list):
            word_score = get_word_score(word, HAND_SIZE)
            total_score += word_score
            print(f'"{word}" earned (word_score) points. Total: {total_score} points')
            for letter in word:
                hand[letter] -= 1
            else:
                print("That word is not valid. Please choose another word.")
    
    return total_score

def is_valid_word(word, hand, word_list):
    pass

def get_word_score(word, n):
    pass

def load_words():
    pass

#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
