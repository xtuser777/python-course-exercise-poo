from models.account import Account

class CurrentAccount(Account):
    def __init__(self, agency: str, number: str, balance: float=0, limit: int=0) -> None:
        super().__init__(agency, number, balance)
        self.__limit = limit

    def withdraw(self, amount: float) -> None:
        if self._balance - amount < (-self.__limit):
            print('Não foi possível sacar o valor desejado')
            print(f'Seu limite é {-self.limite:.2f}')
        else:
            self._balance -= amount