# dir, hasattr e getattr em Python

# No debug console podemos usar o modo interativo
# e verificar quais metodos estão disponiveis na nossa variavel
# mas para isso precisamos debugar o código.

string = 'Luiz'

print(string) # Basta chamar a string e depois chamar dir(string) (nesse caso)

"""string
'Luiz'
dir(string)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', ...]"""

# o hasattr serve para verificar se x metodo é verdadeiro

metodo = 'sum'

if hasattr(string, metodo):
    print('Existe o metodo')
else:
    print('Não existe o método')