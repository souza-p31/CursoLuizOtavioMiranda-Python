"""
Herança simples - Relações entre classes

Associação - usa (uma classe usa a outra. Ex.:
Classe pintor usa Classe ferramenta)

Composição - É dono de (uma classe passa a ser dona da outra classe no próprio escopo,
e se ela for deletada a outra também será)

Herança - É um (uma classe pai da origem a uma classe filho, então a relação entre as
duas é bem mais fortre do que a de uma composição)

Herança VS Composição

Classe principal (Pessoa)
    -> super class, base class, parent class
Classes filhas (Cliente)
    -> sub class, child class, derived class

A herança também pode servir para generalizar um objeto para que ele possa ser reaproveitado, 
Ex.: Classe cliente é muito expecifico, então vou extender/generalizar para Pessoa, porque
todo cliente é uma pessoa. O contrário também é possível, tornando um objeto mais especifico.
"""

class Pessoa:
    cpf = '1234'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    
    def falar_nome_classe(self):
        print('Classe PESSOA')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('Classe CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa):
    cpf = 'cpf aluno'


c1 = Cliente('Luiz', 'Otávio')
c1.falar_nome_classe()
a1 = Aluno('Maria', 'Helena')
a1.falar_nome_classe()
print(a1.cpf)

help(Cliente)

"""
Method resoluion order é a ordem em que a informação será
buscada. No caso de Cliente, se for um metodo "falar_nome_classe"
primeiro sera buscada em Cliente, depois em Pessoa e por fim em
builtins.object que é um objeto que já vem com o Python, que todas
as novas classes são filhas dele (ou seja, herdam dele).
"""