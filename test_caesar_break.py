# -*- coding: utf-8 -*-
"""
Determine the shift of the Caesar Cypher

Created on Sat Feb  2 23:03:02 2019

@author: shakes
"""

import string
from collections import Counter

import test_caesar as tc


# Finds most frequently occurring letter
def mostFrequentLetter(counts):
    maxFreq = -1
    freqLetter = None
    for letter, freq in letter_counts.items():
        if freq > maxFreq and letter != " ":
            maxFreq = freq
            freqLetter = letter
    return freqLetter


# Predicts shift, assuming most frequent letter is 'e'
def predictShift(freqLetter):
    letters = (
        string.ascii_letters
    )  # contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shift = letters.index(freqLetter.lower()) - letters.index("e")
    return shift


if __name__ == "__main__":
    message = "Zyp cpxpxmpc ez wzzv fa le esp delcd lyo yze ozhy le jzfc qppe Ehz ypgpc rtgp fa hzcv Hzcv rtgpd jzf xplytyr lyo afcazdp lyo wtqp td pxaej hteszfe te Escpp tq jzf lcp wfnvj pyzfrs ez qtyo wzgp cpxpxmpc te td espcp lyo ozye esczh te lhlj Depaspy Slhvtyr"

    # Finds frequency of each letter
    letter_counts = Counter(message)

    freqLetter = mostFrequentLetter(letter_counts)
    print("Most frequently occurring letter:", freqLetter)
    predictedShift = predictShift(freqLetter)
    print("Predicted Shift:", predictedShift)
    keys, invKeys = tc.generateCypher(predictedShift)
    decryptedMessage = tc.decrypt(message, invKeys)
    print("Decrypted message:", decryptedMessage)
