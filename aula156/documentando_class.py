

variavel1 = 1
class Foo:
    """Este é um módulo de exemplo

    Este módulo contém funções e exemplos de documentação de funções.
    A função soma você já conhece bastante.
    """
    def soma(x: int | float, y: int | float) -> int | float:
        """Soma x e y

        Este módulo contém funções e exemplos de
        documentação de funções.
        A função soma você já conhece bastante.

        :parametro x: Número 1
        :tipo x: int or float
        :param y: Número 2
        :type y: int or float

        :return: A soma entre x e y
        :rtype: int or float
        """
        return x + y

    def multiplica(
            x: int | float,
            y: int | float,
            z: int | float | None = None
    ) -> int | float:
        """Multiplica x, y e/ou z
        
        Multiplica x e y. Se z for enviado, multiplica
        x, y e z.
        """

        if z is None:
            return x * y
        return x * y * z

    def bar(self) -> int:
        """O que ele faz

        :raises NotImplementedError: Se o método bla bla
        :raises ValueError: Se o método bla bla
        """
varaivel2 = 2 
varaivel3 = 3
varaivel4 = 4