import re

print("------------------------------------------")
text = "My phone Number is 12345"
pattern = "phone"
result = re.search(pattern=pattern, string=text)
print(result)

print("------------------------------------------")
numbers = re.findall(pattern=r"\d", string=text) # ['1', '2', '3', '4', '5']
# numbers = re.findall(pattern=r"\d+", string=text) # ['12345']
print(numbers)

print("------------------------------------------")
all_word = re.findall(pattern=r"\w+", string=text) # ['My', 'phone', 'number', 'is', '12345']
print(all_word)
alphabetic_words = re.findall(r"[A-Z][a-z]+", text) # ['My', 'phone', 'number', 'is']
print(alphabetic_words)

print("------------------------------------------")
spaces = re.findall(pattern=r"\s", string=text)
print(spaces)

print("------------------------------------------") 
text2 = "cat cot cut"
findings = re.findall(pattern=r"c.t", string=text2)
print(findings)

print("------------------------------------------")
text3 = "cat bat hat"
findings2 = re.findall(pattern=r"[cbh]at", string=text3)
print(findings2)