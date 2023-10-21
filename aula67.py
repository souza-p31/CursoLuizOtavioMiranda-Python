"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""

def soma(x, y, z=None):  # 0, 0.0 e strings vázias em booleano são Falsy
    if z is not None: # Nesse caso, se o parâmetro Z recebesse 0 o if não seria executado
        print(f'{x=} {y=} {z=}', x + y + z) # por isso no lugar colocamos como padrão None, assim caso seja diferente de None o If é executado
    else:
        print(f'{x=} {y=}', x + y)

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
soma(y=9, z=0 , x=7)