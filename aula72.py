"""
Exercício com funções

Crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variável e mostre o valor
da variável.
"""

def multiplicador(*args):
    produto = 1
    for numero in args:
        print(f'{produto} * {numero} = ', end='' )
        if numero == 0:
            numero = 1
        produto *= numero
        print(produto)
    return produto

multiplicacao = multiplicador(3, 7, 9, 3, 1)
print(f'O resultado da multiplicação é {multiplicacao}')


# Cria uma função fala se um número é par ou ímpar.
# Retorne-se o número é par ou ímpar.
 
def parouimpar(numero):
    if numero % 2 == 0:
        return 'Par'
    return 'Ímpar'


consulta = parouimpar(multiplicacao)
print(f'\nO número {multiplicacao} é {consulta}')

print(parouimpar(10))
print(parouimpar(51))
print(parouimpar(90))