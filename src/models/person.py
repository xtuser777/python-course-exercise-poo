# from abc import ABC, abstractmethod


# class Person(ABC):
#     def __init__(self, name: str, age: int) -> None:
#         super().__init__()
#         self._name = name
#         self._age = age

#     @property
#     def name(self) -> str:
#         return self._name
    
#     @name.setter
#     def name(self, name) -> None:
#         self._name = name

#     @property
#     def age(self) -> int:
#         return self._age
    
#     @age.setter
#     def age(self, age) -> None:
#         self._age = age
    
#     def __repr__(self):
#         class_name = type(self).__name__
#         attrs = f'({self.name!r}, {self.age!r})'
#         return f'{class_name}{attrs}'

from dataclasses import dataclass

@dataclass
class Person:
    name: str = ''
    age: int = 0