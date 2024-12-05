import hashlib
import requests

def check_password_leak(password):
    """
    Checks if the password has been leaked using the Have I Been Pwned API.

    Parameters:
        password (str): The password to check.

    Returns:
        int: The number of times the password has been leaked.
    """
    # Hash the password using SHA-1
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    # Split the hash into prefix (first 5 characters) and suffix
    hash_prefix = sha1_hash[:5]
    hash_suffix = sha1_hash[5:]

    # Use the HIBP API to fetch all hashes with the same prefix
    url = f"https://api.pwnedpasswords.com/range/{hash_prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError(f"Error fetching data from HIBP API: {response.status_code}")

    # Check if the suffix is in the returned hashes
    hashes = response.text.splitlines()
    for hash_entry in hashes:
        hash_entry_suffix, count = hash_entry.split(':')
        if hash_entry_suffix == hash_suffix:
            return int(count)  # Return the number of times the password has been leaked

    return 0  # Password not found in the breach database


def process_file(filename):
    """
    Processes a file containing username-password pairs, checks each password for leaks.

    Parameters:
        filename (str): The name of the file to process.

    Returns:
        None
    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        print("Checking passwords for leaks...\n")
        for line in lines:
            username, password = line.strip().split(',')
            leak_count = check_password_leak(password)
            if leak_count > 0:
                print(f"ALERT: Password for user '{username}' has been leaked {leak_count} times.")
            else:
                print(f"Password for user '{username}' is safe (not found in breaches).")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Specify the input file
    filename = input("Enter the filename containing usernames and passwords: ")
    process_file(filename)
