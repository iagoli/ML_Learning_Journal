# Exercise: ex04_word_count_and_sort
# Topic: 01 Python Fundamentals

#-----------------------------------------------------------
# 4- Ler um texto e apresentar por ordem alfabética o número
# de ocorrências de cada palavra contida nesse texto
#-----------------------------------------------------------

import string
from collections import Counter
from typing import Dict

def count_words(text: str) -> Dict[str, int]:
    """
    Counts the occurrences of each word in a given text, ignoring punctuation, 
    and returns the results sorted alphabetically by word.

    Args:
        text: The input text (string).

    Returns:
        A dictionary where keys are unique words (lowercase) and values are their counts,
        sorted alphabetically by key.
    """
    
    translator = str.maketrans('', '', string.punctuation)
    
    normalized_text = text.translate(translator).lower()
    words = normalized_text.split()
    
    if not words:
        return {}

    word_counts = Counter(words)
    
    return dict(sorted(word_counts.items()))

if __name__ == "__main__":
    user_text = input("Input a text: ")
    result = count_words(user_text)
    
    for word, count in result.items():
        print(f"{word}: {count}")