from models.account import Account
from models.customer import Customer

    
class Bank:
    def __init__(
            self, 
            agencies: list[int] | None=None, 
            accounts: list[Account] | None=None, 
            customers: list[Customer] | None=None) -> None:
        self.__agencies = agencies or []
        self.__accounts = accounts or []
        self.__customers = customers or []

    @property
    def agencies(self) -> list[int]:
        return self.__agencies

    @property
    def accounts(self) -> list[Account]:
        return self.__accounts
    
    @property
    def customers(self) -> list[Customer]:
        return self.__customers
    
    def _check_agency(self, account: Account) -> bool:
        if account.agency in self.__agencies:
            print('_check_agency', True)
            return True
        print('_check_agency', False)
        return False

    def _check_customer(self, customer: Customer) -> bool:
        if customer in self.__customers:
            print('_check_customer', True)
            return True
        print('_check_customer', False)
        return False

    def _check_account(self, account: Account) -> bool:
        if account in self.__accounts:
            print('_check_account', True)
            return True
        print('_check_account', False)
        return False

    def _check_account_owner(self, customer: Customer, account: Account) -> bool:
        if account is customer.account:
            print('_check_se_conta_e_do_cliente', True)
            return True
        print('_check_se_conta_e_do_cliente', False)
        return False

    def authenticate(self, customer: Customer, account: Account) -> bool:
        return self._check_agency(account) and \
            self._check_customer(customer) and \
            self._check_account(account) and \
            self._check_account_owner(customer, account)
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.__agencies!r}, {self.__customers!r}, {self.__accounts!r})'
        return f'{class_name}{attrs}'