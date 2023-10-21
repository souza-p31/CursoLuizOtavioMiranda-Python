"""
Métodos em instâncias de classes Python
Hard coded - é algo que foi escrito diretamente no código

Entendendo self em classes Python
Classe - Molde (geralmente sem dados)
Instância da class (objeto) - Tem os dados
Uma classe pode gerar várias instâncias
Na classe o self é a própria instância

Todo primeiro parâmetro de um método vai ser o self, mesmo que o nome que ele receba não seja esse.

Criamoso 'Molde' com o class, esse molde tem um nome e recebe parâmetros (caracteristicas) e o objeto criado usando esse molde vai poder executar ou não ações com base nas caracteristicas dele.
"""

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro('Celta')
print(celta.nome)
celta.acelerar()