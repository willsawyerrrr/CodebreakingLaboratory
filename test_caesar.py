# -*- coding: utf-8 -*-
"""
Caesar cypher script

Encode and decode messages by scrambling the letters in your message

Created on Fri Feb  1 23:06:50 2019

@author: shakes
"""

import string

letters = (
    string.ascii_letters
)  # contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def generateCypher(offset):
    offset = offset
    totalLetters = 26
    keys = {" ": " "}  # Caesar Cypher
    invKeys = {" ": " "}  # Inverse Caesar Cypher
    for index, letter in enumerate(letters):
        if index < totalLetters:  # lowercase
            keys[letter] = letters[(index + offset) % 26]
        else:  # uppercase
            keys[letter] = letters[(index + offset) % 26 + 26]
        invKeys[keys[letter]] = letter
    return keys, invKeys


def encrypt(message, keys):
    encryptedMessage = []
    for letter in message:
        encryptedMessage.append(keys[letter])
    encryptedMessage = "".join(encryptedMessage)
    return encryptedMessage


def decrypt(encryptedMessage, invKeys):
    decryptedMessage = []
    for letter in encryptedMessage:
        decryptedMessage.append(invKeys[letter])
    decryptedMessage = "".join(decryptedMessage)
    return decryptedMessage


if __name__ == "__main__":
    message = input("Enter a message to encypher: ")
    print("Message:", message)
    offset = int(input("Enter an offset: "))
    keys, invKeys = generateCypher(offset)
    encryptedMessage = encrypt(message, keys)
    print("Encrypted message:", encryptedMessage)
    decryptedMessage = decrypt(encryptedMessage, invKeys)
    print("Decrypted message:", decryptedMessage)
