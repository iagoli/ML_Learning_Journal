# Exercise: ex02_binary_entropy
# Topic: 01 Python Fundamentals
"""
----------------------------------------------------------------------------------------------
2- Considere um conjunto S formado por n1 elementos de um determinado tipo e n2 elementos
doutro tipo. A entropia é uma medida que quantifica de alguma forma a desordem
(impureza) de um conjunto de elementos e, para o caso de existirem só 2 classes de
elementos, é expressa da seguinte forma:

Entropia(𝑆) = −𝑝1 log2(𝑝1) − 𝑝2 log2(𝑝2),

em que p1=n1/(n1+n2) e p2=n2/(n1+n2) são as proporções do primeiro e do segundo tipos de
elementos, respetivamente.
Escreva em Python a função entropia, que comece por validar devidamente os dados de
entrada do problema, invocando-a depois para conjuntos com as seguintes proporções: 0/1,
0.5/0.5, 0.1/0.9 e 0.9/0.1. Não se esqueça de documentar devidamente a função
----------------------------------------------------------------------------------------------

""" 
from math import log2
from typing import Optional

def entropy2(n1: int, n2: int) -> Optional[float]:
    """
    Calculates the entropy of a set containing two classes of elements.

    Args:
        n1: Number of occurrences of the first class of elements.
        n2: Number of occurrences of the second class of elements.

    Returns:
        float: The entropy of the distribution, or None if the input is invalid.
    """
    
    if n1 < 0 or n2 < 0:
        print("n1 and n2 must be non-negative.")
        return None
    
    total = n1 + n2
    
    if total == 0:
        return 0.0

    p1 = n1 / total
    p2 = n2 / total

    entropy = 0.0
    
    for p in [p1, p2]:
        if p > 0:
            entropy -= p * log2(p)
            
    return entropy

# Test case with invalid input
print(entropy2(-5, 5)) 

# Test cases from the exercise: 0/1, 0.5/0.5, 0.1/0.9, 0.9/0.1
print(entropy2(0, 1))    
print(entropy2(5, 5))    
print(entropy2(1, 9))    
print(entropy2(9, 1))