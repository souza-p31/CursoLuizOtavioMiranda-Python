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
from abc import ABC, abstractmethod

# Conta (ABC)
#     ContaCorrente
#     ContaPoupanca
"""Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)"""

class Conta(ABC):
    def __init__(self, agencia, conta):
        self._agencia = agencia
        self._conta = conta
        self._clientes = []

    @abstractmethod
    def agencia_conta():
        ...

    @abstractmethod
    def depositar():
        ...

    @abstractmethod
    def sacar():
        ...

    @abstractmethod
    def saldo():
        ...

class ContaPoupança(Conta):
    def __init__(self, agencia, conta):
        super().__init__(agencia, conta)
        self._saldo = 0


    def agencia_conta(self):
        print(f'Ag: {self._agencia} Ct: {self._conta}')
        return


    def depositar(self, valor):
        self._saldo += valor
        print(f'Depósito de R${valor} realizado!')
        return


    def sacar(self, valor):
        self._saldo -= valor
        print(f'Saque de R${valor} realizado!')
        return

    
    def saldo(self):
        print(f'Seu saldo atual é R${self._saldo}')
        return

class ContaCorrente(Conta):
    def __init__(self, agencia, conta):
        super().__init__(agencia, conta)
        self._saldo = 100


    def agencia_conta(self):
        print(f'Ag: {self._agencia} Ct: {self._conta}')
        return


    def depositar(self, valor):
        self._saldo += valor
        print(f'Depósito de R${valor} realizado!')
        return


    def sacar(self, valor):
        self._saldo -= valor
        print(f'Saque de R${valor} realizado!')
        return

    
    def saldo(self):
        print(f'Seu saldo atual é R${self._saldo}')

    

# Pessoa (ABC)
#     Cliente
#         Clente -> Conta
# Criar classe Cliente que herda da classe Pessoa (Herança)
#     Pessoa tem nome e idade (com getters)
#     Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)

class Pessoa(ABC):
    def __init__(self, nome, idade) -> None:
         self._nome = nome
         self._idade = idade
    
class Cliente(Pessoa):
    def __init__(self, nome, idade) -> None:
        super().__init__(nome, idade)

    
    @property
    def nome(self):
        print(self._nome)
        return 
    

    @property
    def idade(self):
        print(self._idade)
        return
    

cliente_pedro = Cliente('Pedro', 21)
cliente_pedro.nome
cliente_pedro.idade
print()

conta_poupanca = ContaPoupança('1234', '654987')
conta_poupanca.agencia_conta()
print()

# Banco
#     Banco -> Cliente
#     Banco -> Conta