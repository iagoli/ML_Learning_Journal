# Exercise: ex06_simple_collection_class
# Topic: 01 Python Fundamentals

""""
'----------------------------------------------------------------------------------------------
6- Defina uma classe que represente uma coleção muito simples de elementos de um qualquer
tipo, que suporte, para além das operações elementares de inserção e remoção, a consulta
do número de elementos colecionados, através da função len(), bem como a possibilidade de
ordenação dos seus elementos, sempre que não esteja em causa um conjunto heterogéneo.
Para além de permitir a inserção, a posteriori, de elementos individuais, a coleção deve poder
ser criada já com alguns elementos. De forma a simplificar a solução, a classe deve armazenar
os elementos numa lista do Python. Torne a sua coleção iterável e teste-a devidamente.
------------------------------------------------------------------------------------------------"""

from typing import Any, List, Optional, Iterable

class SimpleCollection:
    """
    A simple collection class to store elements of any type, backed by a Python list.

    Supports insertion, removal, length consultation (using len()), 
    sorting, and iteration.
    """

    def __init__(self, initial_elements: Optional[Iterable[Any]] = None):
        """
        Initializes the collection. Can optionally accept an iterable 
        (list, tuple, etc.) of initial elements.
        """
        self._elements: List[Any] = []
        
        if initial_elements is not None:
            self._elements.extend(initial_elements)


    def insert(self, item: Any) -> None:
        """Inserts a single element into the collection."""
        self._elements.append(item)

    def remove(self, item: Any) -> None:
        """
        Removes the first occurrence of a specific element.
        Raises ValueError if the item is not found.
        """
        self._elements.remove(item)
    
    def __len__(self) -> int:
        """
        Allows consulting the number of elements using the built-in len() function.
        """
        return len(self._elements)

    def __iter__(self) -> Iterable[Any]:
        """
        Makes the collection iterable, allowing use in 'for' loops.
        """
        return iter(self._elements)

    def sort_elements(self) -> None:
        """
        Sorts the elements in the collection in place.

        Raises:
            TypeError: If the collection contains heterogeneous types 
                       that cannot be compared.
        """
        self._elements.sort()


if __name__ == "__main__":
    
    print("--- 1. Testing Initialization and Length ---")
    initial_data = [50, 20, 80]
    col = SimpleCollection(initial_data)
    col.insert(10)
    col.insert(90)
    print(f"Initial elements: {list(col)}")
    print(f"Total elements (len()): {len(col)}") 

    print("\n--- 2. Testing Sorting (Homogeneous) ---")
    try:
        col.sort_elements()
        print(f"Elements after sort: {list(col)}")
    except TypeError as e:
        print(f"Sorting failed: {e}")

    print("\n--- 3. Testing Removal and Iteration ---")
    col.remove(90)
    print(f"Elements after removing 90: {list(col)}")
    print(f"New length: {len(col)}")

    print("\n--- 4. Testing Sorting with Heterogeneous Elements ---")
    hetero_col = SimpleCollection([1, "a", 3])
    print(f"Heterogeneous elements: {list(hetero_col)}")
    try:
        hetero_col.sort_elements()
        print("Sorting SUCCESSFUL (Unexpected)")
    except TypeError:
        print("Sorting FAILED as expected (TypeError: cannot compare int and str)")