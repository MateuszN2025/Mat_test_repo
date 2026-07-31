from collections import Counter


print("------------------------------------------")
string = "automation"
c = Counter(string)
print(dict(c))


print("------------------------------------------")

def count_string(text: str) -> dict:
    dict1 = {}

    for letter in text:
        # dict1[letter] = text.count(letter)
        dict1[letter] = dict1.get(letter, 0) + 1
        # Mini trace
        # Start: dict1 = {}
        # letter = 'a'
        # get('a', 0) -> 0, 0 + 1 -> 1, store → {'a': 1}
        # next letter = 'a'
        # get('a', 0) -> 1, 1 + 1 -> 2, store → {'a': 2}
        # letter = 't'
        # get('t', 0) -> 0, 0 + 1 -> 1, store → {'a': 2, 't': 1}
    return dict1
        
dict2 = {'a': 2, 'u': 1, 't': 2, 'o': 2, 'm': 1, 'i': 1, 'n': 1}
print(count_string(string))
print(dict2.get("t")) # dict.get() in Python safely reads a dictionary value by key.
print("------------------------------------------")
