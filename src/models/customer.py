from models.person import Person
from models.account import Account


class Customer(Person):
    def __init__(self, name: str, age: int, account: Account=None) -> None:
        super().__init__(name, age)
        self.__account = account

    @property
    def account(self) -> Account:
        return self.__account