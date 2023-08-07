def display_hand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end = ' ')
print()


def update_hand(hand, word):
    new_hand = hand.copy()
    keys_to_delete = []
    for letter in new_hand:
        new_hand[letter] -= 1
        if new_hand[letter] == 0:
            keys_to_delete.append(letter)
    for keys in keys_to_delete:
        del new_hand[keys]
    return new_hand

hand ={'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
print("Original hand:")
display_hand(hand)

word = "quail"
new_hand = update_hand(hand, word)
print("\nUpdate hand after playing '{}':".format(word))
display_hand(new_hand)

print("\nOriginal hand after playing '{}':".format(word))
display_hand(hand)
