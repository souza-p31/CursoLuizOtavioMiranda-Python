# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(função, x):
    def executar_funcao(y):
        return função(x, y)
    return executar_funcao


somar = criar_funcao(soma, 5)
multiplicar = criar_funcao(multiplica, 10)

print(somar(2))
print(multiplicar(2))