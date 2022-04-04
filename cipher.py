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
        encryptedLetter += ord('A')
        cipher_text.append(chr(encryptedLetter))
    return ("".join(cipher_text))

def decryption(cipher_text, key):
    originalString = []
    for letter in range(len(cipher_text)):
        decryptedLetter = (ord(cipher_text[letter]) - ord(key[letter]) + 26) %26
        decryptedLetter += ord('A')
        originalString.append(chr(decryptedLetter))
    newString = condenseString(originalString)
    return newString

#The index out of range is in this function. 
#this function is not generating a random string of characters at length inputString
def generateKey(inputString):
    characterList = []
    for i in range(len(inputString)):
        randomletters = random.choice(string.ascii_lowercase)
        characterList.append(randomletters)
    newString = condenseString(characterList)
    return newString

def condenseString(characterList):
    newString = ""
    for letter in characterList:
        newString += letter
    return newString


if __name__ == "__main__":
    inputString = input("Enter a word:")
    key = generateKey(inputString)
    encrypt = VinegereCypher(inputString, key)
    print(encrypt)
    decrypt = decryption(encrypt,key)
    print(decrypt)
