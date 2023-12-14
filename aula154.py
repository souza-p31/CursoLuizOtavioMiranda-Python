"""
Classes decoradoras (Decorator Classes)
"""

class Multiplicar:
    def __init__(self, multiplicador) -> None:
        self.multiplicador = multiplicador
    
    def __call__(self, func):
        def interna(*args,**kwargs):
            resultado = func(*args,**kwargs)
            return resultado * self.multiplicador
        return interna

@Multiplicar(10)
def soma(x, y):
    return x + y

soma = soma(2, 4)
print(soma)