"""
Exercício - salve sua classe em Json
Salve os dados da sua classe em Json
e depois crie novamente as instâncias
da classe com os dados salvos
Faça em arquivos separados
"""

import json

CAMINHO_ARQUIVO = 'aula127a.json'

class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
    

    def registro(self):
        return f'Nome: {self.nome}, idade: {self.idade}, altura: {self.altura} e peso: {self.peso}'


pessoa1 = Pessoa('Pedro', 20, 1.70, 72.00)
pessoa2 = Pessoa('Evaristo', 41, 1.74, 87.70)
pessoa3 = Pessoa('Nintendo Switch', 92, 1.51, 154.60)
bd = [pessoa1.__dict__, pessoa2.__dict__, pessoa3.__dict__]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        json.dump(bd, arquivo, indent=2, ensure_ascii=False)
    return

if __name__ == '__main__':
    print('fazendo dump')
    fazer_dump()

print(__name__)

