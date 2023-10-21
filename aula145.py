"""
Positional-Only Parameters (/) e Keyword-Only Arguments (*)
*args - ilimitado de argumentos posicionais
**kwargs - ilimitado de argumentos nomeados

Positional-Only Parameters (/) - TUDO antes da barra deve ser APENAS posicional

PEP 570 - Python Positional-Only Parameters
https://peps.python.org/pep-0570/

Keywords-Only Arguments (*) - Sozinho NÃO SUGA valores. Depois do * TODOS os argumentos devem ser nomeados.
https://peps.python.org/pep-3102/
"""

def soma(a, b, /, *, c, **kwargs):
    print(kwargs)
    print(a + b + c)

soma(1, 2, c=3, nome='Pedro')