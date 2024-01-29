"""
MAIN IDEAS:
The idea behind Transposition Encryption is quite simple.
For example, given the first 5 letter of alphabet:

   Original letter:   A   B   C   D   E
   Scrambled letters: x   c   d   m   p

Note that we scramble the letter randomly.

DO NOTE THE FOLLOWING:
- This is an asymmetric encryption.

"""
import random


def scrambleLetter():
    # Create a list of 26 letters, each of them is a character:
    alphabet_numbers = list("abcdefghijklmnopqrstuvwxyz")
  
    # Creating key
    """
    For each letter in the alphabet
        Map them with a random character
    """
    # Step 1: Scrambling the alphabet:

    # First create an empty string
    shuffledCharacters = random.sample(alphabet_numbers)

    # STEP 2: MAP EACH LETTER IN THE NORMAL LIST WITH A LETTER IN THE SHUFFLE LIST
    for normal_letter in alphabet_numbers:
        for scrambled_letter in shuffledCharacters:
            # Create a mapping
            letter_mapping = {normal_letter:scrambled_letter}
            return letter_mapping

#TODO: REMOVE THIS METHOD LATER:
def testScrambleLetter(letter_mapping,alphabet_numbers):
    # Get a random character in the list
    random_Character = alphabet_numbers[random.randint(0,25)]

    # Get a value:
    selected_char = letter_mapping.get(random_Character)
    return selected_char


