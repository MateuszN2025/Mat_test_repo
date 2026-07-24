def count_frequency(s):
    # Dictionary to store how many times each character appears.
    # Key = character, Value = occurrence count.
    freq = {}

    # Go through the string one character at a time.
    for ch in s:
        """
        # freq.get(ch, 0) means:
        # - if ch is already in the dictionary, get its current count
        # - if ch is not present yet, use 0 as a default
        # Then add 1 for the current occurrence.
        freq[ch] = freq.get(ch, 0) + 1
        """
        # 
        # If character already exists, increase its count.
        # If not, start its count at 1.
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # Return the completed frequency dictionary.
    return freq


# Example input string
text = "automation"

# Loop through (character, count) pairs and print them.
for char, count in count_frequency(text).items():
    print(f"{char}: {count}")
    
print("------------------------------------------")

from collections import Counter

text = "automation"
print(Counter(text))