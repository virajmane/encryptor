from cryptography.fernet import Fernet

def keygen():
    key = Fernet.generate_key()
    with open("key.txt","wb") as k:
        k.write(key)

def encrypt(message):
    with open("key.txt","rb") as k:
        key = k.read()
    en_msg = message.encode()
    f = Fernet(key)
    result = f.encrypt(en_msg)
    with open("msg.txt", "wb") as m:
        m.write(result)
    print("Encrypted Text File Generated in Current Folder!")
    print("Key Text File Generated in Current Folder!")

def decrypt(msgfile, keyfile):
    with open(keyfile, "rb") as k:
        key = k.read()
    with open(msgfile, "rb") as m:
        en_msg = m.read()
    f = Fernet(key)
    result = f.decrypt(en_msg)
    print(result.decode())
ch = input("Do you want to Encrypt or Decrypt ? (E/D)")
if ch=="E".casefold():
    encrypt(input("Please Enter Your Text\n> "))
elif ch=="D".casefold():
    m = input("Enter Encrypted File Path \n> ")
    n = input("Enter Key File Path \n> ")
    decrypt(m,n)
else:
    print("Invalid Choice")