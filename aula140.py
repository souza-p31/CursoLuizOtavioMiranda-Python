"""
Herança múltipla - Python Orientado a Objetos

Quer dizer que no Python, uma classe pode estender
várias outras classes.

Herança simples:
Animal -> Mamífero -> Humano -> Pessoa -> Cliente

Herança múltipla e mixins:
Log -> Filelog
Animal -> Mamífero -> Humano -> Pessoa -> Cliente
Cliente(Pessoa, Filelog)

A, B, C, D
D(B, C) - C(A) - B(A) - A

método -> falar
           A
         /   \
        B     C
         \   /
           D

Python3 usa c3 superclass linearization para gerar o mro.

Vocẽ não precisa estudar isso (é complexo)
https://en.wikipedia.org/wiki/C3_linearization

Para saber a ordem de chamada dos métodos
Use o método de classe classe.mro()
ou o atributo __mro__ (Dunder - Double Underscore)
"""

class A:
    ...

    def quem_sou(self):
        print('A')

class B(A):
    ...

    # def quem_sou(self):
    #     print('B')

class C(A):
    ...

    # def quem_sou(self):
    #     print('C')

class D(B, C):
    ...

    # def quem_sou(self):
    #     print('D')


d = D()
d.quem_sou()
print(D.__mro__)
# print(D.mro())

"""
O C3 superclass linearization é um algoritmo complexo
que vai fazer a escolha de como o mro vai se comportar.
Usando o método mro() ou a propriedade __mro__ 
conseguimos ver esse comportamento, então não é necessario
entender como esse algoritmo complexo funciona.

Aqui vemos que, D que herdou de B e C (nessa ordem), primeiro
buscou no proprio escopo, depois em B e depois em C, mas
se mudarmos a ordem das heranças, ele irá buscar em C
primeiro. Caso não encontre o método em nenhum dos dois
irá buscar em A, que é de quem B e C herdaram o método.
"""