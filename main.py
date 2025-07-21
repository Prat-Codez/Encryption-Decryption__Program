import string
import random

print("Welcome to Encryption Program")
chars=" "+string.ascii_letters+string.punctuation+string.digits
chars=list(chars)
keys=chars.copy()
random.shuffle(keys)
#print(f"Chars:{chars}")
#print(f"Keys:{keys}")

while True:
    Mode=input("Type '1' to Encrypt a message , type '2' to Decrypt a message , type '3' to Quit: ")

# Encrypt
    def encrypt():
        plain_text=input("Enter Original Text: ")
        cipher_text=""
        for letter in plain_text:
            index=chars.index(letter)
            cipher_text+=keys[index]
        print(f"Plain_Text: {plain_text}")
        print(f"Cipher_Text: {cipher_text}")

#Decrypt
    def decrypt():
        cipher_text=input("Enter Encrypted Text: ")
        plain_text=""
        for letter in cipher_text:
            index=keys.index(letter)
            plain_text+=chars[index]
        print(f"Encrypted_Text: {cipher_text}")
        print(f"Decrypted_Text: {plain_text}")
    if Mode=="1":
        encrypt()
    elif Mode=="2":
        decrypt()
    elif Mode=="3":
        print("Thank you for using Encryption Program")
        exit()
    else:
        print("Invalid Input")
