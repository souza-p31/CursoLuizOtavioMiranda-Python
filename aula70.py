"""
Retorno de valores das funções (return)
"""


def soma(x, y):
    return x + y
    print(1+1) # Não vai ser executado porque return fecha a função

def soma(x, y):
    print('Olha')
    print('só')
    print('que')
    print('legal')
    return x + y
    print(1+1) # Não vai ser executado porque return fecha a função

def soma(x, y):
    if x > 10:
        return 10
    return x + y # Não é necessário Else, porque caso If não
                # seja verdadeiro, a outra linha do código irá executar de qualquer forma


# variavel = soma(1,2)
# variavel = int('1')
soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1+ soma2)
print(soma(11, 55)) # Retorno se mantém, porque a função já foi executada

soma3 = soma(9, 55)
print(soma3)
