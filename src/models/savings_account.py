from models.account import Account

class SavingsAccount(Account):
    def __init__(self, agency: str, number: str, balance: float=0) -> None:
        super().__init__(agency, number, balance)

    def withdraw(self, amount: float) -> None:
        if self._balance - amount < 0:
            print('Não foi possível sacar o valor desejado')
        else:
            self._balance -= amount
