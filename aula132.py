"""
@property + @setter - getter e setter no modo Pythônico
- como getter
- p/ evitar quebrar o código cliente
- p/ habilitar setter
- p/ executar ações ao obter um atributo
Atributos que começar com um ou dois underlines
não devem ser usados fora da classe (é entendido que são configurações internas).
🐍🤓🤯🤯🤯🤯
"""

class Caneta:
    def __init__(self, cor):
        #private protected public
        self._cor = cor
        self._cor_tampa = None

    
    @property
    def cor(self):
        print('estou no getter')
        return self._cor


    @cor.setter
    def cor(self, nova_cor):
        print('estou no setter')
        self._cor = nova_cor

    
    @property
    def cor_tampa(self):
        return self._cor_tampa


    @cor_tampa.setter
    def cor_tampa(self, nova_cor):
        self._cor_tampa = nova_cor
        return self._cor_tampa

caneta = Caneta('Azul')
print(caneta.cor)
caneta.cor = 'Rosa'
print(caneta.cor)
print(caneta.cor_tampa)
caneta.cor_tampa = 'Lilás'
print(caneta.cor_tampa)
