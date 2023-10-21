# Decoradores com parâmetros

# def fabrica_de_funcoes(func):
#     print('Decoradora 1')
    
#     def aninhada(*args,**kwargs):
#         print('Aninhada')
#         res = func(*args, **kwargs)
#         return res
#     return aninhada

# def soma(x, y):
#     return x + y

# # dez_mais_cinco = fabrica_de_funcoes(soma) # A função decoradora executa o que tem dentro dela e armazena a função decorada, que no caso é soma.
# # soma_dez_mais_cinco = dez_mais_cinco(10, 5) # Quando executamos a função interna ela executa o que tem dentro dela e armazena o resultado da função decorada
# # print(soma_dez_mais_cinco) # Se imprimirmos a função interna, ela vai ter guardado o retorno da função decorada. Essa estrutura serve para adicionar mais passos a execução caso haja necessidade, mas para fazer isso não é necessário usar toda essa estrutura, podemos fazer de uma forma mais simples.

# # print('---------------------------------------')

# # def fabrica_de_funcoes(func):
# #     print('Decoradora 1')
    
# #     def aninhada(*args,**kwargs):
# #         print('Aninhada')
# #         res = func(*args, **kwargs)
# #         return res
# #     return aninhada

# # @fabrica_de_funcoes # Se colocarmos @ e o nome da função decoradora ela já ira executar e armazenar nossa função decorada, tirando a necessidade de criar uma variavel para isso.
# # def soma(x, y):
# #     return x + y

# # dez_mais_cinco = soma(10, 5) # aqui quando chamamos a função decorada ela executou a função interna e retornou a função decorada, tanto que se imprimirmos o resultado da soma vai estar lá.
# # print(dez_mais_cinco)

# print('---------------------------------------')
# Podemos ainda adicionar mais um nível para atrasar mais ainda a execução

def decoradora(funcao):
    def wrapper(*args):
        print(f'Vou realizar uma {funcao.__name__}')
        print(f'O resultado da {funcao.__name__} foi: {funcao(*args)}')
        print(f'{funcao.__name__} realizada')
    return wrapper


@decoradora
def soma(x, y):
    return x + y

@decoradora
def multiplica(x, y):
    return x * y

multiplica(2, 5)