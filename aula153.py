"""
Método especial __call__

callable é algo que pode ser executado com parênteses

Em classes normais, __call__ faz a instância de uma
classe "callable".
"""
from typing import Any


class CallMe:
    def __init__(self, phone) -> None:
        self.phone = phone

    def __call__(self, *args) -> Any:
        print(f'{args} Está chamando', self.phone)
        return 123456
    
call1 = CallMe('164813548651635')
# print(call1.phone)
call1()
retorno = call1('Luiz')