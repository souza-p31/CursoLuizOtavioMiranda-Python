"""
Relações entre classes: associação, agregação e composição
Composição é uma especialização da agregação.
Mas nela, quando o objeto "pai" for apagado, todas as referências dos objetos filhos também são apagadas.

Na prática, quando declaramos duas classes uma delas se torna "pai", e a classe filho irá compor o escopo da classe pai. Dessa forma quando o pai for apagado o filho também será já que está no escopo dele.

Sempre que um código termina o Python executa o método __del__ para limpar o que estava armazenado na memoria, vamos imprimir no terminal o momento em que ele faz isso para ver que de fato se a classe pai deixar de existir as outras irão.
"""

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    
    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    
    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    
    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)


    def __del__(self):
        print('Apagando,', self.nome)

    
class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
    

    def __del__(self):
        print('Apagando,', self.rua, self.numero)


cliente1 = Cliente('Pedro')
cliente1.inserir_endereco('Av Rio Branco', 1)
cliente1.inserir_endereco('Av Cesário de Melo', 199)
endereco_externo = Endereco('Av Saudade', 5641)
cliente1.inserir_endereco_externo(endereco_externo)
cliente1.listar_enderecos()

del cliente1

print(endereco_externo.rua, endereco_externo.numero)

