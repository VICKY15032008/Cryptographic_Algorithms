message=input("enter the message:")
key=input("enter the key:").upper()
l="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
k=[]


for i in key:
 if i not in k and i.isalpha():
    k.append(i)
for i in l:
    if i not in k:
        k.append(i)
k="".join(k)        

#encryption
enc=""
for i in message.upper():
    if i in k:
        index=k.index(i)
        enc+=l[index]
    else:
        enc += i    
print("enc:",enc)
#decryption
dec=""
for i in enc:
    if i in l:
        index=l.index(i)
        dec+=k[index]
    else:
        dec += i    
print("dec:",dec)        
            
