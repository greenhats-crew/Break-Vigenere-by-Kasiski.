from pycipher import Vigenere
import re

def encrypt(key, plaintext):
    if key == '' or key.isnumeric():
        return plaintext
    key = re.sub(r'[^A-Z]', '', key.upper())
    return Vigenere(key).encipher(plaintext)

def decrypt(key, ciphertext):
    if key == '' or key.isnumeric():
        return ciphertext
    key = re.sub(r'[^A-Z]', '', key.upper())
    return Vigenere(key).decipher(ciphertext)

def main():
    choice = input("Would you like to encrypt or decrypt? ").lower()
    key = input("Enter the key: ")
    text = input("Enter the text, or filename.txt to read the text from: ")
    if text.endswith('.txt'):
        with open(text, 'r') as file:
            text = file.read()
    if choice == 'encrypt':
        print(encrypt(key, text))
        with open('encrypted.txt', 'w') as file:
            file.write(encrypt(key, text))
    elif choice == 'decrypt':
        print(decrypt(key, text))
    else:
        print("Invalid choice")
    
if __name__ == '__main__':
    main()