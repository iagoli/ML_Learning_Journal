# Exercise: ex05_palindrome_checker
# Topic: 01 Python Fundamentals

"""
-------------------------------------------------------------------------------------
5- Defina uma função que verifique se um dado texto é capicua, que seja insensível a maiúsculas
e minúsculas e que ignore a pontuação, espaços e outros carateres não alfanuméricos. Por
exemplo, o texto “Rise to vote, sir.” é capicua.
-------------------------------------------------------------------------------------
"""
import string

def is_palindrome(text: str) -> bool:
    """
    Checks if a given text is a palindrome (capicua).

    The function is case-insensitive and ignores all non-alphanumeric 
    characters (punctuation, spaces, etc.).

    Args:
        text: The input text (string).

    Returns:
        True if the text is a palindrome, False otherwise.
    """
    
    chars_to_remove = string.punctuation + string.whitespace
    translator = str.maketrans('', '', chars_to_remove)
    
    normalized_text = text.translate(translator).lower()
    
    return normalized_text == normalized_text[::-1]

if __name__ == "__main__":
    user_input = input("Enter a sequence of characters, phrases, or numbers: ")
    
    is_it_palindrome = is_palindrome(user_input)
    
    if is_it_palindrome:
        print(f"'{user_input}' IS a palindrome (capicua).")
    else:
        print(f"'{user_input}' IS NOT a palindrome.")