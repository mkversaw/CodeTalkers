import hashlib
import os
import py2exe
# Opens cmd.exe and pipes stdout


print("Please enter your new password")
password=input()

h = hashlib.sha256()
h.update(password.encode('utf8')) 

hash_pw=open("encrypted_password.txt","w+")
hash_pw.write(h.hexdigest())
hash_pw.close()