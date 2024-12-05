import hashlib

def hash_password(password):
    """
    Hashes a given password using SHA-256 and returns its hexadecimal representation.

    Parameters:
        password (str): The input password to hash.

    Returns:
        str: The SHA-256 hashed representation of the password as a hexadecimal string.
    """
    # Encode the password to bytes, as hashlib works on byte data
    password_bytes = password.encode('utf-8')
    
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()
    
    # Update the hash object with the password bytes
    sha256_hash.update(password_bytes)
    
    # Return the hexadecimal digest of the hash
    return sha256_hash.hexdigest()

# Example usage
if __name__ == "__main__":
    password = input("Enter the password: ")
    hashed_password = hash_password(password)
    print(f"SHA-256 Hashed Password: {hashed_password}")
