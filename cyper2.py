from cryptography.fernet import Fernet
import sys

def keygen():
    key = Fernet.generate_key()
    return key

def encrypt(message):
    key = keygen()
    #with open("key.txt","rb") as k:
    #    key = k.read()
    en_msg = message.encode()
    f = Fernet(key)
    result = f.encrypt(en_msg)
    final = "{} {}".format(result,key)
    print("Please Save the below encypted message:")
    print(final)

def decrypt():
    try:
        en_msg,key = input("Enter the encrypted message ").split("' b'")
        en_msg = bytes(en_msg[1:], 'utf-8')
        key = bytes(key[:-1], 'utf-8')
        f = Fernet(key)
        result = f.decrypt(en_msg)
        print(result.decode('utf-8'))
    except ValueError:
        print("Incorrect Values")
while True:
    ch = input("\nDo you want to Encrypt or Decrypt ?(E/D)\n> ")
    if ch=="E" or ch =="e":
        encrypt(input("Please Enter Your Text\n> "))
    elif ch=="D" or ch =="d":
        decrypt()
    elif ch=="x" or ch=="X":
        print("Thank You!")
        sys.exit()
    else:
        continue
