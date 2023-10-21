# Try, except, else e finally

"""
Uma das várias regras do python é que erros não devem passar silenciosos, a menos que sejam explicitamente silenciados. Isso fala muito sobre o try e except, isso porque caso não seja usado corretamente vai silenciar todos os erros sem tratar nenhum, e isso é ruim.
"""

# a = 18
# b = 0
# c = a / b
# print(c) # Aqui naturalmente teremos um ZeroDivisionError, porque não tem como dividir nada por zero

# try:
#     a = 18
#     b = 0
#     c = a / b
# except:
#     print('Ok!') #Mas como podemos ver, já que foi colocado dentro de um try/except o erro foi silenciado e retornou o "ok!". Aqui o uso está errado, o correto é tratar cada caso em um except diferente, e caso queira generalizar usar um except junto do exception que é o top erro que serve para todos.

# try:
#     a = 18
#     b = 2
#     c = a / b   
# except ZeroDivisionError:
#     print('Dividiu por zero')
# except TypeError: # tentei dividir 18 por uma string
#     print('Erro de tipo')
# except IndexError: # Tentei iterar um indice que não existe
#     print('Erro de indice')
# except (TypeError, IndexError): # Se colocar dentro de uma tupla é possível tratar mais de um erro por vez
#     print('Erro de indice ou de tipo')
# except Exception: #Agora todos os erros que forem dar e não tiverem sido tratados antes vão cair aqui
#     print('Erro desconhecido')

# print("Continua")

# try:
#     a = 18
#     b = 0
#     c = a / b   
# except ZeroDivisionError as error: # É possível colocar alias (as) nos erros
#     # print(error) # Vai imprimir o nome do erro

# try:
#     a = 18
#     b = 0
#     c = a / b   
# except ZeroDivisionError as error:
    # print(error.__class__.__name__) # Aqui chamamos a classe e em seguida chamamos apenas o nome, só para ver que é isso que aconteceu no exemplo anterior, só que de forma mais simples. O Python foi programado para ser assim.

# Esses casos são interessantes para caso a gente queira tratar mais de um erro de uma vez só, mas que mostre qual erro foi:

try:
    a = 18
    b = 'a'
    c = a / b   
except (TypeError, IndexError) as e:
    print('Erro de tipo ou de index')
    print('mensagem:',e) # nome erro
    print(e.__class__.__name__) # Nome da Classe do erro