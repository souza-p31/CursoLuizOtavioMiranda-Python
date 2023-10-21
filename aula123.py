"""
Escopo da classe e métodos da classe

o self permite os métodos acessarem o escopo da classe e de outros métodos, sem ele os dados ficam restritos ao escopo do próprio método.
"""

class Animal:
    
    
    def __init__(self, nome):
        self.nome = nome
        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'
    
    
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)
    
leao = Animal(nome='Leão')
print(leao.nome)
print(leao.comendo('banana'))
print(leao.executar('maça'))