import random, json
# encrypted decrypted

# message = input("message to encrypt: ")
ascii_chars_all = "#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
# indeks_list = []
secret_key = {}

def machine_to_encrypt(message):
    ascii_chars = ascii_chars_all
    encrypted_message = ""
    # char_list = []
    # char_list_encrypted = []

    for char in message:
        # char_list.append(char)
        char_encrypted = char.replace(char,random.choice(ascii_chars))
        ascii_chars = ascii_chars.replace(char_encrypted, "")
        # print("---------")
        # print(char_encrypted)
        # print(ascii_chars)
        # print("---------")
        # indeks = ascii_chars.index(char_encrypted)
        # indeks_list.append(indeks)
        encrypted_message += char_encrypted
        # char_list_encrypted.append(char_encrypted)
        secret_key[char_encrypted] = char

    # print(f"message to encrypt: {message}")
    # print(f"encrypted message: {encrypted_message}")
    # print(f"char_list1: {char_list}")
    # print(f"char_list_encrypted: {char_list_encrypted}")
    # print(f"index_list: {indeks_list}")
    # print(f"secret_key: {secret_key}")
    # print(f"secret_key JSON: {json.dumps(secret_key, indent=4)}")

    return encrypted_message

def decryptor(encrypted_message):
    # encrypted_message_list = list(encrypted_message)
    # print(f"encrypted_message_list: {encrypted_message_list}")
    decrypted_message = ""
    for j in secret_key:
        decrypted_message += secret_key[j]
    return decrypted_message

message = "Car is red"
print(f"Set the message: {message}")
# em = input("Set the message: ")
em = machine_to_encrypt(message)
print(f"Encrypted message: {em}")
print(f"Decrypted message: {decryptor(em)}")