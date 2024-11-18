from random import choice
import string
import base64

def encrypt_message(message):
    message = message.upper().replace(" ", "")
    key = "".join(choice(string.ascii_uppercase) for _ in range(len(message)))
    print(f"Key: {key}")

    encrypt = []
    for m_char, k_char in zip(message, key):
        value = chr(ord(m_char) ^ ord(k_char)) 
        encrypt.append(value)

    enc = "".join(encrypt)
    enc_bytes = enc.encode('utf-8')
    base = base64.b64encode(enc_bytes).decode('utf-8')
    return base, key

def decrypt_message(encrypted_base64, key):
    enc_bytes = base64.b64decode(encrypted_base64)
    enc = enc_bytes.decode('utf-8')
    
    decrypted = []
    for e_char, k_char in zip(enc, key):
        value = chr(ord(e_char) ^ ord(k_char)) 
        decrypted.append(value)
    
    return "".join(decrypted)
    message = input("Enter the message: ")
    encrypted_message, key = encrypt_message(message)
    print(f"Encrypted Message (Base64): {encrypted_message}")
  
    decrypted_message = decrypt_message(encrypted_message, key)
    print(f"Decrypted Message: {decrypted_message}")
