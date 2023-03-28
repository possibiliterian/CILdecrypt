import os
os.system("cls")

import time

print("_______WELCOME TO MY SIMPLE DECRYPTING PROGRAM!_________")


# Decryption
def decrypt(ciphertext: str, key: int):
    alphabet =  "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    
    plaintext = ""
    count = 0
    
    while count < len(ciphertext):
       letter = ciphertext[count]
       plaintext = plaintext + letter
       count = count + key + 1

    return plaintext

ciphertext = input("Enter a message to decrypt (ciphertext) ")

# Input key (1-10)

key = int(input("Input your key as a number between 1 and 10 "))

# Error

while not (key>=1 and key<=10):
  print("Invalid key, try again!")
  key = int(input("Input your key as a number between 1 and 10"))

# "Loading"

print("Decrypting ciphertext...")
time.sleep(1)
plaintext = decrypt(ciphertext, key)

# Print output

print("Plaintext: " + plaintext)
print("THANK YOU")