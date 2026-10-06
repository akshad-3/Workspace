def encrypt(text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "QWERTYUIOPASDFGHJKLZXCVBNM"

    result = ""

    for char in text.upper():
        if char.isalpha():
            result += key[alphabet.index(char)]
        else:
            result += char

    return result


def decrypt(text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "QWERTYUIOPASDFGHJKLZXCVBNM"

    result = ""

    for char in text.upper():
        if char.isalpha():
            result += alphabet[key.index(char)]
        else:
            result += char

    return result


plaintext = input("Enter plaintext: ")

ciphertext = encrypt(plaintext)

print("Encrypted text:", ciphertext)
print("Decrypted text:", decrypt(ciphertext))