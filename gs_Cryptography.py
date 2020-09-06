import hashlib
from cryptography.fernet import Fernet

def getSHA256(inputString, iterations):     #returns SHA-256 hash of inputString
    hash256 = hashlib.sha256()          #I would salt this, but that requires a second input 
    for i in range(iterations):         #And I don't have enough time to figure a good one out
        hash256.update(inputString.encode("utf8"))  #Besides, who has time to wait around
    return hash256.hexdigest()      #for their computer to do fifty million hashes per possible string?
                                        #Just follow the XKCD guidelines for good passwords

def encode(message, keyHash):   #functions for encoding/decoding a message given a keyHash
    f = Fernet(keyHash)         #hashing the key won't do much, but it's 3:30 in the morning and I don't care
    encrypted = f.encrypt(bytearray(message, "utf8"))
    return encrypted

def decode(message, keyHash):
    f = Fernet(keyHash)
    decrypted = f.decrypt(message)
    return decrypted