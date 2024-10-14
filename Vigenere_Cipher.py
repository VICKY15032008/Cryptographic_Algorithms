message=input("enter the message:")
key=input("enter the key:")
key=key.lower()
count=0
encl=[]
decr=[]
#for encryption purpose:
for i in message:
   if i.isalpha():
       shift=ord(key[count%len(key)])-ord('a')
       if i.islower():
           cha=chr((ord(i)-ord('a')+shift)%26 +ord('a'))
       else:
           cha=chr((ord(i)-ord('A')+shift)%26 +ord('A'))
       encl.append(cha)
       count+=1
   else:
       encl.append(i)
encrypted_msg=''.join(encl)       
#for decryption purpose:
value=0
for i in encrypted_msg:
    if i.isalpha():
       shift=ord(key[value%len(key)])-ord('a')
       if i.islower():
           cha=chr(((ord(i)-ord('a')-shift)+26)%26 +ord('a'))
       else:
           cha=chr(((ord(i)-ord('A')-shift)+26)%26 +ord('A'))
       decr.append(cha)
       value+=1
    else:
       decr.append(i)
decrypted_msg="".join(decr)


print(f"Encrypted msg is:{encrypted_msg}")
print(f"Decrypted msg is:{decrypted_msg}")
       
       
       
