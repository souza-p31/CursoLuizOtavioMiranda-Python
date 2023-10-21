"""
@staticmethod (métodos estáticos) são inúteis em Python =)
Métodos estáticos são métodos que estão dentro da
classe, mas não tem acesso ao self nem ao cls.
Em resumo, são funções que existem dentro da sua classe.
"""
class Classe:
    @staticmethod
    def funcao_que_esta_na_classe(*args,**kwargs):
        print('oi', args, kwargs)

#métodos estáticos são iguais a funções normais
c1 = Classe()
c1.funcao_que_esta_na_classe(1, 2, 3, nome='Pedro')