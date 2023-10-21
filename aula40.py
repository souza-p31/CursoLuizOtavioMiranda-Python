""" Calculadora com while """

print(f'{"~"*5} Calculadora com WHILE {"~"*5}')

while True:
    print('\nDigite os valores que deseja calcular e em seguida informe o operador aritmetico\n')
    
    sair = str(input('Deseja [S]air? ')).upper()[0]
    if sair == 'S':
        break

    n1 = input('Primeiro número: ')
    n2 = input('Segundo número: ')
    operador = input('Qual operador? [+][-][*][/] ')[0]
    resultado = None
    numeros_validos = None
    operadores_validos = '+-*/'

    try:
        n1_float = float(n1)
        n2_float = float(n2)
        numeros_validos = True
    except:
        print('Um dos valores é inválido')
        continue

    if operador not in operadores_validos:
        print('Operador inválido.')
        continue
    
    if operador == '+':
        resultado = n1_float + n2_float
    elif operador == '-':
        resultado = n1_float - n2_float
    elif operador == '*':
        resultado = n1_float * n2_float
    elif operador == '/':
        resultado = n1_float / n2_float
    print(f'{resultado=}')

