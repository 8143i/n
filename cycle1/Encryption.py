# Caesar Cipher Encryption

text = input("Enter text to encrypt: ")
shift = int(input("Enter shift value: "))
cipher = ""

for char in text:
    if char.isupper():
        cipher += chr((ord(char) + shift - 65) % 26 + 65)
    elif char.islower():
        cipher += chr((ord(char) + shift - 97) % 26 + 97)
    else:
        cipher += char
print("Encrypted text:", cipher)

