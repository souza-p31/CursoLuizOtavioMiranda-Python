"""
super() e a sobreposição de membros - Python Orientado a Objetos

classe Principal(Pessoa)
    -> super class, base class, parent class

classes Filhas(Cliente)
    -> sub class, child class, derived class
"""


# class MinhaString(str):
#     def upper(self):
#         print('Chamou upper')
#         retorno = super(MinhaString, self).upper()
#         print('Depois do upper')
#         return retorno

# a = MinhaString('Pedro')
# print(a.upper())

class A(object):
    atributo_a = 'valor a'
    
    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')
    

class C(B):
    atributo_c = 'valor c'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def metodo(self):
        print('C')


print(C.mro())
print(B.mro())
print(A.mro()) # metodo mro mostra o method resolution order


c = C('Atributo', 'Qualquer')
print(c.atributo)
print(c.outra_coisa)
print()
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()