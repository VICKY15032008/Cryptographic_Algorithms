message=input("enter the message to encrypt:")
offset=int(input("enter the offset:"))
encryption='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
e_message=''
d=message.upper()
for letter in d:
    if letter in encryption:
        value=encryption.index(letter)
        new=(value+offset)%26
        e_message+=encryption[new]
print(e_message)  


for inset in range(0,27):
    d_message=''
    for chat in e_message:
       if chat in encryption:
           value=encryption.index(chat)
           new=(value-inset)%26
           d_message+=encryption[new]
    print(f"decrypted message:{d_message}")       
    ++inset
