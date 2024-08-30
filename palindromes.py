def string_input(sentence="Enter a string: "):
    """
    Prompts the user for input until a valid string (non-numeric) is provided.

    Args:
        sentence (str): The prompt message displayed to the user.

    Returns:
        str: The valid user input string.
    """
    while True:
        user_input = input(sentence)
        if user_input.isdigit():
            print("Invalid input! Please enter a string, not numbers.")
        else:
            return user_input


def is_palindrome(word):
    """
    Checks if a given word is a palindrome.

    A palindrome is a string that reads the same backward as forward.

    Args:
        word (str): The string to check.

    Returns:
        bool: True if the word is a palindrome, False otherwise.
    """
    return word == word[::-1]


def palindrome_substrings(input_sentences):
    """
    Finds all unique palindromic substrings within a given string.

    Args:
        input_sentences (str): The string in which to find palindromic substrings.

    Returns:
        set: A set containing all unique palindromic substrings.
    """
    palindrome = set()
    n = len(input_sentences)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = input_sentences[i:j]
            if is_palindrome(substring):
                palindrome.add(substring)
    return palindrome


input_sentence = string_input("Enter a string: ")
palindromes = palindrome_substrings(input_sentence)

print(f"Palindromic substrings:{palindromes}")
print(f"Total palindromic substrings: {len(palindromes)}")
