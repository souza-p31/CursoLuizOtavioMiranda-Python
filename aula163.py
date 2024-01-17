"""
datetime.timedelta e dateutil.relativedelta 
(calculando datas)

Docs: 
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
"""
from datetime import datetime
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:38:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)
print(data_inicio, data_fim, sep='\n')

delta = relativedelta(data_inicio, data_fim)
print(delta)

print(data_fim + relativedelta(seconds=59, minutes=5))

print(data_fim<data_inicio)
print(data_fim>data_inicio)
print(data_fim==data_inicio)