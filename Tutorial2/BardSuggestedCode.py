import random

def create_cipher_map():
    """Creates a randomly shuffled cipher map."""
    letters = list("abcdefghijklmnopqrstuvwxyz")
    random.shuffle(letters)
    return dict(zip(letters, letters))

def encrypt(text, cipher_map):
    """Encrypts text using the given cipher map."""
    cipher_text = ""
    for char in text.lower():
        if char.isalpha():
            cipher_text += cipher_map.get(char, char)  # Preserve non-letters
        else:
            cipher_text += char
    return cipher_text

# Example usage:
cipher_map = create_cipher_map()
message = "This is a secret message."
encrypted_message = encrypt(message, cipher_map)
print("Encrypted message:", encrypted_message)