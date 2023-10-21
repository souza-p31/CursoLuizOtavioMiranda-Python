"""
Exercício - salve sua classe em Json
Salve os dados da sua classe em Json
e depois crie novamente as instâncias
da classe com os dados salvos
Faça em arquivos separados
"""

# import json


# class Pessoa:
#     def __init__(self, nome, idade, altura, peso):
#         self.nome = nome
#         self.idade = idade
#         self.altura = altura
#         self.peso = peso
    

#     def registro(self):
#         return f'Nome: {self.nome}, idade: {self.idade}, altura: {self.altura} e peso: {self.peso}'

# with open('aula127a.json', 'r', encoding='utf-8') as arquivo:
#     dados = json.load(arquivo)

# pessoa = Pessoa(dados['nome'], dados['idade'], dados['altura'], dados['peso'])
# print(pessoa.registro())

import json
from aula127a import CAMINHO_ARQUIVO, Pessoa

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    pessoa1 = Pessoa(**pessoas[0])
    pessoa2 = Pessoa(**pessoas[1])
    pessoa3 = Pessoa(**pessoas[2])

    print(pessoa1.registro())
    print(pessoa2.registro())
    print(pessoa3.registro())

print(__name__)