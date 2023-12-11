"""
Polimorfismo em Python Orientado a Objetos

Polimorfismo é o princípio que permite que
classes derivadas de uma mesma superclasse
tenham métodos iguais (com mesma assinatura)
mas comportamentos diferentes.

Assinatura do método = Mesmo nome e quantidade
de parâmetros (retorno não faz parte da assinatura)

Opinião + princípios que contam:
Assinatura de método: nome, parâmetros e retorno iguais

SO"L"ID

Princípio da substituição de Liskov

Objetos de uma superclasse devem ser substituíveis
por objetos de uma subclasse sem querer a aplicação.
"""
from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando - ', self.mensagem)
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando - ', self.mensagem)
        return True

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação NÃO enviada')

notificacao_email = NotificacaoEmail('oi')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('tchau')
notificar(notificacao_sms)
