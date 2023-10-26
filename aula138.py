"""
Herança simples - Relações entre classes

Associação - usa (uma classe usa a outra. Ex.:
Classe pintor usa Classe ferramenta)

Composição - É dono de (uma classe passa a ser dona da outra classe no próprio escopo, e se ela for deletada a outra também será)

Herança - É um (uma classe pai da origem a uma classe filho, então a relação entre as duas é bem mais fortre do que a de uma composição)

Herança VS Composição

Classe principal (Pessoa)
    -> super class, base class, parent class
Classes filhas (Cliente)
    -> sub class, child class, derived class

A herança também pode servir para generalizar um objeto para que ele possa ser reaproveitado, Ex.: Classe cliente é muito expecifico, então vou extender/generalizar para Pessoa, porque todo cliente é uma pessoa. O contrário também é possível, tornando um objeto mais expecifico.
"""