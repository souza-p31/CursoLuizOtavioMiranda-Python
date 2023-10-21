"""
Funções decoradoras e decoradores
Decorar = Adicionar / Remover / Restringir / Alterar
Funções decoradoras são funções que  decoram outras funções
Decoradores são usados para fazer o Python 
usar as funções decoradoras em outras funções.
Decoradores são "Syntax Sugar" (Açúcar Sintático)
"""

# Essa parte de funções que decoram é interessante para casos que a função já existe, mas precisamos fazer uma checagem. Por exemplo, caso seja colocado um inteiro nessa função o código irá quebrar, e isso precisa ser tratado.

def criar_funcao(func): # essa estrutura é a de uma função decorada
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print('ok, agora você foi decorado')
        return resultado
    return interna # o trabalho dela é receber uma função, criar uma função internar criando um closure e ela não será executada, só quando for chamada, para que a função decoradora execute a função decorada e nela podemos Adicionar / Remover / Restringir / Alterar

def inverte_string(string):
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)