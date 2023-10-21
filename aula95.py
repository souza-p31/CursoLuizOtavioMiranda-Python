# Raise - lançando exceções (erros)

# De certa forma, é bom quando nosso código retorna um erro, porque desse jeito sabemos onde temos que corrigir. Seguindo essa linha de raciocinio, o raise faz algo parecido:

# def divide(n, d):
#     return n / d

# a = divide(2, 0) # Essa função vai retornar um erro de divisão, porque estou tentando dividir por zero.
# print(a)


# Aqui o raise funciona semelhante aos erros comuns que já acontecem, porque foi programado para funcionar assim. A principio podemos usar as classes de erros que já existem, e modificar suas mensagens, mas se for necessário podemos criar novos erros.

# Isso é importante para mostrar onde estamos errando ou quem for dar manutenção no código está errando.

# def divide(n, d):
#     if d == 0:
#         raise ZeroDivisionError('Você está tentando dividir por 0')

# a = divide(2, 0)
# print(a)

def int_ou_float(n):
    if not isinstance(n, (float, int)):
        raise TypeError('O número deve ser int ou float')
    return True

def divide(n, d):
    check = int_ou_float(n)
    if check:
        return n / d

a = divide('1', 2) # Retorna erro porque caiu na função de verificação e o raise dela retornou um erro que definimos.
print(a)