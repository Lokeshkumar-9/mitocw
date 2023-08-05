def match_with_gaps(my_word, other_word):
    my_word = my_word.replace(" "," ")
    if len(my_word) != len(my_word):
        return False
    for i in range(len(my_word)):
        if my_word[i] != "_" and my_word[i] != other_word[i]:
            return False

        return True

#example usage
print(match_with_gaps("te_ t", "tact"))
print(match_with_gaps("a_ _", "banana"))
print(match_with_gaps("a_ _le", "apple"))
print(match_with_gaps("a_ple", "apple"))

