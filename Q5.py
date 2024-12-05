import random

def load_dictionary(file_path):
    """
    Loads words from a dictionary file.
    
    Parameters:
        file_path (str): Path to the dictionary file.
    
    Returns:
        list: A list of words from the file.
    """
    try:
        with open(file_path, 'r') as file:
            words = [line.strip() for line in file if line.strip()]  # Remove empty lines and spaces
        return words
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []

def generate_password(word_list, num_words=4):
    """
    Generates a password by combining random words from a list.
    
    Parameters:
        word_list (list): List of words to choose from.
        num_words (int): Number of words to combine for the password.
        separator (str): Separator to use between words (default is no separator).
    
    Returns:
        str: The generated password.
    """
    separator= str(random.randint(0, 99))
    if len(word_list) < num_words:
        raise ValueError("Not enough words in the word list to generate the password.")
    
    # Randomly select words
    chosen_words = random.sample(word_list, num_words)
    
    # Combine words into a single string
    return separator.join(chosen_words)

if __name__ == "__main__":
    # Prompt the user for the dictionary file and number of words
    dictionary_file = input("Enter the path to the dictionary file: ")
    word_list = load_dictionary(dictionary_file)
    
    if word_list:
        try:
            num_words = int(input("Enter the number of words for the password: "))
            password = generate_password(word_list, num_words,)
            print(f"Generated password: {password}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Could not load words from the dictionary file.")
