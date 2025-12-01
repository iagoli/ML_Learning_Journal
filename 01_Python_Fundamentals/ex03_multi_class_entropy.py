# Exercise: ex03_multi_class_entropy
# Topic: 01 Python Fundamentals
"""
--------------------------------------------------------------------------------------------------
3- Escreva uma função em Python, idêntica à do problema anterior, mas que permita calcular a
entropia de um conjunto contendo elementos de n classes distintas, a qual se pode expressar
matematicamente da seguinte forma:
Entropia(𝑆) = − ∑ 𝑝𝑖 log2(𝑝𝑖)𝑛
𝑖=1 ,
sendo pi=ni/n a proporção de elementos da i-ésima classe que estão contidos no grupo
--------------------------------------------------------------------------------------------------

"""

from math import log2
from typing import Optional

def entropyN(*args: int) -> Optional[float]:
    """
    Calculates the entropy of a set containing N classes of elements.
    
    Args:
        *args: A variable number of non-negative integers representing 
               the counts (ni) of each class.

    Returns:
        float: The entropy of the distribution, or None if input is invalid.
    """
    
    for n in args:
        if n < 0:
            print("All class counts must be non-negative integers.")
            return None
            
    total = sum(args)
    
    if total == 0:
        return 0.0

    entropy = 0.0
    
    for n in args:
        p = n / total
        
        if p > 0:
            entropy -= p * log2(p)
            
    return entropy

# Test the function 
print(entropyN(0, 0, 0, 1))
print(entropyN(1, 1, 1, 1))
print(entropyN(1, 2, 3, 4))
print(entropyN(-1, 1, 1))
