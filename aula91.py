# Introdução às generator functions em Python
# generator = (n for n in range(1000000))


# return para a execuçao e retorna
# def generator(n=0):
#     return 1  

# yield faz uma pausa e retorna 
def generator(n=0):
    yield 1 # pausa
    return 'acabou' # aqui o return funciona como um stopiteration

# gen = generator()
# print(next(gen))
# print(next(gen)) # aqui levanta o stopinteration porque acabaram os iteraveis

# def generator(n=0, maximo= 10):
#     yield 1
#     print('mais um')
#     yield 2
#     print('mais dois')
#     yield 3
#     print('mais tres')
#     return 'acabou'

# gen = generator()
# print(next(gen))
# print(next(gen)) 
# print(next(gen)) # ele vai pausando até acabarem os itens e retornar o stopinteration

# no caso se fossemos fazer isso com um numero grande, poderiamos fazer assim:

def generator(n=0, maximo=10):
    while True:
        yield n # pausa
        n += 1 # soma +1 no numero inicial
        if n >= maximo:  # condição para acabar ou
            return 'acabou'

gen = generator()

for n in gen:
    print(n)