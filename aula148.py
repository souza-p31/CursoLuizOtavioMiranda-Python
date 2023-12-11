"""
__new__ e __init__ em classes Python

__new__ é o método responsável por criar e retornar
o novo objeto. Por isso, new recebe cls.

__new__ DEVE retornar o novo objeto

__init__ é o método responsável por inicializar a
instância. Por isso, init recebe self.

__init__ NÃO DEVE retornar nada (None)

object é a super classe de uma classse
"""

class A:
    def __new__(cls, *args, **kwargs):
        print('Antes da criação')
        instancia = object.__new__(cls)
        print('Depois da criação')
        return instancia

    def __init__(self, x) -> None:
        self.x = x
        print('Sou o init')

    def __repr__(self) -> str:
        return 'A()'
    
a = A(123)
print(a.x)