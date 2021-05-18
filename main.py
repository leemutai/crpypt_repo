from cryptography.fernet import Fernet


def write_key():
    """
    generate a key nand save it to a file

    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


# write_key() #call a function
# this function is for loading the key from the file generated
def load_key():
    """
    loads the key from the current directory named "key.key"
    """
    return open("key.key", "rb").read()


key = load_key()
print('key:', key)
message = "This is FUN".encode()
print("message", message)

# encrypting the message
f = Fernet(key)
# encrypt message using f
encrypted_message = f.encrypt(message)
print('Encrypted', encrypted_message)

# decrypting
# decrypted_message = f.encrypt(message)
# print('Encrypted:',encrypted_message)
decrypted_message = f.decrypt(encrypted_message)
print("Decrypted:", decrypted_message)