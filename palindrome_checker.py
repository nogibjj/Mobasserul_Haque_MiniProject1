def is_palindrome(word: str) -> bool:
    """
    Check if the given word is a palindrome.
    
    A palindrome is a word that reads the same forwards and backwards.
    
    Args:
    word (str): The word to check.

    Returns:
    bool: True if the word is a palindrome, False otherwise.
    """
    # Normalize the word to lowercase for case-insensitive comparison
    normalized_word = word.lower()
    # Check if the word reads the same forwards and backwards
    return normalized_word == normalized_word[::-1]
