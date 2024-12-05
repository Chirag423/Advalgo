from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature

def generate_keys():
    """
    Generates a pair of RSA keys (private and public).
    Returns:
        private_key, public_key: The RSA private and public keys.
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

def sign_document(private_key, document):
    """
    Signs a document using the provided private key.
    Parameters:
        private_key: The RSA private key used for signing.
        document (str): The document to sign.
    Returns:
        bytes: The signature.
    """
    document_bytes = document.encode('utf-8')
    signature = private_key.sign(
        document_bytes,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def verify_signature(public_key, document, signature):
    """
    Verifies the signature of a document using the provided public key.
    Parameters:
        public_key: The RSA public key used for verification.
        document (str): The document to verify.
        signature (bytes): The signature to verify.
    Returns:
        bool: True if the signature is valid, False otherwise.
    """
    document_bytes = document.encode('utf-8')
    try:
        public_key.verify(
            signature,
            document_bytes,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False

def serialize_public_key(public_key):
    """
    Serializes a public key to send it as part of the signed document package.
    Parameters:
        public_key: The RSA public key to serialize.
    Returns:
        bytes: Serialized public key in PEM format.
    """
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

def deserialize_public_key(pem_data):
    """
    Deserializes a PEM-formatted public key.
    Parameters:
        pem_data (bytes): The serialized public key in PEM format.
    Returns:
        public_key: The deserialized RSA public key.
    """
    return serialization.load_pem_public_key(pem_data)

if __name__ == "__main__":
    # Step 1: Generate RSA keys
    private_key, public_key = generate_keys()

    # Step 2: Document to be signed
    document = "This is a confidential document that must not be altered."

    # Step 3: Sign the document
    signature = sign_document(private_key, document)
    print("Document signed successfully.")

    # Serialize the public key for sharing
    serialized_public_key = serialize_public_key(public_key)

    # Simulate sending the document, signature, and public key
    print("\n--- Sending the Document ---")
    print("Document:", document)
    print("Signature:", signature.hex())  # Hex format for readability
    print("Public Key (PEM):", serialized_public_key.decode('utf-8'))

    # Step 4: Receiver verifies the document
    print("\n--- Verifying the Document ---")
    received_public_key = deserialize_public_key(serialized_public_key)
    is_valid = verify_signature(received_public_key, document, signature)

    if is_valid:
        print("The document's signature is valid. It has not been altered.")
    else:
        print("The document's signature is invalid. It may have been tampered with.")
