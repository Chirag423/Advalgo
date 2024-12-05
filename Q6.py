import itertools
import string

def brute_force_attack(target_password, max_length):
    """
    Simulates a brute-force attack to guess a password.

    Parameters:
        target_password (str): The password to crack.
        max_length (int): The maximum length of the password to try.

    Returns:
        str: The cracked password, if found.
        int: The number of attempts it took to crack the password.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    attempts = 0

    for length in range(1, max_length + 1):
        # Generate all possible combinations of the given length
        for combination in itertools.product(characters, repeat=length):
            # Convert tuple to string
            guess = ''.join(combination)
            attempts += 1

            # Check if the guess matches the target password
            if guess == target_password:
                return guess, attempts

    # If not found within max_length
    return None, attempts


if __name__ == "__main__":
    print("=== Brute-Force Password Attack Simulation ===")
    # Get target password from the user
    target_password = input("Enter the target password to crack: ")
    max_length = int(input("Enter the maximum password length to try: "))

    print("\nAttempting to crack the password...")
    result, attempts = brute_force_attack(target_password, max_length)

    if result:
        print(f"\nPassword cracked: {result}")
        print(f"Total attempts: {attempts}")
    else:
        print("\nFailed to crack the password within the given length.")
