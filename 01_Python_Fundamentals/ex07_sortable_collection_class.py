# Exercise: ex07_sortable_collection_class
# Topic: 01 Python Fundamentals

#-----------------------------------------------------------------------------------------------
# 7- Guarde na coleção que definiu no exercício anterior instâncias de uma classe criada por si e
# tente ordená-la. Se essa operação falhar, aperfeiçoe a definição da coleção, tratando
# devidamente esse erro. Posteriormente, torne as instâncias da sua classe ordenáveis.
#-----------------------------------------------------------------------------------------------

from typing import Any, List, Optional, Iterable
from functools import total_ordering

class SimpleCollection:
    """
    A simple collection class, improved to handle sorting errors.
    
    Supports basic list operations, len(), iteration, and attempts sorting 
    with custom error handling for non-comparable elements.
    """

    def __init__(self, initial_elements: Optional[Iterable[Any]] = None):
        self._elements: List[Any] = []
        if initial_elements is not None:
            self._elements.extend(initial_elements)

    def insert(self, item: Any) -> None:
        """Inserts a single element."""
        self._elements.append(item)

    def remove(self, item: Any) -> None:
        """Removes the first occurrence of an element."""
        self._elements.remove(item)

    def __len__(self) -> int:
        """Allows use of len()."""
        return len(self._elements)

    def __iter__(self) -> Iterable[Any]:
        """Makes the collection iterable."""
        return iter(self._elements)

    def sort_elements(self) -> None:
        """
        Sorts the elements, catching TypeError if objects are not comparable,
        as required by the exercise.
        """
        try:
            self._elements.sort()
            print("Sorting successful.")
        except TypeError as e:
     
            print(f"Error caught: {e}")
            print("Sorting failed: Elements are not mutually comparable or missing comparison methods.")



@total_ordering
class ComparablePerson:
    """
    Represents a person and implements comparison methods (__lt__ and __eq__) 
    to make instances sortable (ordenável) based on age.
    """
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        """Standard representation for printing."""
        return f"Person(Name='{self.name}', Age={self.age})"

    def __lt__(self, other: Any) -> bool:
        """Defines the 'less than' (<) operator, primarily by age."""
        if not isinstance(other, ComparablePerson):
            return NotImplemented
        return self.age < other.age

    def __eq__(self, other: Any) -> bool:
        """Defines the 'equal to' (==) operator, checking both name and age."""
        if not isinstance(other, ComparablePerson):
            return NotImplemented
        return (self.age == other.age) and (self.name == other.name)




if __name__ == "__main__":
    
    print("\n--- TEST 1: Sorting Failure (Heterogeneous Types) ---")
    failure_col = SimpleCollection([10, "apple", 5])
    failure_col.sort_elements()
    
    print("\n--- TEST 2: Successful Sorting (Custom Objects) ---")
    
    final_col = SimpleCollection([
        ComparablePerson("Zoe", 28),
        ComparablePerson("Anna", 20),
        ComparablePerson("John", 19)
    ])
    
    print(f"Before sort (by age): {list(final_col)}")
    final_col.sort_elements()
    print(f"After sort (by age): {list(final_col)}")