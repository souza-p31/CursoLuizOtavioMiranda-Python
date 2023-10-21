"""
__dict__ e vans para atributos de instâncias

Os parametros e valores da classe precisam ficar armazenados em algum lugar, podemos acessar esse lugar usando __dict__ ou vars, ambos fazem a mesma coisa.
"""

class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

p1 = Pessoa('João', 35)
print(p1.get_ano_nascimento())
print(p1.__dict__) #Os valores dos parametros da classe estão ali e organizados como dict
print(vars(p1)) #vars faz a mesma coisa que __dict__

#Podemos modificar os valores, ou adicionar mais valores, como por exemplo

p1.__dict__['nome'] = 'Pedro'
p1.__dict__['Novo'] = 'Item novo'
print(p1.__dict__) #trocamos o nome e adicionamos mais um elemento.