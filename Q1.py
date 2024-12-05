def caesar_cipher_encrypt(text, shift):
    """
    Encrypts the given text using the Caesar cipher algorithm.

    Parameters:
        text (str): The plaintext to encrypt.
        shift (int): The number of positions to shift each character.

    Returns:
        str: The encrypted text.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text


def caesar_cipher_decrypt(ciphertext, shift):
    """
    Decrypts the given ciphertext using the Caesar cipher algorithm.

    Parameters:
        ciphertext (str): The encrypted text to decrypt.
        shift (int): The number of positions to shift each character back.

    Returns:
        str: The decrypted text.
    """
    return caesar_cipher_encrypt(ciphertext, -shift)


# Example usage
if __name__ == "__main__":
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value: "))

    encrypted = caesar_cipher_encrypt(text, shift)
    print(f"Encrypted text: {encrypted}")

    decrypted = caesar_cipher_decrypt(encrypted, shift)
    print(f"Decrypted text: {decrypted}")
