from django.db.models import Sum
from django.shortcuts import render
from django.utils.datetime_safe import date
from .models import BaseVendasRealizadas


def vendas_pachamama(request):

    queryset = BaseVendasRealizadas.objects.all()

    mes_pagamento_vendas = sorted(set([int(obj.mes_faturamento_2) for obj in queryset]))
    produtos_vendas_lista = sorted(set([str(obj.produto_2) for obj in queryset]))

    periodo_vendas = []
    produtos_vendas = []


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
        'Dez': 12
    }

    for i in meses:
        data_1 = date.today()
        data = '{}-{}'.format(i, data_1.year)
        periodo_vendas.append(data)


    STATUS = {'status_1': 'Conciliado'}

    CLASSIFICACAO_RESULTADO = {'produtos': '( + ) Produtos',}



    for mes in mes_pagamento_vendas:
        cartao_lan = int(BaseVendasRealizadas.objects.filter(situacao_faturamento_2=STATUS['status_1'],
                                                 classificacao_resultado_faturamento_2=CLASSIFICACAO_RESULTADO[
                                                     'produtos'],
                                                 mes_faturamento_2=mes,
                                                 ano_faturamento_2='2020').aggregate(Sum('total_mercadoria_2'))['total_mercadoria_2__sum'])

        produtos_vendas.append(cartao_lan)


    return render(request, 'pachamama/vendas.html', {'produtos_vendas': produtos_vendas,
                                                     'periodo_vendas': periodo_vendas,
                                                     'produtos_vendas_lista': produtos_vendas_lista})

