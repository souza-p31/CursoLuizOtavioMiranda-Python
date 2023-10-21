# variáveis livres + nonlocal (locals, globals)

# def fora(x):
#     a = x
#     def dentro():
#         # print(locals())
#         # print(dentro.__code__.co_freevars)
#         return a # a é considerada um variável livre, porque não está declarada dentro do escopo da função. Se usarmos a função locals vamos ver quais são as variáveis locais. Para ver as variaveis livres podemos usar __code__.co_freevars
#     return dentro

# a = fora(10)
# b = fora(20)

# print(a())
# print(b())

# print(globals()) # Usando globals podemos ver todas as variaveis globais no código

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar):
        nonlocal valor_final # Faz a função buscar o valor da variável livre em outra função.
        valor_final += valor_a_concatenar # Se fizermos assim vai dar erro. A sintaxe está correta, mas esse variavel não é desse escopo e por isso não funciona. Para contornar isso ela precisa estar nesse escopo, e para fazer isso ela não precisa nem ser global e nem local, ela tem que ser nonlocal.
        return valor_final
    return interna

a = concatenar('a')

print(a('b'))
print(a('c'))
print(a('d'))