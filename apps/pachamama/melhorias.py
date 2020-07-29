from datetime import date

periodo_vendas = []

meses = {
    'Jan': 1,
    'Fev': 2,
    'Mar': 3,
    'Abr': 4,
    'Mai': 5,
    'Jun': 6,
    'Jul': 7,
    'Ago': 8,
    'Set': 9,
    'Out': 10,
    'Nov': 11,
    'Dez': 12}

for i in meses:
    data_1 = date.today()
    data = '{}-{}'.format(i, data_1.year)
    periodo_vendas.append(data)


print(periodo_vendas)