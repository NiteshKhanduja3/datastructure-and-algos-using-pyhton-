from cryptography.fernet import Fernet

def write_key():

    #Genetrating the key
    
    key = Fernet.generate_key()

    with open("key.key","wb") as key_file:
        key_file.write(key)
def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()


key = load_key()


message = "Hello Nitesh".encode()

f = Fernet(key)
encrypted = f.encrypt(message)
print("this is encripted message:- ",encrypted)


decrypted_encrypted = f.decrypt(encrypted)
print("this is the decripted message:-  ",decrypted_encrypted)