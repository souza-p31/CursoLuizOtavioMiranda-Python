"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""numero = input('Insira um número: ')

if numero.isnumeric():
    if int(numero) % 2 == 0:
        print('PAR')
    else:
        print('ÍMPAR')
else:
    print('Não é um número inteiro')
"""


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""hora = int(input('Que horas são agora? '))
mensagem = ...

if 0 <= hora <= 11:
    mensagem = 'Bom dia!'
elif 12 <= hora <= 17:
    mensagem = 'Boa tarde!'
elif 18 <= hora <= 23:
    mensagem = 'Boa noite!'
else:
    mensagem = 'Hora inválida'

print(mensagem)"""

hora = input('Que horas são agora? ')

try:

    hora_int = int(hora)

    if hora_int >= 0 and hora_int <= 11:
        print('Bom dia')
    elif hora_int >= 12 and hora_int <= 17:
        print('Boa tarde')
    elif hora_int >= 18 and hora_int <= 23:
        print('Boa noite')
    else:
        print('Não conheço essa hora')
except:
    print('Não entendi')


    
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

"""nome = str(input('Qual é o seu nome? '))
tam_nome = len(nome)
mensagem = ...

if tam_nome <= 4:
    mensagem = 'Nome curto'
elif 5 <= tam_nome <= 6:
    mensagem = 'Nome normal'
elif tam_nome > 6:
    mensagem = 'Nome grande'

print(mensagem)"""