import os
from keyManager import generateKey, loadKey
from fileEncryptor import encryptFiles, decryptFiles
from utility import getDirectory

# Provide user with different options
def main():
    print("1. Generate a new encryption key")
    print("2. Encrypt files")
    print("3. Decrypt files")
    print("4. Exit")
    choice = input("Enter an option from the menu: ").strip()
    
    match choice:
        case "1":
            keyFile = input("Enter a name for your key's file").strip or "randsomKey.key"
            generateKey(keyFile)
        case "2":
            keyFile = input("Enter the key's file name to load the key: ").strip() or "randsomKey.key"
            if os.path.exists(keyFile): # If key file exists getDirectory
                directory = getDirectory()
                if directory:
                    encryptionKey = loadKey(keyFile) # Read files
                    encryptFiles(directory, encryptionKey) # Encrypt them
            else:
                print(f"Key file '{keyFile}' was not found. Try generating a key first.")
        case "3":
            keyFile = input("Enter the key's file name to load the key: ").strip() or "randsomKey.key"
            if os.path.exists(keyFile): # If key file exists getDirectory
                directory = getDirectory()
                if directory:
                    decryptionKey = loadKey(keyFile) # Read files
                    decryptFiles(directory, decryptionKey) # Decrypt them
            else:
                print(f"Key file '{keyFile}' was not found. Try generating a key first.")
        case "4":
            print("Exiting.")
            exit()
        case _:
            print("That is not a valid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    while True: # Keep running the main function until the user exits
        main()


