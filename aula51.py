"""
Introdução ao desempacotamento + tuples (tuplas)
"""
_, _, nome, *_ = ['Maria','Helena','Luiz']
print(nome)

nome1, nome2, nome3 = ['Maria','Helena','Luiz']
print(nome1, nome2, nome3)

nome1, *_ = ['Maria','Helena','Luiz']
print(nome1, _)

"""
se tiver mais variáveis que elementos na lista o
python vai retornar um erro, e se tiver mais elementos
do que variaveis vai acontecer o mesmo erro. Para contornar isso podemos
usar o *variável que vai pegar o resto dos elementos da lista, ainda que 
não tenha mais nenhum. Utilizar o underline(_) para variáveis que não serão usadas
é uma boa prática entre os desenvolvedores, pois ajuda a entender que aquilo não será utilizado.
"""