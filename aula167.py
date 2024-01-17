"""
Locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?
view=windowsserver2022-ps&viewFallbackFrom=win10-ps

Por padrão algumas libs (a calendar por exemplo) vem em
inglês, mas isso pode ser corrigido para qualquer idioma
utilizando o locale.
"""
import calendar
import locale

print(locale.getlocale())
print(calendar.calendar(2024))
locale.setlocale(locale.LC_ALL, '') #Dessa forma será alterado para o idioma da máquina.
print(calendar.calendar(2024))

print(locale.getlocale())

#também é possível usar no unix o comando "locale -a" 
#para ver todas as opções