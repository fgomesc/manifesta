def fluxo_de_caixa_pachamama(request):
    MES_PAGAMENTO = {
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '10': '10',
        '11': '11',
        '12': '12',
    }

    cartao = []

    for x in MES_PAGAMENTO:
        cartao_lan = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                       classificacao_caixa='(+) Entradas Cartão',
                                                       mes_pagamento=x, ano_pagamento='2020').aggregate(Sum('valor'))[
            'valor__sum']
        cartao.append(cartao_lan)

    return render(request, 'pachamama/fluxo_de_caixa.html', {'cartao': cartao})


{ % for cartao in cartao %}
    < td > {{cartao}} </ td >
{% endfor %}