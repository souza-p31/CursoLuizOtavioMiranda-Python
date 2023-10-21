# try, except, else e finally

try: # Nunca pode estar sozinho
    print('Abrir arquivo')
    8/0
    # 8/1
except ZeroDivisionError: # Trata as exceções
    print('Dividiu por zero')
else: # Caso não dê erro, ele é executado
    print('Não deu erro')
finally: # Sempre vai ser executado, independente de qualquer coisa
    print('Fechar arquivo')

print()

try: # Nunca pode estar sozinho
    print('Abrir arquivo')
    # 8/0
    8/1
except ZeroDivisionError: # Trata as exceções
    print('Dividiu por zero')
else: # Caso não dê erro, ele é executado
    print('Não deu erro')
finally: # Sempre vai ser executado, independente de qualquer coisa
    print('Fechar arquivo')