from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, agency: int, number: str, balance: float) -> None:
        super().__init__()
        self._agency = agency
        self._number = number
        self._balance = balance

    @property
    def agency(self) -> int:
        return self._agency
    
    @property
    def number(self) -> str:
        return self._number
    
    @property
    def balance(self) -> float:
        return self._balance

    @property
    def deposit(self, amount: float) -> None:
        self._balance += amount

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        ...

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self._agency!r}, {self._number!r}, {self._balance!r})'
        return f'{class_name}{attrs}'