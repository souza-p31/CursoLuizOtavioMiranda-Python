"""
Atributos de classe

Digamos que em algum contexto a gente precise se um valor disponível em todo o escopo da classe, é o caso do atributo de classe. Podemos criar no corpo da classe, fora dos métodos para poder acessar de qualquer método. Só precisamos tomar cuidado quando for chamar esse atributo da classe, porque existem duas formas:

Usando o Self, mas caso exista outro atributo com o mesmo nome vai ser considerado primeiro o do método.

Chamando a classe junto do atributo, mas pode ser modificado durante a execução do código.
"""

class Pessoa:
    ano_atual = 2023


    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 1000
    
    def ano_nascimento(self):
        return self.ano_atual - self.idade
    

p1 = Pessoa('João', 35)
print(p1.ano_nascimento()) # 965 por conta do self.ano_atual = 1000


class Pessoa:
    ano_atual = 2023


    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 1000
    
    def ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    

p1 = Pessoa('João', 35)
print(p1.ano_nascimento()) # 1988, mesmo com o self.ano_atual o resultado não é alterado.

Pessoa.ano_atual = 1000

print(p1.ano_nascimento()) # Porém pode ser modificado ao longo do código.