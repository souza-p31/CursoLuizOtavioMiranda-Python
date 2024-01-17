"""
Formatando datas do datetime
datetime.strftime('DATA', 'Formato')
https://docs.python.org/3/library/datetime.html
"""
from datetime import datetime

# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime('2022-12-13  7:59:23', '%Y-%m-%d %H:%M:%S')

print(data)

print(data.strftime('%d/%m/%Y'))
print(data.strftime('%d/%m/%Y %H:'))
print(data.strftime('%d/%m/%Y %H:%M'))
print(data.strftime('%d/%m/%Y %H:%M:%S'))
print(data.strftime('ano %Y'))

print(data.year, data.month, data.day, data.hour, data.minute)