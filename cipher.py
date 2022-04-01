# --------------------------------------------------------------------------------------------
# Matthew Anzano 
# 3/31/2022
# Montclair State University
# Description: The vigenere cypher requires that the plain text be converted useing a matrix 
# of the english alphabte
#---------------------------------------------------------------------------------------------

from operator import mod
import random
import string

#Formula for Encryption 
# Ei = (Pi + Ki) mod 26

#Formula for Decryption 
# Di = (Ei - Ki + 26) mod 26

#Translating the alphabet from letters to numbers for this to work

def VinegereCypher(inputString, key):
    #Taking input from user
    cipher_text = []
    for i in range(len(inputString)):
        encryptedLetter = (ord(inputString[i]) + ord(key[i])) % 26
        cipher_text.append(chr(encryptedLetter))
    return ("".join(cipher_text))



def generateKey(inputString):
    lengthOfString = inputString
    for i in range(len(lengthOfString)):
        randomletters = random.choice(string.ascii_lowercase) 
        key = ''.join(randomletters)
    return key




if __name__ == "__main__":
    inputString = input("Enter a word:")
    key = generateKey(inputString)
    encrypt = VinegereCypher(inputString, key)
    print(encrypt)
