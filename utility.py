import os

# Get a directory to read files from
def getDirectory():
    directory = input("Enter the directory path you'd like to use: ").strip()
    if not os.path.exists(directory):
        createNew = input(f"The directory '{directory}' was not found. Would you like to create it? (y/n): ").strip().lower()
        if createNew == 'y': # Create new directory
            os.makedirs(directory, exist_ok=True) 
            print(f"Directory '{directory}' created.")
        else:
            print("Operation canceled.") # Confirm when user cancels
            return None
    return directory # If all is well, return directory
