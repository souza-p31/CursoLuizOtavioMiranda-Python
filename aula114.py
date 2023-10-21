"""
Funções recursivas e recursividade
- funções que podem se chamar de volta
- úteis p/ dividir problemas grandes em partes menores
Toda função recursiva deve ter:
- um problema que possa ser dividido em partes menores
- um caso recursivo que resolve o pequeno problema
- um caso base que para a recursão
- fatorial n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
"""
# import sys
# sys.setrecursionlimit()
# Basicamente a função recursiva vai retornar ela mesma, é como se fosse um laço, porém como vimos antes nas funções por exemplo, quando criamos vários escopos, aquelas informações ficam armazenadas em algum lugar, que no caso é o call stack. Quando fazemos recursões acontece algo parecido, a função vai stackando até atender a condição base ou estourar o limite do python, que é o chamado stack overflow


# se executarmos desse jeito o código vai retornar um erro de recursão porque vai exceder o limite do Python. Com o modulo sys e função setrecursionlimit até tem como aumentar, mas esse limite funciona como se fosse uma trava, para caso não tenhamos feito de proposito o computador não travar de vez tentando processar. 
# def recursiva(inicio=0, fim=4):
#     print(inicio, fim)

#     inicio += 1
#     return recursiva(inicio, fim)

# recursiva()

# Para que a recursão anterior funcione como deveria não podemos esquecer de colocar a base.
def recursiva(inicio=0, fim=4):
    print(inicio, fim)
    if inicio >= fim:
        return fim
    
    inicio += 1
    return recursiva(inicio, fim)
recursiva() # agora sim  o código funcionou como deveria.

# aplicação na prática da função recursiva
def fatorial(n):
    if n <= 1:
        return 1
    
    return n * fatorial(n - 1)

print(fatorial(5))
print(fatorial(10))
print(fatorial(100)) # até aqui funciona, mas se tentarmos aumentar vamos cair no stack overflow.

# no fim das contas funções recursivas fazem o que os laços fazem só que pior.