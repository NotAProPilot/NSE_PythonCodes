"""
MAIN IDEAS:
The idea behind Transposition Encryption is quite simple.
For example, here are the first five letters of alphabet:

   Original letter:   A   B   C   D   E
   Scrambled letters: x   c   d   m   p

Note that we scramble the letter randomly.

DO NOTE THE FOLLOWING:
- This is an asymmetric encryption.

PSEUDOCODE:
- assign each letter in the alphabet with a letter with a random letter
- approach:
+ create a list of normal letter
+ create a list of shuffled letter:
for each normal letter
   for each shuffled letter
        assign each normal letter to shuffled letter (i'm not sure if i should be using mapping or dictionary)

A function that takes in user string
for each character in said string
   converts them into a scrambled letter using the approach mentioned above
"""

# Creating a function to shuffle letters:
def shuffleLetter():
    # Initializing a list of normal characters:
    letters = list("abcdefghijklmnopqrstuvwxyz")



