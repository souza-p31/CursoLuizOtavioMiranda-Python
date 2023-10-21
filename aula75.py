"""
Exercícios
Crie funções que duplicam, triplicam e quadruplicam
O número recebido como parâmetro
"""

# def multiplicar(numero, fator):
#     return numero * fator

# duplicar = multiplicar(4, 3)
# print(duplicar)

# def multiplicador(multiplicador):
#     def multiplicar(numero):
#         return numero * multiplicador
#     return multiplicar

# duplicar = multiplicador(2)
# print(duplicar(3))

def multiplicar(multiplicador):
    def numero(fator):
        return multiplicador * fator
    return numero

duplicar = multiplicar(2)
print(duplicar(1))
