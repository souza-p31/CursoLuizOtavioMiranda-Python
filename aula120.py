"""
Introdução ao método __init__ (inicializador de atributos)
class - classes são moldes para criar novos objetos
As classes geram novos objetos (instâncias) que podem ter seus proprios atributos e métodos.

Os objetos gerados pelas classes podem usar seus dados
internos para realizar várias ações.

Por convenção, usamos PascalCase para nomes de classes.
"""

# string = 'Luiz' # str
# print(string.upper())
# print(isinstance(string, str))

"""Uma das primeiras coisas a ser executada na classe é o __init__ para inicializar os atributos. Dentro das classes as defs não são funções, são atributos. O __init__ recebe como primeiro parametro o self, já que a classe é um molde para criação de objetos, o self vai fazer a classe se referenciar a ela mesma. Como fizemos antes em inicializar a classe com

p1 = Pessoa()

e depois criar os métodos com 

p1.nome = 'Luiz'
p1.sobrenome = 'Otavio'

vai acontecer a mesma coisa dentro da classe usando o self.
"""
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Luiz', 'Otávio')
# p1.nome = 'Luiz'
# p1.sobrenome = 'Otavio'

p2 = Pessoa('Maria', 'Joana')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)