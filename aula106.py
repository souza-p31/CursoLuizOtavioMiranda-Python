# Ordem dos decoradores

def parametros_decorador(nome):
    def decorador(func):
        print('Decorador:', nome)

        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador

@parametros_decorador('3')
@parametros_decorador('2')
@parametros_decorador('1')
def soma(x, y):
    return x + y

a = soma(1, 2)
print(a)