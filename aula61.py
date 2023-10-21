"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = '74682489070'
nove_digitos = cpf[:9]
contador = 10
resultado = 0

for digito in nove_digitos:
    resultado += int(digito) * contador
    contador -= 1

pdigito = (resultado * 10) % 11
pdigito = pdigito if pdigito <= 9 else 0
print(pdigito)

# multiplicador = 10
# for c in cpf:
#     if multiplicador >= 2:
#         conversao_str_int = int(c)
#         multiplicacao = conversao_str_int * multiplicador
#         conversao_int_str = str(multiplicacao)
#         validacao1.append(conversao_int_str)
#         multiplicador -= 1
#     else:
#         break

"""Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7"""

# soma = 0
# for d in validacao1:
#     conversao_str_int = int(d)
#     soma += conversao_str_int

# soma *= 10
# resultado = soma % 11
# resultado = resultado if resultado <= 9 else 0 
# print(resultado)
