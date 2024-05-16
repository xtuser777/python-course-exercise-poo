"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

from models.current_account import CurrentAccount
from models.savings_account import SavingsAccount
from models.customer import Customer
from models.bank import Bank


if __name__ == '__main__':
    c1 = Customer('Luiz', 30)
    cc1 = CurrentAccount(111, 222, 0, 0)
    c1.conta = cc1
    c2 = Customer('Maria', 18)
    cp1 = SavingsAccount(112, 223, 100)
    c2.conta = cp1
    banco = Bank()
    banco.customers.extend([c1, c2])
    banco.accounts.extend([cc1, cp1])
    banco.agencies.extend([111, 222])

    if banco.authenticate(c1, cc1):
        cc1.deposit(10)
        c1.account.deposit(100)
        print(c1.account)

    