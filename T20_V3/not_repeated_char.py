# Requirements:

# Return the first character that appears exactly once in the string.
# If no such character exists, return None.
# Keep character case-sensitive ("A" and "a" are different).
# Do not use collections.Counter.
# Examples:

# "automation" -> "u"
# "aabbcc" -> None
# "swiss" -> "w"
# "" -> None

def first_unique_char(text: str) -> str | None:
    dict1 = {}
    for letter in text:
        dict1[letter] = dict1.get(letter, 0) + 1
    
    # list1 = []
    # for k, v in dict1.items():
    #     if v == 1:
    #         list1.append(k)
            
    # if len(list1) == 0:
    #     return None
    # else:
    #     return list1[0]
    
    for letter in text:
        if dict1[letter] == 1:
            return letter

    return None

str1 = "automation"

print(first_unique_char(str1))
    
    
    