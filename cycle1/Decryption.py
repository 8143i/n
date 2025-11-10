cipher_text = input("Enter text to decrypt: ")
shift = int(input("Enter shift value: "))
original = ""

for char in cipher_text:
    if char.isupper():
        original += chr((ord(char) - shift - 65) % 26 + 65)
    elif char.islower():
        original += chr((ord(char) - shift - 97) % 26 + 97)
    else:
        original += char 

print("Decrypted text:", original)

