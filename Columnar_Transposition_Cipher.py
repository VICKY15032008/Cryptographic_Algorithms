import numpy as np
message=input("enter the message:")
key=input("enter the key:")
enum_key=list(enumerate(key))
def encrypt(message,key):
    message=list(message.replace(" ","").upper())
    key_length=len(key)
    row=len(message)//key_length + (len(message) % key_length > 0)
    while len(message)!=row*key_length:
        message.append("X")
    msg=np.array(message).reshape(row,key_length)
    column_order = [index for index, _ in sorted(enum_key, key=lambda x: x[1])]
    cipher_text=""
    for col in column_order:
            cipher_text+="".join(msg[:,col])
    return cipher_text

def decrypt(cipher_text,key):
    key_length = len(key)
    row = len(cipher_text) // key_length
    column_order = [index for index, _ in sorted(enumerate(key), key=lambda x: x[1])]
    grid = np.empty((row, key_length), dtype="str")
    idx = 0
    for col in column_order:
        for r in range(row):
            grid[r][col] = cipher_text[idx]
            idx += 1
    decrypt_text = ""
    for r in range(row):
        decrypt_text += "".join(grid[r])
    decrypt_text=decrypt_text.rstrip("X")    
    return decrypt_text
cipher_text=encrypt(message,key)  
print(encrypt(message,key))
print(decrypt(cipher_text,key))
