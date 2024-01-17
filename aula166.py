"""
Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html

Calendar é usado para coisas genéricas de calendários e datas.

Com calendar, você pode saber coisas como:
    - Qual o último dia do mês (ex: monthrange)
    - Qual o nome e número do dia de determinada data (ex: weekday)
    - Criar um calendário em si (ex: monthcalendar)
    - Trabalhar com coisas especificas de calendários (ex: calendar, month)

Por padrão dia da semana começa em 0 até 6
0 = segunda-feira | 6 = domingo
"""

import calendar

# print(calendar.calendar(2024))
print(calendar.month(2024, 1))

numeroPrimeiroDia, ultimoDia = calendar.monthrange(2024, 1)
print(numeroPrimeiroDia, ultimoDia) # retorna zero como primeiro parametro pq representa segunda-feira

print(list(calendar.day_name)) # retorna lista dos dias da semana

print(calendar.day_name[numeroPrimeiroDia]) # retorna dia da semana do dia 1 de janeiro de 2024

print(calendar.weekday(2024, 1, 16))

print(calendar.day_name[calendar.weekday(2024, 1, 16)])