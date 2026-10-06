def caesar_decrypt(ciphertext, shift):
    result = ""

    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char

    return result


ciphertext = input("Enter encrypted text: ")

print("\nPossible plaintexts:")
for shift in range(26):
    print(f"Shift {shift}: {caesar_decrypt(ciphertext, shift)}")