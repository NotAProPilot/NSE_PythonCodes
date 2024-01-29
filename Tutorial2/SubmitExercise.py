def encryptMessage(message, key):
    ciphertext = ""
    keyMap = sorted(key)
    col = len(key)
    row = int(len(message) / col) + (1 if len(message) % col else 0)

    matrix = [['' for i in range(col)] for j in range(row)]
    index = 0
    for i in range(row):
        for j in range(col):
            if index < len(message):
                matrix[i][j] = message[index]
            index += 1

    for i in keyMap:
        for j in range(row):
            ciphertext += matrix[j][key.index(i)]

    return ciphertext

def decryptMessage(ciphertext, key):
    plaintext = ""
    keyMap = sorted(key)
    col = len(key)
    row = int(len(ciphertext) / col)

    matrix = [['' for i in range(row)] for j in range(col)]
    index = 0
    for i in keyMap:
        for j in range(row):
            matrix[key.index(i)][j] = ciphertext[index]
            index += 1

    for i in range(row):
        for j in range(col):
            plaintext += matrix[j][i]

    return plaintext

# Get user input
message = input("Enter the message to encrypt: ")
key = input("Enter the key (a string of unique characters): ")

# Encrypt the message
encrypted_message = encryptMessage(message, key)
print("Encrypted message:", encrypted_message)

# Decrypt the message (optional)
decrypted_message = decryptMessage(encrypted_message, key)
print("Decrypted message:", decrypted_message)