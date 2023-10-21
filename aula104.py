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

# inverte_string_checando_parametro = criar_funcao(inverte_string)
# invertida = inverte_string_checando_parametro('123')
# print(invertida)

# -----------------------------------------------
# Agora a gente entra na parte que explica porque decoradores são o açucar sintatico. Isso tudo que foi feito na mão na verdade pode ser feito de forma bem simples graças ao Python.

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print('ok, agora você foi decorado')
        return resultado
    return interna

@criar_funcao # aqui o Python pega e faz exatamente o que fizemos antes
def inverte_string(string):
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


# No lugar de fazer esse monte de linha de código, podemos simplesmente usar @ e o nome da função decoradora e pronto. O que antes era uma simples função passa a funcionar em conjunto de uma função decoradora. E o mais interessante é que se executarmos o __name__ o que retorna é o nome da função decoradora e não da inicial.

# inverte_string_checando_parametro = criar_funcao(inverte_string)
# invertida = inverte_string_checando_parametro('123')
# print(invertida)

invertida = inverte_string('123')
print(invertida)