"""
Exercício com classes

1 - Crie uma classe Carro (nome)
2 - Crie uma classe Motor (nome)
3 - Crie uma classe Fabricante (nome)
4 - Faça a ligação entre carro tem um Motor
Obs.: Um motor pode ser de vários carros
5 - Faça a ligação entre Carro e um Fabricante
Obs.: Um fabricante pode fabricar vários carros

Exiba o nome do carro, motor e fabricante na tela
"""

class Carro:
    def __init__(self, nome):
        self._nome = nome
        self._motor = None
        self._fabricante = None


    @property
    def motor(self):
        return self._motor
    

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    
    @property
    def fabricante(self):
        return self._fabricante
    

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor
    # def inserir_motor(self, motor):
    #     self.motor = motor.nome


    # def inserir_fabricante(self, fabricante):
    #     self.fabricante = fabricante.nome


    def informacoes(self):
        print(f'Nome: {self._nome}\nMotor: {self._motor.nome}\nFabricante: {self._fabricante.nome}')


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


carro1 = Carro('Fox')
carro2 = Carro('Fusca')
motor1 = Motor('1.6')
fabricante1 = Fabricante('Volkswagem')

carro1.motor = motor1
carro1.fabricante = fabricante1
carro1.informacoes()

# carro1.inserir_motor(motor1)
# carro1.inserir_fabricante(fabricante1)
# carro1.informacoes()
# print('-'*10)

# carro2.inserir_motor(motor1)
# carro2.inserir_fabricante(fabricante1)
# carro2.informacoes()
# print('-'*10)

# carro1.motor = motor1.nome
# carro1.fabricante = fabricante1.nome
# carro1.informacoes()