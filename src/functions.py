alphabet = 'abcdefghijklmnñopqrstuvwxyz'

def cesar_cipher(message, key):
    ciphered_message = ""
    for char in message:
        new_char = char
        if char.casefold() in alphabet:
            new_char = alphabet[(alphabet.find(char.lower()) + key) % len(alphabet)]
            new_char = new_char.upper() if char.isupper() else new_char
        ciphered_message += new_char
    return ciphered_message

def cesar_decipher(message, key):
    return cesar_cipher(message, -key)