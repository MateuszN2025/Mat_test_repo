import random

# encrypted decrypted

# message = input("message to encrypt: ")
ascii_chars = "fdjkhfaliwaueyrwuiy238472489471920381098324yiewhrkjh"

def machine_to_encrypt(message):
    encrypted_message = ""
    char_list = []
    char_list_encrypted = []
    print(f"message to encrypt: {message}")
    for char in message:
        char_list.append(char)
        encrypted_message += char.replace(char,random.choice(ascii_chars))
    print(f"encrypted message: {encrypted_message}")
    print(f"char_list: {char_list}")
    return encrypted_message

print("---------")
machine_to_encrypt("Hi Mat")