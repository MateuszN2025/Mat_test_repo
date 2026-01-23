a = 'doggy'

def reverse_string(word: str):
    length = len(word)
    # print(length)
    # print(length-1)
    new_word = []
    for letter in word:
        # print(letter)
        new_word.insert(length,letter)
        length -= length

    old_reversed_word = ''
    for letter2 in new_word:
        old_reversed_word += letter2

    return old_reversed_word

bbb = input("Write a word to reverse: ")

print(reverse_string(bbb))

def reverse_string3(word: str):
    # Method 1: Using slice notation (simplest)
    return word[::-1]

print(reverse_string3(bbb))
