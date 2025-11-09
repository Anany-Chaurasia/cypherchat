
# This file is responsible for password hashing and verification 
# and also encryption/decryption of messages.

import bcrypt

def hasher(password:str):
    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(password, salt)
    return hashed

def checker(password:str, hashed:str):
    return bcrypt.checkpw(password, hashed)
