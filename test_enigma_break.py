# -*- coding: utf-8 -*-
"""
Create and test an Enigma machine encryption and decoding machine

This code is based on the implementation of the Enigma machine in Python 
called pyEnigma by Christophe Goessen (initial author) and Cédric Bonhomme
https://github.com/cedricbonhomme/pyEnigma

Created on Tue Feb  5 12:17:02 2019

@author: uqscha22
"""

import string

import enigma
import rotor

letters = (
    string.ascii_letters
)  # contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
capitalLetters = letters[-26:]

ShakesHorribleMessage = "Xm xti ca idjmq Ecokta Rkhoxuu! Kdiu gm xex oft uz yjwenv qik parwc hs emrvm sfzu qnwfg. Gvgt vz vih rlt ly cnvpym xtq sgfvk jp jatrl irzru oubjo odp uso nsty jm gfp lkwrx pliv ojfo rl rylm isn aueuom! Gdwm Qopjmw!"
crib = "Hail Shakes!"


# Part C
#   Break the code via brute force search
t = 0
breakOut = False
for i in range(26):
    rotorOne = capitalLetters[i]
    if breakOut:
        break
    for j in range(26):
        if breakOut:
            break
        rotorTwo = capitalLetters[j]
        for k in range(26):
            t += 1
            key = rotorOne + rotorTwo + capitalLetters[k]
            engine = enigma.Enigma(
                rotor.ROTOR_Reflector_A,
                rotor.ROTOR_I,
                rotor.ROTOR_II,
                rotor.ROTOR_III,
                key=key,
                plugs="AA BB CC DD EE",
            )
            decryptedMessage = engine.encipher(ShakesHorribleMessage)
            cribSubstring = decryptedMessage[-12:]
            if cribSubstring == crib:
                breakOut = True
                break

# Print the decoded message
print(decryptedMessage)


# Part D
print("Number of tries:", t)  # 11772
#    My computer took around 45 seconds to search just under 12000 combinations.


# Part E
#    It would take my computer a period of time on the order of 10 ** 12 years
#    to brute force search an Enigma encryption with 5 rotors and the plugboard.
