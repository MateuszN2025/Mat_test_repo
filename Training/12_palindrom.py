# kajak
# kajak
# kot
# tok
# parzysta ilość liter i nieparzysta
# ostatnia liter = 1 litera odwórconego słowa


word = 'acba'

# tok != kot nie palindrom

def if_palindorm(word1: str):
    reversed_word = word[::-1]
    if word1 == reversed_word:
        print('yes')
    else:
        print('no')

if_palindorm(word)
