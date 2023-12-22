"""
dataclasses - o que são dataclasses?

O módulo dataclasses fornece um decorador
e funções para criar métodos como
__init__(), __repr__(), __eq__() (entre outros)
em classes definidas pelo usuário.

Em resumo: dataclasses são syntax sugar para
criar classes normais.

Foi descrito na PEP 557 e adicionado na versão
3.7 do Python.
Doc: https://docs.python.org/3/library/dataclasses.html
"""
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    
    @nome_completo.setter
    def nome_completo(self, valor):
        nome, sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Pedro', 'Souza')
print(p1.nome_completo)
p1.nome_completo = 'Luiz Otávio'
print(p1.nome_completo)
print('------------------')


# o post init é um metodo magico que executa logo
# apos o init, porém se informarmos a dataclass que
# queremos definir o init, ele não irá funcionar

# é possível desativar várias coisas no dataclass, 
#só olhar na documentação (init, repr, frozen e tal)

@dataclass(init=False)
class Pessoa:
    nome: str
    sobrenome: str

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    
    @nome_completo.setter
    def nome_completo(self, valor):
        nome, sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = sobrenome
    
    def __post_init__(self):
        print('post init')

p1 = Pessoa('Pedro', 'Souza')
print(p1)