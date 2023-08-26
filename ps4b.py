# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words("words.txt")
               
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text
    
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy[:]
    
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        shift_dict = {}
        
        for i in range(26):
            shift_dict[lowercase[i]] = lowercase[(i + shift) % 26]
            shift_dict[uppercase[i]] = uppercase[(i + shift) % 26]
            
        return shift_dict
            
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shift_dict = self.build_shift_dict(shift)
        shifted_message = ""
        
        for char in self.message_text:
            if char in shift_dict:
                shifted_message += shift_dict[char]
            else:
                shifted_message += char
                
        return shifted_message
                   
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
            
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift
        
    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()
    
    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.get_message_text_encrypted
        
    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        best_shift = 0
        best_count = 0
        best_message = ""
        
        for shift in range(26):
            decrypted_message = self.apply_shift(26 - shift)
            words = decrypted_message.split()
            count_valid_words = sum(1 for word in words if is_word(self.valid_words, word))
            
            if count_valid_words > best_count:
                best_count = count_valid_words
                best_shift = shift
                best_message = decrypted_message
                
        return best_shift, best_message
            
       
if __name__ == '__main__':
    
    #Example Test Cases for PlaintextMesaage
    #Example1
    test_text1 = "Hello, World"
    test_shift1 = 2
    plainttext1 = PlaintextMessage(test_text1, test_shift1)
    expected_otuput1 = "Jgnnq"
    actual_output1 = plainttext1.get_message_text_encrypted()
    print("Plaintext 1 Expected:", expected_otuput1)
    print("Plaintext 1 Actual:", actual_output1)
    
    test_text2 = "This is Lokesh Kumar."
    test_shift2 = 10
    plainttext2 = PlaintextMessage(test_text2, test_shift2)
    expected_output2 = "Drasi otaadf Fhisdngl Dfsadnj"
    actual_output2 = plainttext2.get_message_text_encrypted()
    print("Plaintext 2 Epected:", expected_output2)
    print("Plaintext 2 Actual:", actual_output2)
    
    #Example Test Cases for CiphertextMessage
    #Example3
    test_text3 = "Jgnnq"
    ciphertext3 = CiphertextMessage(test_text3)
    expected_shift3 = 2
    expected_output3 = "Hello, World"
    actual_shift3, actual_output3 = ciphertext3.decrypt_message()
    print("Ciphertext 3 Shift Expected:", expected_shift3)
    print("Ciphertext 3 Shift Actual:", actual_shift3)
    print("Ciphertext 3 Decrypted expected:", expected_output3)
    print("Cipherttext 3 Decrypted Actual:", actual_output3)
    
    test_text4 = "Drasi otaadf Fhisdngl Dfsadnj"
    ciphertext4 = CiphertextMessage(test_text4)
    expected_shift4 = 10
    expected_output4 = "This is Lokesh Kumar."
    actual_shift4, actual_output4 = ciphertext4.decrypt_message()
    print("Ciphertext 4 Shift Expected:", expected_shift4)
    print("Ciphertext 4 Shift Actual:", actual_shift4)
    print("Ciphertext 4 Decrypted expected:", expected_output4)
    print("Ciphertext 4 Decrypted Actual:", actual_output4)
    
    story_string = get_story_string()
    encrypted_story = CiphertextMessage(story_string)
    shift_value, decrypted_story = encrypted_story.decrypt_message()
    print("Shift value for story:", shift_value)
    print("Decrypted story:\n", decrypted_story) 
