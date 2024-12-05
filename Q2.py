def rail_fence_encrypt(plaintext, rails):
    """
    Encrypts the plaintext using the Rail Fence Cipher.

    Parameters:
        plaintext (str): The text to encrypt.
        rails (int): The number of rails (rows) to use in the cipher.

    Returns:
        str: The encrypted text (ciphertext).
    """
    if rails <= 1:
        return plaintext  # No encryption if there's only 1 rail
    
    # Create a list of empty strings for each rail
    rail_lines = [''] * rails
    rail = 0  # Current rail
    direction = 1  # 1 for down, -1 for up

    # Distribute characters across rails in zigzag pattern
    for char in plaintext:
        rail_lines[rail] += char
        rail += direction
        # Change direction at the top or bottom rail
        if rail == 0 or rail == rails - 1:
            direction *= -1

    # Combine all rails to form the ciphertext
    return ''.join(rail_lines)


def rail_fence_decrypt(ciphertext, rails):
    """
    Decrypts the ciphertext using the Rail Fence Cipher.

    Parameters:
        ciphertext (str): The encrypted text (ciphertext).
        rails (int): The number of rails (rows) used during encryption.

    Returns:
        str: The decrypted text (plaintext).
    """
    if rails <= 1:
        return ciphertext  # No decryption if there's only 1 rail

    # Create an empty matrix to simulate the zigzag pattern
    length = len(ciphertext)
    matrix = [[''] * length for _ in range(rails)]
    
    # Mark the zigzag pattern on the matrix
    rail = 0
    direction = 1
    for i in range(length):
        matrix[rail][i] = '*'
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    # Fill the matrix with characters from the ciphertext
    index = 0
    for row in range(rails):
        for col in range(length):
            if matrix[row][col] == '*':
                matrix[row][col] = ciphertext[index]
                index += 1

    # Read the matrix in zigzag order to reconstruct the plaintext
    rail = 0
    direction = 1
    plaintext = ''
    for i in range(length):
        plaintext += matrix[rail][i]
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    return plaintext


# Example usage
if __name__ == "__main__":
    plaintext = input("Enter the plaintext: ")
    rails = int(input("Enter the number of rails: "))

    # Perform encryption
    ciphertext = rail_fence_encrypt(plaintext, rails)
    print(f"Encrypted text (Ciphertext): {ciphertext}")

    # Perform decryption
    decrypted_text = rail_fence_decrypt(ciphertext, rails)
    print(f"Decrypted text (Plaintext): {decrypted_text}")

