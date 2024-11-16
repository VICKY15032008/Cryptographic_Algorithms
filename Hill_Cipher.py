import numpy as np
size=int(input("enter the size from2:"))
key=input(f"enter the key with {size*size} letters:").upper().replace(" ","")
message=input(f"enter the message:").upper().replace(" ","")

def key_matrix(key,size):
    matrix=[]
    for i in key:
        value=ord(i)-ord('A')
        matrix.append(value)
    matrix=np.array(matrix,dtype="i4").reshape((size,size))
    return matrix

def encrypt(message,key,size):
    key_vector=key_matrix(key,size)
    vector=[]
    encrypt=''
    for i in message:
        value=ord(i)-ord('A')
        vector.append(value)
    while len(vector)%size !=0:
        vector.append((ord('X')-ord('A')))
   
    enc=[]
    for i in range(0,len(vector),size):
        s_dim=vector[i:i+size]
        block=np.dot(key_vector,s_dim)%26
        enc.extend(block)
    enc_value=[]  
    for i in enc:
        val=chr(i+ord('A'))
        enc_value.append(val)
    encrypt="".join(enc_value)
    return encrypt
    
    
print(key_matrix(key,size))    
print(encrypt(message,key,size))    
