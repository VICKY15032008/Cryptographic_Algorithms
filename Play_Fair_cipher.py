import string

def create_key_matrix(key):
    # Remove duplicates and replace 'J' with 'I'
    key = key.upper().replace('J', 'I')
    key = ''.join(sorted(set(key), key=key.index))  # Remove duplicates while maintaining order

    # Create a 5x5 matrix
    matrix = []
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # 'J' is excluded
    for char in key:
        if char not in matrix and char in alphabet:
            matrix.append(char)
    
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def format_message(message):
    message = message.upper().replace('J', 'I')
    message = ''.join(filter(lambda x: x in string.ascii_uppercase, message))
    
    # Add padding
    formatted_message = []
    i = 0
    while i < len(message):
        if i + 1 < len(message) and message[i] == message[i + 1]:
            formatted_message.append(message[i])
            formatted_message.append('X')  # Padding character
            i += 1
        else:
            formatted_message.append(message[i])
            if i + 1 < len(message):
                formatted_message.append(message[i + 1])
                i += 2
            else:
                formatted_message.append('X')  # Padding character for odd length
                i += 1

    return ''.join(formatted_message)

def find_position(char, matrix):
    for i, row in enumerate(matrix):
        if char in row:
            return (i, row.index(char))
    return None

def encrypt(message, key):
    key_matrix = create_key_matrix(key)
    formatted_message = format_message(message)
    ciphertext = []

    for i in range(0, len(formatted_message), 2):
        row1, col1 = find_position(formatted_message[i], key_matrix)
        row2, col2 = find_position(formatted_message[i + 1], key_matrix)

        if row1 == row2:  # Same row
            ciphertext.append(key_matrix[row1][(col1 + 1) % 5])
            ciphertext.append(key_matrix[row2][(col2 + 1) % 5])
        elif col1 == col2:  # Same column
            ciphertext.append(key_matrix[(row1 + 1) % 5][col1])
            ciphertext.append(key_matrix[(row2 + 1) % 5][col2])
        else:  # Rectangle
            ciphertext.append(key_matrix[row1][col2])
            ciphertext.append(key_matrix[row2][col1])

    return ''.join(ciphertext)

def decrypt(ciphertext, key):
    key_matrix = create_key_matrix(key)
    plaintext = []

    for i in range(0, len(ciphertext), 2):
        row1, col1 = find_position(ciphertext[i], key_matrix)
        row2, col2 = find_position(ciphertext[i + 1], key_matrix)

        if row1 == row2:  # Same row
            plaintext.append(key_matrix[row1][(col1 - 1) % 5])
            plaintext.append(key_matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:  # Same column
            plaintext.append(key_matrix[(row1 - 1) % 5][col1])
            plaintext.append(key_matrix[(row2 - 1) % 5][col2])
        else:  # Rectangle
            plaintext.append(key_matrix[row1][col2])
            plaintext.append(key_matrix[row2][col1])

    return ''.join(plaintext).replace('X', '')


key = input("enter the key:")
message =input("enter the message:")
ciphertext = encrypt(message, key)
decrypted_message = decrypt(ciphertext, key)

print(f"Key Matrix:\n{create_key_matrix(key)}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Message: {decrypted_message}")
