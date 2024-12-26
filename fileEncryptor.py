import os
from cryptography.fernet import Fernet

# Encrypt
def encryptFiles(targetDirectory, key):
    fernet = Fernet(key)
    for root, dirs, files in os.walk(targetDirectory): # Loops through and encrypts each file in directory
        for file in files:
            filePath = os.path.join(root, file)
            try:
                # Try to encrypt if possible
                with open(filePath, "rb") as f:
                    data = f.read()
                encryptedData = fernet.encrypt(data) # Read data and encrypt it
                with open(filePath, "wb") as f:
                    f.write(encryptedData) # Write encrypted data back in 
                print(f"Encrypted {filePath}") # Confirm success with user
            except Exception as e:
                print(f"Could not encrypt {filePath}: {e}")

# Decrypt (similar function to Encrypt)
def decryptFiles(targetDirectory, key):
    fernet = Fernet(key)
    for root, dirs, files in os.walk(targetDirectory):
        for file in files:
            filePath = os.path.join(root, file)
            try:
                with open(filePath, "rb") as f:
                    encryptedData = f.read()
                decryptedData = fernet.decrypt(encryptedData)
                with open(filePath, "wb") as f:
                    f.write(decryptedData)
                print(f"Decrypted {filePath}")
            except Exception as e:
                print(f"Could not decrypt {filePath}: {e}")
