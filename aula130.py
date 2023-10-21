"""
method vs @classmethod vs @staticmethod
method - self, método da instância
@classmethod - cls, método de classe
@staticmethod - método estático (sem self, sem cls)
"""

class Conexao():
    def __init__(self, host='localhost'):
        self.host = host
        self.usuario = None
        self.senha = None
    
    #method - método da instância
    def selecionar_usuario(self, usuario):
        self.usuario = usuario # essa estrutura é chamada se setter (pois seta algo, define algo)
    
    #method - método da instância
    def selecionar_senha(self, senha):
        self.senha = senha

    #classmethod - método da classe
    @classmethod
    def autenticador(cls, usuario, senha):
        conexao = cls
        conexao.usuario = usuario
        conexao.senha = senha
        return conexao    
    
    #staticmethod - função normal porém dentro do escopo da classe (bom por motivos de organização, mas sem função expecifica)
    @staticmethod
    def log(mensagem):
        print('Log:', mensagem)
    
c1 = Conexao()
c1.selecionar_usuario('Pedro')
c1.selecionar_senha('Pedro123')
print(c1.usuario, c1.senha)

c2 = Conexao.autenticador('Pedro', 'Pedro123')
print(c2.usuario, c2.senha)

c3 = Conexao.log('Seja bem-vindo!')