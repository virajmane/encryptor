"""
This Script Generates two files one is the message and other one is the key
to get a single message embeded with the key check the other script
"""

from cryptography.fernet import Fernet
import sys

def keygen():
    key = Fernet.generate_key()
    with open("key.txt","wb") as k:
        k.write(key)

def encrypt(message):
    keygen()
    with open("key.txt","rb") as k:
        key = k.read()
    en_msg = message.encode()
    f = Fernet(key)
    result = f.encrypt(en_msg)
    with open("msg.txt", "wb") as m:
        m.write(result)
    print("Encrypted Text: " +str(result))
    print("Key: " +str(key))
    print("Encrypted Text and Key Files Generated!")

def decrypt(msgfile, keyfile):
    with open(keyfile, "rb") as k:
        key = k.read()
    with open(msgfile, "rb") as m:
        en_msg = m.read()
    f = Fernet(key)
    result = f.decrypt(en_msg)
    print(result.decode())
while True:
    ch = input("\nDo you want to Encrypt or Decrypt ?(E/D)\n> ")
    if ch=="E" or ch =="e":
        encrypt(input("Please Enter Your Text\n> "))
    elif ch=="D" or ch =="d":
        m = input("Enter Encrypted File Path \n> ")
        n = input("Enter Key File Path \n> ")
        decrypt(m,n)
    else:
        print("Thank You!")
        sys.exit()
