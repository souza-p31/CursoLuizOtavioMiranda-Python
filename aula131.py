"""
@property - um getter no modo Pythônico
getter - um método para obter um atributo
cor -> get_cor()
modo pythônico - modo do python de fazer as coisas
@property é uma propriedade do objeto, ela é um método que se comporta como um atributo. Dentro da classe tem cara de método e fora dela tem cara de atributo.
Geralmente é usada nas seguintes situações:
- como getter
- p/ evitar quebrar o código cliente
- p/ habilitar setter
- p/ executar ações ao obter um atributo
Código cliente - é o código que usa seu código 
"""

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor


    @property
    def cor(self):
        print('property')
        return self.cor_tinta
    

    @property
    def cor_tampa(self):
        return 123456
    
caneta1 = Caneta('Azul')

print(caneta1.cor)
print(caneta1.cor)
print(caneta1.cor)
print(caneta1.cor)
print(caneta1.cor)
print(caneta1.cor_tampa)