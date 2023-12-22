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
# Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
#     ContaCorrente deve ter um limite extra
#     Contas têm agência, número da conta e saldo
#     Contas devem ter método para depósito
#     Conta (super classe) deve ter o método sacar abstrato (Abstração e
#     polimorfismo - as subclasses que implementam o método sacar)

class Conta(ABC):
    def __init__(self, agencia, conta) -> None:
        self._agencia = agencia
        self._conta = conta
        self._saldo = 0

    @abstractmethod
    def depositar(self, valor):
        ...

    @abstractmethod
    def sacar(self, valor):
        ...

    @abstractmethod
    def saldo(self):
        ...

class ContaPoupanca(Conta):
    def __init__(self, agencia, conta):
        super().__init__(agencia, conta)


    def depositar(self, valor):
        print(f'Deposito de R${valor} realizado!')
        self._saldo += valor
        return
    

    def sacar(self, valor):
        print(f'Saque de R${valor} realizado!')
        self._saldo -= valor
        return
    

    def saldo(self):
        print(f'Seu saldo é R${self._saldo}')
        return 

class ContaCorrente(Conta):
    def __init__(self, agencia, conta):
        super().__init__(agencia, conta)
        self._saldo = 150


    def depositar(self, valor):
        print(f'Deposito de R${valor} realizado!')
        self._saldo += valor
        return
    

    def sacar(self, valor):
        print(f'Saque de R${valor} realizado!')
        self._saldo -= valor
        return


    def saldo(self):
        print(f'Seu saldo é R${self._saldo}')
        return 
    

    
    # Pessoa (ABC)
#     Cliente
#         Clente -> Conta
# Criar classe Cliente que herda da classe Pessoa (Herança)
#     Pessoa tem nome e idade (com getters)
#     Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade


    @property
    def nome(self):
        return self._nome
    

    @property
    def idade(self):
        return self._idade
    
class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
# Banco
#     Banco -> Cliente
#     Banco -> Conta
# Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
# Banco será responsável autenticar o cliente e as contas da seguinte maneira:
#     Banco tem contas e clentes (Agregação)
#     * Checar se a agência é daquele banco
#     * Checar se o cliente é daquele banco
#     * Checar se a conta é daquele banco
# Só será possível sacar se passar na autenticação do banco (descrita acima)
# Banco autentica por um método.

class Banco:
    def __init__(self, nome, cliente, conta) -> None:
        self._nome = nome
        self._cliente = cliente
        self._conta = conta
        self._agencias = []
        self._contas = []
        self._clientes = []

    def cadastrar_cliente(self):
        cliente_novo = self._cliente
        self._clientes.append(cliente_novo.nome)
        print(f'{cliente_novo.nome} cadastrado com sucesso!')
        return cliente_novo
    
    def cadastrar_conta(self):
        self._agencias.append((self._conta._agencia))
        self._contas.append((self._conta._conta))
        print(f'Conta nova cadastrada com sucesso!\nAg: {self._conta._agencia} Ct: {self._conta._conta}')
        return
    

    def depositar(self, valor, agencia, conta, nome):
        if agencia in self._agencias and conta in self._contas and nome in self._clientes:
            self._conta.depositar(valor)
        else:
            print('Acesso negado!')

    def sacar(self, valor, agencia, conta, nome):
        if agencia in self._agencias and conta in self._contas and nome in self._clientes:
            self._conta.sacar(valor)
        else:
            print('Acesso negado!')

    def saldo(self, agencia, conta, nome):
        if agencia in self._agencias and conta in self._contas and nome in self._clientes:
            self._conta.saldo()
        else:
            print('Acesso negado!')
    

cliente_mirella = Cliente('Mirella', 15)

conta_corrente_mirella = ContaCorrente('1234','5678')

banco_nubank = Banco('Nubank', cliente_mirella, conta_corrente_mirella)

banco_nubank.cadastrar_cliente()
banco_nubank.cadastrar_conta()

conta_corrente_mirella.depositar(9999999999)
conta_corrente_mirella.sacar(8)
conta_corrente_mirella.saldo()