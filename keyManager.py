from cryptography.fernet import Fernet

# Generates a key
def generateKey(keyFile="ransomKey.key"):
    key = Fernet.generateKey() # Generates a random key using Fernet
    with open(keyFile, "wb") as keyOut:
        keyOut.write(key) # Write key to file
    print("Encryption key saved")
    return key

# Load existing key
def loadKey(keyFile="ransomKey.key"):
    with open(keyFile="rb") as keyIn: # Read Binary
        return keyIn.read()
