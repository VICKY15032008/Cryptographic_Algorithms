message=input("enter the message:")
depth=int(input("enter the depth:"))
def encrypt(message,depth):
  rails=[[""for _ in range(len(message))]for _ in range(depth)]
  direction=1
  row,col=0,0
  for i in message:
      rails[row][col]=i
      col=col+1
      if row==0:
        direction=1
      elif row==(depth-1):
        direction=-1
      row=row+direction
  print(rails)   
  encrypt="".join(["".join(rail) for rail in rails])  
  return encrypt


def decrypt(enc_msg,depth):
    rails=[[""for _ in range(len(enc_msg))]for _ in range(depth)]
    row,col=0,0
    direction=1
    
    for i in range(len(enc_msg)):
        rails[row][col]="*"
        col=col+1
        if row==0:
            direction=1
        elif row==(depth-1):
            direction=-1
        row=row+direction
    count=0
    print("rails at setting stage:",rails)
    for i in range(depth):
        for j in range(len(enc_msg)):
           if rails[i][j]=="*":
                rails[i][j]=enc_msg[count]
                count=count+1
    print("rails at inserting stage:",rails)           
    decrypt_msg=[]
    row=0
    col=0
    for i in range(len(enc_msg)):
        decrypt_msg.append(rails[row][col])
        col=col+1
        if row==0:
            direction=1
        elif row==(depth-1):
            direction=-1
        row=row+direction 
    return "".join(decrypt_msg)
enc_msg=encrypt(message,depth)    
print("encrypted_msg using rail fence cipher:",encrypt(message,depth))
print("decrypted_msg using rail fence cipher:",decrypt(enc_msg,depth))
