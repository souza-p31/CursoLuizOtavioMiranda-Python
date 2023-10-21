"""
Relações entre classes: Associação, Agregação e Composição.
Agregação é uma forma mais especializada da Associação entre dois ou mais objetos. Cada objeto terá seu ciclo de vida independente.
Geralmente é uma relação de um para muitos, onde um objeto tem um ou muitos objetos.
Os objetos podem viver separadamente, mas pode se tratar de uma relação onde um objeto precisa de outro para fazer determinada tarefa.
(existem controvérsias sobre as definições de agregação).
"""

class Carrinho:
    def __init__(self):
        self._produto = []
    

    def total(self):
        print(f'O total no carrinho é: {sum([produto.preco for produto in self._produto])}')
    

    def inserir_produtos(self, *produtos):
        #self._produto.extend(produtos)
        #self._produto += produtos
        for produto in produtos:
            self._produto.append(produto)

    
    def listar_produtos(self):
        for produto in self._produto:
            print(produto.nome, produto.preco)
        print()


class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
produto1, produto2 = Produto('Sabonete', 5.00), Produto('Banana', 6.5)
carrinho.inserir_produtos(produto1, produto2)
carrinho.listar_produtos()
carrinho.total()