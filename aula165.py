"""
# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
"""
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

formato = '%d/%m/%Y'
valor_emprestimo = float(1_000_000)
data_inicial_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final_emprestimo = data_inicial_emprestimo + delta_anos 

data_parcelas = []
data = data_inicial_emprestimo
while data < data_final_emprestimo:
    data += relativedelta(months=1)
    data_parcelas.append(data)


for data in data_parcelas:
    print(f'Datas parcelas {datetime.strftime(data, '%d/%m/%Y')}')