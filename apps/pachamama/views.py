from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import ListView
from apps.pachamama.models import BaseCaixaRealizado


def home_pachamama(request):
    return render(request, 'pachamama/index.html')



@login_required
def fluxo_de_caixa_pachamama(request):

    """

    Chaves

    """


    STATUS = {
        'status_1': 'Conciliado'
    }


    CLASSIFICACAO_CAIXA = {
        'entrada_cartao': '(+) Entradas Cartão',
        'entrada_boleto': '(+) Entrada Boleto',
        'rendimentos': '(+) Rendimentos',
        'impostos': '(-) Impostos',
        'custo_produto': '( - ) Custo de Produtos',
        'trans_correrios': '( - ) Transportes e Correios',
        'devolucoes': '( - ) Devoluções',
        'desp_folha': '( - ) Despesas de Folha',
        'desp_adm': '( -  ) Despesas Administrativas',
        'marketing': '( - ) Marketing',
        'tel_fx_mv': '( - ) Telefonia Fixa e Móvel',
        'desp_ti': '( - ) Despesas TI',
        'tx_jur': '( - ) Taxas/Juros',
    }

    MES_PAGAMENTO = {
        'jan': '1',
        'fev': '2',
        'mar': '3',
        'abr': '4',
        'mai': '5',
        'jun': '6',
        'jul': '7',
        'ago': '8',
        'set': '9',
        'out': '10',
        'nov': '11',
        'dez': '12',
    }

    ANO_PAGAMENTO = {
        'ano_1': '2020'
    }

    """

    Receita - Parte aonde é detalhado das receitas por mês

    """

    # Entrada Cartao

    jan_entrada_cartao = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='(+) Entradas Cartão',
                                                           mes_pagamento='1',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    fev_entrada_cartao = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='(+) Entradas Cartão',
                                                           mes_pagamento='2',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    mar_entrada_cartao = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='(+) Entradas Cartão',
                                                           mes_pagamento='3',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    abr_entrada_cartao = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='(+) Entradas Cartão',
                                                           mes_pagamento='4',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    mai_entrada_cartao = BaseCaixaRealizado.objects.filter(situacao=STATUS["status_1"],
                                                           classificacao_caixa='(+) Entradas Cartão',
                                                           mes_pagamento='5',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    jun_entrada_cartao = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='(+) Entradas Cartão',
                                                           mes_pagamento='6',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    jul_entrada_cartao = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='(+) Entradas Cartão',
                                                           mes_pagamento='7',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    ago_entrada_cartao = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='(+) Entradas Cartão',
                                                           mes_pagamento='8',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    set_entrada_cartao = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='(+) Entradas Cartão',
                                                           mes_pagamento='9',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    out_entrada_cartao = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='(+) Entradas Cartão',
                                                           mes_pagamento='10',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    nov_entrada_cartao = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='(+) Entradas Cartão',
                                                           mes_pagamento='11',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    dez_entrada_cartao = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='(+) Entradas Cartão',
                                                           mes_pagamento='12',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    # ( + ) Entrada Boleto

    jan_entrada_boleto = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='(+) Entrada Boleto',
                                                           mes_pagamento='1',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    fev_entrada_boleto = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='(+) Entrada Boleto',
                                                           mes_pagamento='2',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    mar_entrada_boleto = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='(+) Entrada Boleto',
                                                           mes_pagamento='3',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    abr_entrada_boleto = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='(+) Entrada Boleto',
                                                           mes_pagamento='4',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    mai_entrada_boleto = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='(+) Entrada Boleto',
                                                           mes_pagamento='5',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    jun_entrada_boleto = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='(+) Entrada Boleto',
                                                           mes_pagamento='6',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    jul_entrada_boleto = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='(+) Entrada Boleto',
                                                           mes_pagamento='7',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    ago_entrada_boleto = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='(+) Entrada Boleto',
                                                           mes_pagamento='8',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    set_entrada_boleto = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='(+) Entrada Boleto',
                                                           mes_pagamento='9',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    out_entrada_boleto = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='(+) Entrada Boleto',
                                                           mes_pagamento='10',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    nov_entrada_boleto = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='(+) Entrada Boleto',
                                                           mes_pagamento='11',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    dez_entrada_boleto = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='(+) Entrada Boleto',
                                                           mes_pagamento='12',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    # ( + ) Rendimentos

    jan_entrada_rendimentos = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                                classificacao_caixa='(+) Rendimentos',
                                                                mes_pagamento='1',
                                                                ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    fev_entrada_rendimentos = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                                classificacao_caixa='(+) Rendimentos',
                                                                mes_pagamento='2',
                                                                ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    mar_entrada_rendimentos = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                                classificacao_caixa='(+) Rendimentos',
                                                                mes_pagamento='3',
                                                                ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    abr_entrada_rendimentos = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                                classificacao_caixa='(+) Rendimentos',
                                                                mes_pagamento='4',
                                                                ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    mai_entrada_rendimentos = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                                classificacao_caixa='(+) Rendimentos',
                                                                mes_pagamento='5',
                                                                ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    jun_entrada_rendimentos = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                                classificacao_caixa='(+) Rendimentos',
                                                                mes_pagamento='6',
                                                                ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    jul_entrada_rendimentos = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                                classificacao_caixa='(+) Rendimentos',
                                                                mes_pagamento='7',
                                                                ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    ago_entrada_rendimentos = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                                classificacao_caixa='(+) Rendimentos',
                                                                mes_pagamento='8',
                                                                ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    set_entrada_rendimentos = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                                classificacao_caixa='(+) Rendimentos',
                                                                mes_pagamento='9',
                                                                ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    out_entrada_rendimentos = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                                classificacao_caixa='(+) Rendimentos',
                                                                mes_pagamento='10',
                                                                ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    nov_entrada_rendimentos = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                                classificacao_caixa='(+) Rendimentos',
                                                                mes_pagamento='11',
                                                                ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    dez_entrada_rendimentos = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                                classificacao_caixa='(+) Rendimentos',
                                                                mes_pagamento='12',
                                                                ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    # (-) Impostos

    jan_impostos = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                     classificacao_caixa='(-) Impostos',
                                                     mes_pagamento='1',
                                                     ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    fev_impostos = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                     classificacao_caixa='(-) Impostos',
                                                     mes_pagamento='2',
                                                     ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    mar_impostos = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                     classificacao_caixa='(-) Impostos',
                                                     mes_pagamento='3',
                                                     ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    abr_impostos = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                     classificacao_caixa='(-) Impostos',
                                                     mes_pagamento='4',
                                                     ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    mai_impostos = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                     classificacao_caixa='(-) Impostos',
                                                     mes_pagamento='5',
                                                     ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    jun_impostos = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                     classificacao_caixa='(-) Impostos',
                                                     mes_pagamento='6',
                                                     ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    jul_impostos = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                     classificacao_caixa='(-) Impostos',
                                                     mes_pagamento='7',
                                                     ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    ago_impostos = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                     classificacao_caixa='(-) Impostos',
                                                     mes_pagamento='8',
                                                     ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    set_impostos = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                     classificacao_caixa='(-) Impostos',
                                                     mes_pagamento='9',
                                                     ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    out_impostos = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                     classificacao_caixa='(-) Impostos',
                                                     mes_pagamento='10',
                                                     ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    nov_impostos = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                     classificacao_caixa='(-) Impostos',
                                                     mes_pagamento='11',
                                                     ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    dez_impostos = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                     classificacao_caixa='(-) Impostos',
                                                     mes_pagamento='12',
                                                     ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']


    """

    Custo - Parte aonde é detalhado os custos por mês por mês

    """


    # (-) Custo de Produtos

    jan_custo_producao = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='( - ) Custo de Produtos',
                                                           mes_pagamento='1',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    fev_custo_producao = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='( - ) Custo de Produtos',
                                                           mes_pagamento='2',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    mar_custo_producao = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='( - ) Custo de Produtos',
                                                           mes_pagamento='3',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    abr_custo_producao = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='( - ) Custo de Produtos',
                                                           mes_pagamento='4',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    mai_custo_producao = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='( - ) Custo de Produtos',
                                                           mes_pagamento='5',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    jun_custo_producao = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='( - ) Custo de Produtos',
                                                           mes_pagamento='6',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    jul_custo_producao = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='( - ) Custo de Produtos',
                                                           mes_pagamento='7',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    ago_custo_producao = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='( - ) Custo de Produtos',
                                                           mes_pagamento='8',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    set_custo_producao = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='( - ) Custo de Produtos',
                                                           mes_pagamento='9',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    out_custo_producao = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='( - ) Custo de Produtos',
                                                           mes_pagamento='10',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    nov_custo_producao = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='( - ) Custo de Produtos',
                                                           mes_pagamento='11',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    dez_custo_producao = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='( - ) Custo de Produtos',
                                                           mes_pagamento='12',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    # (-) Transportes e Correios

    jan_transporte_correiros = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                                 classificacao_caixa='( - ) Transportes e Correios',
                                                                 mes_pagamento='1',
                                                                 ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    fev_transporte_correiros = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                                 classificacao_caixa='( - ) Transportes e Correios',
                                                                 mes_pagamento='2',
                                                                 ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    mar_transporte_correiros = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                                 classificacao_caixa='( - ) Transportes e Correios',
                                                                 mes_pagamento='3',
                                                                 ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    abr_transporte_correiros = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                                 classificacao_caixa='( - ) Transportes e Correios',
                                                                 mes_pagamento='4',
                                                                 ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    mai_transporte_correiros = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                                 classificacao_caixa='( - ) Transportes e Correios',
                                                                 mes_pagamento='5',
                                                                 ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    jun_transporte_correiros = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                                 classificacao_caixa='( - ) Transportes e Correios',
                                                                 mes_pagamento='6',
                                                                 ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    jul_transporte_correiros = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                                 classificacao_caixa='( - ) Transportes e Correios',
                                                                 mes_pagamento='7',
                                                                 ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']


    ago_transporte_correiros = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                                 classificacao_caixa='( - ) Transportes e Correios',
                                                                 mes_pagamento='8',
                                                                 ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    set_transporte_correiros = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                                 classificacao_caixa='( - ) Transportes e Correios',
                                                                 mes_pagamento='9',
                                                                 ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    out_transporte_correiros = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                                 classificacao_caixa='( - ) Transportes e Correios',
                                                                 mes_pagamento='10',
                                                                 ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    nov_transporte_correiros = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                                 classificacao_caixa='( - ) Transportes e Correios',
                                                                 mes_pagamento='11',
                                                                 ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    dez_transporte_correiros = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                                 classificacao_caixa='( - ) Transportes e Correios',
                                                                 mes_pagamento='12',
                                                                 ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    # (-) Devoluções

    jan_devolucoes = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                       classificacao_caixa='( - ) Devoluções',
                                                       mes_pagamento='1',
                                                       ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    fev_devolucoes = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                       classificacao_caixa='( - ) Devoluções',
                                                       mes_pagamento='2',
                                                       ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    mar_devolucoes = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                       classificacao_caixa='( - ) Devoluções',
                                                       mes_pagamento='3',
                                                       ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    abr_devolucoes = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                       classificacao_caixa='( - ) Devoluções',
                                                       mes_pagamento='4',
                                                       ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    mai_devolucoes = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                       classificacao_caixa='( - ) Devoluções',
                                                       mes_pagamento='5',
                                                       ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    jun_devolucoes = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                       classificacao_caixa='( - ) Devoluções',
                                                       mes_pagamento='6',
                                                       ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    jul_devolucoes = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                       classificacao_caixa='( - ) Devoluções',
                                                       mes_pagamento='7',
                                                       ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    ago_devolucoes = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                       classificacao_caixa='( - ) Devoluções',
                                                       mes_pagamento='8',
                                                       ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    set_devolucoes = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                       classificacao_caixa='( - ) Devoluções',
                                                       mes_pagamento='9',
                                                       ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    out_devolucoes = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                       classificacao_caixa='( - ) Devoluções',
                                                       mes_pagamento='10',
                                                       ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    nov_devolucoes = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                       classificacao_caixa='( - ) Devoluções',
                                                       mes_pagamento='11',
                                                       ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    dez_devolucoes = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                       classificacao_caixa='( - ) Devoluções',
                                                       mes_pagamento='12',
                                                       ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    """

    Despesas - Parte aonde é detalhado os despesas por mês por mês

    """

    # (-) Despesas de Folha

    jan_despesas_folha = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='( - ) Despesas de Folha',
                                                           mes_pagamento='1',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    fev_despesas_folha = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='( - ) Despesas de Folha',
                                                           mes_pagamento='2',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    mar_despesas_folha = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='( - ) Despesas de Folha',
                                                           mes_pagamento='3',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    abr_despesas_folha = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='( - ) Despesas de Folha',
                                                           mes_pagamento='4',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    mai_despesas_folha = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='( - ) Despesas de Folha',
                                                           mes_pagamento='5',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    jun_despesas_folha = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='( - ) Despesas de Folha',
                                                           mes_pagamento='6',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    jul_despesas_folha = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='( - ) Despesas de Folha',
                                                           mes_pagamento='7',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    ago_despesas_folha = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='( - ) Despesas de Folha',
                                                           mes_pagamento='8',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    set_despesas_folha = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='( - ) Despesas de Folha',
                                                           mes_pagamento='9',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    out_despesas_folha = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='( - ) Despesas de Folha',
                                                           mes_pagamento='10',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    nov_despesas_folha = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='( - ) Despesas de Folha',
                                                           mes_pagamento='11',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    dez_despesas_folha = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                           classificacao_caixa='( - ) Despesas de Folha',
                                                           mes_pagamento='12',
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']


    # (-) Despesas Administrativas

    jan_despesas_adm = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                         classificacao_caixa='( -  ) Despesas Administrativas',
                                                         mes_pagamento='1',
                                                         ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    fev_despesas_adm = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                         classificacao_caixa='( -  ) Despesas Administrativas',
                                                         mes_pagamento='2',
                                                         ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    mar_despesas_adm = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                         classificacao_caixa='( -  ) Despesas Administrativas',
                                                         mes_pagamento='3',
                                                         ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    abr_despesas_adm = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                         classificacao_caixa='( -  ) Despesas Administrativas',
                                                         mes_pagamento='4',
                                                         ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    mai_despesas_adm = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                         classificacao_caixa='( -  ) Despesas Administrativas',
                                                         mes_pagamento='5',
                                                         ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    jun_despesas_adm = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                         classificacao_caixa='( -  ) Despesas Administrativas',
                                                         mes_pagamento='6',
                                                         ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    jul_despesas_adm = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                         classificacao_caixa='( -  ) Despesas Administrativas',
                                                         mes_pagamento='7',
                                                         ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    ago_despesas_adm = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                         classificacao_caixa='( -  ) Despesas Administrativas',
                                                         mes_pagamento='8',
                                                         ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    set_despesas_adm = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                         classificacao_caixa='( -  ) Despesas Administrativas',
                                                         mes_pagamento='9',
                                                         ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    out_despesas_adm = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                         classificacao_caixa='( -  ) Despesas Administrativas',
                                                         mes_pagamento='10',
                                                         ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    nov_despesas_adm = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                         classificacao_caixa='( -  ) Despesas Administrativas',
                                                         mes_pagamento='11',
                                                         ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    dez_despesas_adm = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                         classificacao_caixa='( -  ) Despesas Administrativas',
                                                         mes_pagamento='12',
                                                         ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    # (-) Marketing

    jan_marketing = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                      classificacao_caixa='( - ) Marketing',
                                                      mes_pagamento='1',
                                                      ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    fev_marketing = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                      classificacao_caixa='( - ) Marketing',
                                                      mes_pagamento='2',
                                                      ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    mar_marketing = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                      classificacao_caixa='( - ) Marketing',
                                                      mes_pagamento='3',
                                                      ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    abr_marketing = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                      classificacao_caixa='( - ) Marketing',
                                                      mes_pagamento='4',
                                                      ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    mai_marketing = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                      classificacao_caixa='( - ) Marketing',
                                                      mes_pagamento='5',
                                                      ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    jun_marketing = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                      classificacao_caixa='( - ) Marketing',
                                                      mes_pagamento='6',
                                                      ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    jul_marketing = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                      classificacao_caixa='( - ) Marketing',
                                                      mes_pagamento='7',
                                                      ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    ago_marketing = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                      classificacao_caixa='( - ) Marketing',
                                                      mes_pagamento='8',
                                                      ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    set_marketing = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                      classificacao_caixa='( - ) Marketing',
                                                      mes_pagamento='9',
                                                      ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    out_marketing = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                      classificacao_caixa='( - ) Marketing',
                                                      mes_pagamento='10',
                                                      ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    nov_marketing = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                      classificacao_caixa='( - ) Marketing',
                                                      mes_pagamento='11',
                                                      ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    dez_marketing = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                      classificacao_caixa='( - ) Marketing',
                                                      mes_pagamento='12',
                                                      ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    # (-) Telefonia Fixa e Móvel

    jan_tel_mov_fix = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                        classificacao_caixa='( - ) Telefonia Fixa e Móvel',
                                                        mes_pagamento='1',
                                                        ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    fev_tel_mov_fix = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                        classificacao_caixa='( - ) Telefonia Fixa e Móvel',
                                                        mes_pagamento='2',
                                                        ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    mar_tel_mov_fix = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                        classificacao_caixa='( - ) Telefonia Fixa e Móvel',
                                                        mes_pagamento='3',
                                                        ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    abr_tel_mov_fix = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                        classificacao_caixa='( - ) Telefonia Fixa e Móvel',
                                                        mes_pagamento='4',
                                                        ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    mai_tel_mov_fix = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                        classificacao_caixa='( - ) Telefonia Fixa e Móvel',
                                                        mes_pagamento='5',
                                                        ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    jun_tel_mov_fix = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                        classificacao_caixa='( - ) Telefonia Fixa e Móvel',
                                                        mes_pagamento='6',
                                                        ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    jul_tel_mov_fix = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                        classificacao_caixa='( - ) Telefonia Fixa e Móvel',
                                                        mes_pagamento='7',
                                                        ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    ago_tel_mov_fix = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                        classificacao_caixa='( - ) Telefonia Fixa e Móvel',
                                                        mes_pagamento='8',
                                                        ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    set_tel_mov_fix = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                        classificacao_caixa='( - ) Telefonia Fixa e Móvel',
                                                        mes_pagamento='9',
                                                        ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    out_tel_mov_fix = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                        classificacao_caixa='( - ) Telefonia Fixa e Móvel',
                                                        mes_pagamento='10',
                                                        ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    nov_tel_mov_fix = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                        classificacao_caixa='( - ) Telefonia Fixa e Móvel',
                                                        mes_pagamento='11',
                                                        ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    dez_tel_mov_fix = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                        classificacao_caixa='( - ) Telefonia Fixa e Móvel',
                                                        mes_pagamento='12',
                                                        ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']
    # (-) Despesas TI

    jan_deso_ti = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                    classificacao_caixa='( - ) Despesas TI',
                                                    mes_pagamento='1',
                                                    ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    fev_deso_ti = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                    classificacao_caixa='( - ) Despesas TI',
                                                    mes_pagamento='2',
                                                    ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    mar_deso_ti = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                    classificacao_caixa='( - ) Despesas TI',
                                                    mes_pagamento='3',
                                                    ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    abr_deso_ti = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                    classificacao_caixa='( - ) Despesas TI',
                                                    mes_pagamento='4',
                                                    ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    mai_deso_ti = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                    classificacao_caixa='( - ) Despesas TI',
                                                    mes_pagamento='5',
                                                    ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    jun_deso_ti = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                    classificacao_caixa='( - ) Despesas TI',
                                                    mes_pagamento='6',
                                                    ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    jul_deso_ti = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                    classificacao_caixa='( - ) Despesas TI',
                                                    mes_pagamento='7',
                                                    ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    ago_deso_ti = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                    classificacao_caixa='( - ) Despesas TI',
                                                    mes_pagamento='8',
                                                    ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    set_deso_ti = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                    classificacao_caixa='( - ) Despesas TI',
                                                    mes_pagamento='9',
                                                    ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    out_deso_ti = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                    classificacao_caixa='( - ) Despesas TI',
                                                    mes_pagamento='10',
                                                    ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']


    nov_deso_ti = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                    classificacao_caixa='( - ) Despesas TI',
                                                    mes_pagamento='11',
                                                    ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']


    dez_deso_ti = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                    classificacao_caixa='( - ) Despesas TI',
                                                    mes_pagamento='12',
                                                    ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    # ( - ) Taxas/Juros

    jan_tax_juros = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                      classificacao_caixa='( - ) Taxas/Juros',
                                                      mes_pagamento='1',
                                                      ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    fev_tax_juros = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                      classificacao_caixa='( - ) Taxas/Juros',
                                                      mes_pagamento='2',
                                                      ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    mar_tax_juros = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                      classificacao_caixa='( - ) Taxas/Juros',
                                                      mes_pagamento='3',
                                                      ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    abr_tax_juros = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                      classificacao_caixa='( - ) Taxas/Juros',
                                                      mes_pagamento='4',
                                                      ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    mai_tax_juros = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                      classificacao_caixa='( - ) Taxas/Juros',
                                                      mes_pagamento='5',
                                                      ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    jun_tax_juros = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                      classificacao_caixa='( - ) Taxas/Juros',
                                                      mes_pagamento='6',
                                                      ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    jul_tax_juros = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                      classificacao_caixa='( - ) Taxas/Juros',
                                                      mes_pagamento='7',
                                                      ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    ago_tax_juros = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                      classificacao_caixa='( - ) Taxas/Juros',
                                                      mes_pagamento='8',
                                                      ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    set_tax_juros = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                      classificacao_caixa='( - ) Taxas/Juros',
                                                      mes_pagamento='9',
                                                      ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    out_tax_juros = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                      classificacao_caixa='( - ) Taxas/Juros',
                                                      mes_pagamento='10',
                                                      ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    nov_tax_juros = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                      classificacao_caixa='( - ) Taxas/Juros',
                                                      mes_pagamento='11',
                                                      ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']

    dez_tax_juros = BaseCaixaRealizado.objects.filter(situacao='Conciliado',
                                                      classificacao_caixa='( - ) Taxas/Juros',
                                                      mes_pagamento='12',
                                                      ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']
    """

    Totais - Parte aonde é detalhado os totais por mês por mês

    """


    # Total Receita

    jan_total_receita = (jan_entrada_cartao + jan_entrada_boleto + jan_entrada_rendimentos) - jan_impostos
    fev_total_receita = (fev_entrada_cartao + fev_entrada_boleto + fev_entrada_rendimentos) - fev_impostos
    mar_total_receita = (mar_entrada_cartao + mar_entrada_boleto + mar_entrada_rendimentos) - mar_impostos
    abr_total_receita = (abr_entrada_cartao + abr_entrada_boleto + abr_entrada_rendimentos) - abr_impostos
    mai_total_receita = (mai_entrada_cartao + mai_entrada_boleto + mai_entrada_rendimentos) - mai_impostos
    jun_total_receita = (jun_entrada_cartao + jun_entrada_boleto + jun_entrada_rendimentos) - jun_impostos
    jul_total_receita = (jul_entrada_cartao + jul_entrada_boleto + jul_entrada_rendimentos) - jul_impostos
    ago_total_receita = (ago_entrada_cartao + ago_entrada_boleto + ago_entrada_rendimentos) - ago_impostos
    set_total_receita = (set_entrada_cartao + set_entrada_boleto + set_entrada_rendimentos) - set_impostos
    out_total_receita = (out_entrada_cartao + out_entrada_boleto + out_entrada_rendimentos) - out_impostos
    nov_total_receita = (nov_entrada_cartao + nov_entrada_boleto + nov_entrada_rendimentos) - nov_impostos
    dez_total_receita = (dez_entrada_cartao + dez_entrada_boleto + dez_entrada_rendimentos) - dez_impostos


    # Total Custo

    jan_total_custo = jan_custo_producao + jan_transporte_correiros + jan_devolucoes
    fev_total_custo = fev_custo_producao + fev_transporte_correiros + fev_devolucoes
    mar_total_custo = mar_custo_producao + mar_transporte_correiros + mar_devolucoes
    abr_total_custo = abr_custo_producao + abr_transporte_correiros + abr_devolucoes
    mai_total_custo = mai_custo_producao + mai_transporte_correiros + mai_devolucoes
    jun_total_custo = jun_custo_producao + jun_transporte_correiros + jun_devolucoes
    jul_total_custo = jul_custo_producao + jul_transporte_correiros + jul_devolucoes
    ago_total_custo = ago_custo_producao + ago_transporte_correiros + ago_devolucoes
    set_total_custo = set_custo_producao + set_transporte_correiros + set_devolucoes
    out_total_custo = out_custo_producao + out_transporte_correiros + out_devolucoes
    nov_total_custo = nov_custo_producao + nov_transporte_correiros + nov_devolucoes
    dez_total_custo = dez_custo_producao + dez_transporte_correiros + dez_devolucoes




    # Total Despesas

    jan_total_despesas = jan_despesas_folha + jan_despesas_adm + jan_marketing + jan_tel_mov_fix + jan_deso_ti + jan_tax_juros
    fev_total_despesas = fev_despesas_folha + fev_despesas_adm + fev_marketing + fev_tel_mov_fix + fev_deso_ti + fev_tax_juros
    mar_total_despesas = mar_despesas_folha + mar_despesas_adm + mar_marketing + mar_tel_mov_fix + mar_deso_ti + mar_tax_juros
    abr_total_despesas = abr_despesas_folha + abr_despesas_adm + abr_marketing + abr_tel_mov_fix + abr_deso_ti + abr_tax_juros
    mai_total_despesas = mai_despesas_folha + mai_despesas_adm + mai_marketing + mai_tel_mov_fix + mai_deso_ti + mai_tax_juros
    jun_total_despesas = jun_despesas_folha + jun_despesas_adm + jun_marketing + jun_tel_mov_fix + jun_deso_ti + jun_tax_juros
    jul_total_despesas = jul_despesas_folha + jul_despesas_adm + jul_marketing + jul_tel_mov_fix + jul_deso_ti + jul_tax_juros
    ago_total_despesas = ago_despesas_folha + ago_despesas_adm + ago_marketing + ago_tel_mov_fix + ago_deso_ti + ago_tax_juros
    set_total_despesas = set_despesas_folha + set_despesas_adm + set_marketing + set_tel_mov_fix + set_deso_ti + set_tax_juros
    out_total_despesas = out_despesas_folha + out_despesas_adm + out_marketing + out_tel_mov_fix + out_deso_ti + out_tax_juros
    nov_total_despesas = nov_despesas_folha + nov_despesas_adm + nov_marketing + nov_tel_mov_fix + nov_deso_ti + nov_tax_juros
    dez_total_despesas = dez_despesas_folha + dez_despesas_adm + dez_marketing + dez_tel_mov_fix + dez_deso_ti + dez_tax_juros


    # FLuxo de Caixa

    jan_fluxo = jan_total_receita + jan_total_custo + jan_total_despesas
    fev_fluxo = fev_total_receita + fev_total_custo + fev_total_despesas
    mar_fluxo = mar_total_receita + mar_total_custo + mar_total_despesas
    abr_fluxo = abr_total_receita + abr_total_custo + abr_total_despesas
    mai_fluxo = mai_total_receita + mai_total_custo + mai_total_despesas
    jun_fluxo = jun_total_receita + jun_total_custo + jun_total_despesas
    jul_fluxo = jul_total_receita + jul_total_custo + jul_total_despesas
    ago_fluxo = ago_total_receita + ago_total_custo + ago_total_despesas
    set_fluxo = set_total_receita + set_total_custo + set_total_despesas
    out_fluxo = out_total_receita + out_total_custo + out_total_despesas
    nov_fluxo = nov_total_receita + nov_total_custo + nov_total_despesas
    dez_fluxo = dez_total_receita + dez_total_custo + dez_total_despesas

    # Total Receita Cartao

    total_receita = jan_total_receita + \
                    fev_total_receita + \
                    mar_total_receita + \
                    abr_total_receita + \
                    mai_total_receita + \
                    jun_total_receita + \
                    jul_total_receita + \
                    ago_total_receita + \
                    set_total_receita + \
                    out_total_receita + \
                    nov_total_receita + \
                    dez_total_receita


    total_receita_cartao = jan_entrada_cartao + \
                               fev_entrada_cartao + \
                               mar_entrada_cartao + \
                               abr_entrada_cartao + \
                               mai_entrada_cartao + \
                               jun_entrada_cartao + \
                               jul_entrada_cartao + \
                               ago_entrada_cartao + \
                               set_entrada_cartao + \
                               out_entrada_cartao + \
                               nov_entrada_cartao + \
                               dez_entrada_cartao

    total_receita_boleto = jan_entrada_boleto + \
                           fev_entrada_boleto + \
                           mar_entrada_boleto + \
                           abr_entrada_boleto + \
                           mai_entrada_boleto + \
                           jun_entrada_boleto + \
                           jul_entrada_boleto + \
                           ago_entrada_boleto + \
                           set_entrada_boleto + \
                           out_entrada_boleto + \
                           nov_entrada_boleto + \
                           dez_entrada_boleto

    total_rendimentos = jan_entrada_rendimentos + \
                        fev_entrada_rendimentos + \
                        mar_entrada_rendimentos + \
                        abr_entrada_rendimentos + \
                        mai_entrada_rendimentos + \
                        jun_entrada_rendimentos + \
                        jul_entrada_rendimentos + \
                        ago_entrada_rendimentos + \
                        set_entrada_rendimentos + \
                        out_entrada_rendimentos + \
                        nov_entrada_rendimentos + \
                        dez_entrada_rendimentos


    total_impostos = jan_impostos + \
                     fev_impostos + \
                     mar_impostos + \
                     abr_impostos + \
                     mai_impostos + \
                     jun_impostos + \
                     jul_impostos + \
                     ago_impostos + \
                     set_impostos + \
                     out_impostos + \
                     nov_impostos + \
                     dez_impostos

    total_custos = jan_total_custo + \
                   fev_total_custo + \
                   mar_total_custo + \
                   abr_total_custo + \
                   mai_total_custo + \
                   jun_total_custo + \
                   jul_total_custo + \
                   ago_total_custo + \
                   set_total_custo + \
                   out_total_custo + \
                   nov_total_custo + \
                   dez_total_custo

    total_custo = jan_custo_producao + \
                  fev_custo_producao + \
                  mar_custo_producao + \
                  abr_custo_producao + \
                  mai_custo_producao + \
                  jun_custo_producao + \
                  jul_custo_producao + \
                  ago_custo_producao + \
                  set_custo_producao + \
                  out_custo_producao + \
                  nov_custo_producao + \
                  dez_custo_producao

    total_trans_correios = jan_transporte_correiros + \
                           fev_transporte_correiros + \
                           mar_transporte_correiros + \
                           abr_transporte_correiros + \
                           mai_transporte_correiros + \
                           jun_transporte_correiros + \
                           jul_transporte_correiros + \
                           ago_transporte_correiros + \
                           set_transporte_correiros + \
                           out_transporte_correiros + \
                           nov_transporte_correiros + \
                           dez_transporte_correiros

    total_devolucoes = jan_devolucoes + \
                       fev_devolucoes + \
                       mar_devolucoes + \
                       abr_devolucoes + \
                       mai_devolucoes + \
                       jun_devolucoes + \
                       jul_devolucoes + \
                       ago_devolucoes + \
                       set_devolucoes + \
                       out_devolucoes + \
                       nov_devolucoes + \
                       dez_devolucoes

    total_despesas = jan_total_despesas + \
                     fev_total_despesas + \
                     mar_total_despesas + \
                     abr_total_despesas + \
                     mai_total_despesas + \
                     jun_total_despesas + \
                     jul_total_despesas + \
                     ago_total_despesas + \
                     set_total_despesas + \
                     out_total_despesas + \
                     nov_total_despesas + \
                     dez_total_despesas

    total_folha = jan_despesas_folha + \
                  fev_despesas_folha + \
                  mar_despesas_folha + \
                  abr_despesas_folha + \
                  mai_despesas_folha + \
                  jun_despesas_folha + \
                  jul_despesas_folha + \
                  ago_despesas_folha + \
                  set_despesas_folha + \
                  out_despesas_folha + \
                  nov_despesas_folha + \
                  dez_despesas_folha

    total_adm = jan_despesas_adm + \
                fev_despesas_adm + \
                mar_despesas_adm + \
                abr_despesas_adm + \
                mai_despesas_adm + \
                jun_despesas_adm + \
                jul_despesas_adm + \
                ago_despesas_adm + \
                set_despesas_adm + \
                out_despesas_adm + \
                nov_despesas_adm + \
                dez_despesas_adm

    total_marketing = jan_marketing + \
                      fev_marketing + \
                      mar_marketing + \
                      abr_marketing + \
                      mai_marketing + \
                      jun_marketing + \
                      jul_marketing + \
                      ago_marketing + \
                      set_marketing + \
                      out_marketing + \
                      nov_marketing + \
                      dez_marketing

    total_tel_fx_mv = jan_tel_mov_fix + \
                      fev_tel_mov_fix + \
                      mar_tel_mov_fix + \
                      abr_tel_mov_fix + \
                      mai_tel_mov_fix + \
                      jun_tel_mov_fix + \
                      jul_tel_mov_fix + \
                      ago_tel_mov_fix + \
                      set_tel_mov_fix + \
                      out_tel_mov_fix + \
                      nov_tel_mov_fix + \
                      dez_tel_mov_fix

    total_desp_ti = jan_deso_ti + \
                    fev_deso_ti + \
                    mar_deso_ti + \
                    abr_deso_ti + \
                    mai_deso_ti + \
                    jun_deso_ti + \
                    jul_deso_ti + \
                    ago_deso_ti + \
                    set_deso_ti + \
                    out_deso_ti + \
                    nov_deso_ti + \
                    dez_deso_ti

    total_tx_jur = jan_tax_juros + \
                   fev_tax_juros + \
                   mar_tax_juros + \
                   abr_tax_juros + \
                   mai_tax_juros + \
                   jun_tax_juros + \
                   jul_tax_juros + \
                   ago_tax_juros + \
                   set_tax_juros + \
                   out_tax_juros + \
                   nov_tax_juros + \
                   dez_tax_juros

    total_fluxo_caixa = jan_fluxo + \
                        fev_fluxo + \
                        mar_fluxo + \
                        abr_fluxo + \
                        mai_fluxo + \
                        jun_fluxo + \
                        jul_fluxo + \
                        jan_fluxo


    #mai_fluxo_caixa = mai_total_receita + (total_despesas + mai_total_custo)



    return render(request, 'pachamama/fluxo_de_caixa.html', {'jan_entrada_cartao': jan_entrada_cartao,
                                                             'fev_entrada_cartao': fev_entrada_cartao,
                                                             'mar_entrada_cartao': mar_entrada_cartao,
                                                             'abr_entrada_cartao': abr_entrada_cartao,
                                                             'mai_entrada_cartao': mai_entrada_cartao,
                                                             'jun_entrada_cartao': jun_entrada_cartao,
                                                             'jul_entrada_cartao': jul_entrada_cartao,
                                                             'ago_entrada_cartao': ago_entrada_cartao,
                                                             'set_entrada_cartao': set_entrada_cartao,
                                                             'out_entrada_cartao': out_entrada_cartao,
                                                             'nov_entrada_cartao': nov_entrada_cartao,
                                                             'dez_entrada_cartao': dez_entrada_cartao,

                                                             'jan_entrada_boleto': jan_entrada_boleto,
                                                             'fev_entrada_boleto': fev_entrada_boleto,
                                                             'mar_entrada_boleto': mar_entrada_boleto,
                                                             'abr_entrada_boleto': abr_entrada_boleto,
                                                             'mai_entrada_boleto': mai_entrada_boleto,
                                                             'jun_entrada_boleto': jun_entrada_boleto,
                                                             'jul_entrada_boleto': jul_entrada_boleto,
                                                             'ago_entrada_boleto': ago_entrada_boleto,
                                                             'set_entrada_boleto': set_entrada_boleto,
                                                             'out_entrada_boleto': out_entrada_boleto,
                                                             'nov_entrada_boleto': nov_entrada_boleto,
                                                             'dez_entrada_boleto': dez_entrada_boleto,

                                                             'jan_entrada_rendimentos': jan_entrada_rendimentos,
                                                             'fev_entrada_rendimentos': fev_entrada_rendimentos,
                                                             'mar_entrada_rendimentos': mar_entrada_rendimentos,
                                                             'abr_entrada_rendimentos': abr_entrada_rendimentos,
                                                             'mai_entrada_rendimentos': mai_entrada_rendimentos,
                                                             'jun_entrada_rendimentos': jun_entrada_rendimentos,
                                                             'jul_entrada_rendimentos': jul_entrada_rendimentos,
                                                             'ago_entrada_rendimentos': ago_entrada_rendimentos,
                                                             'set_entrada_rendimentos': set_entrada_rendimentos,
                                                             'out_entrada_rendimentos': out_entrada_rendimentos,
                                                             'nov_entrada_rendimentos': nov_entrada_rendimentos,
                                                             'dez_entrada_rendimentos': dez_entrada_rendimentos,

                                                             'jan_impostos': jan_impostos,
                                                             'fev_impostos': fev_impostos,
                                                             'mar_impostos': mar_impostos,
                                                             'abr_impostos': abr_impostos,
                                                             'mai_impostos': mai_impostos,
                                                             'jun_impostos': jun_impostos,
                                                             'jul_impostos': jul_impostos,
                                                             'ago_impostos': ago_impostos,
                                                             'set_impostos': set_impostos,
                                                             'out_impostos': out_impostos,
                                                             'nov_impostos': nov_impostos,
                                                             'dez_impostos': dez_impostos,

                                                             'jan_custo_producao': jan_custo_producao,
                                                             'fev_custo_producao': fev_custo_producao,
                                                             'mar_custo_producao': mar_custo_producao,
                                                             'abr_custo_producao': abr_custo_producao,
                                                             'mai_custo_producao': mai_custo_producao,
                                                             'jun_custo_producao': jun_custo_producao,
                                                             'jul_custo_producao': jul_custo_producao,
                                                             'ago_custo_producao': ago_custo_producao,
                                                             'set_custo_producao': set_custo_producao,
                                                             'out_custo_producao': out_custo_producao,
                                                             'nov_custo_producao': nov_custo_producao,
                                                             'dez_custo_producao': dez_custo_producao,

                                                             'jan_transporte_correiros': jan_transporte_correiros,
                                                             'fev_transporte_correiros': fev_transporte_correiros,
                                                             'mar_transporte_correiros': mar_transporte_correiros,
                                                             'abr_transporte_correiros': abr_transporte_correiros,
                                                             'mai_transporte_correiros': mai_transporte_correiros,
                                                             'jun_transporte_correiros': jun_transporte_correiros,
                                                             'jul_transporte_correiros': jul_transporte_correiros,
                                                             'ago_transporte_correiros': ago_transporte_correiros,
                                                             'set_transporte_correiros': set_transporte_correiros,
                                                             'out_transporte_correiros': out_transporte_correiros,
                                                             'nov_transporte_correiros': nov_transporte_correiros,
                                                             'dez_transporte_correiros': dez_transporte_correiros,

                                                             'jan_devolucoes': jan_devolucoes,
                                                             'fev_devolucoes': fev_devolucoes,
                                                             'mar_devolucoes': mar_devolucoes,
                                                             'abr_devolucoes': abr_devolucoes,
                                                             'mai_devolucoes': mai_devolucoes,
                                                             'jun_devolucoes': jun_devolucoes,
                                                             'jul_devolucoes': jul_devolucoes,
                                                             'ago_devolucoes': ago_devolucoes,
                                                             'set_devolucoes': set_devolucoes,
                                                             'out_devolucoes': out_devolucoes,
                                                             'nov_devolucoes': nov_devolucoes,
                                                             'dez_devolucoes': dez_devolucoes,

                                                             'jan_despesas_folha': jan_despesas_folha,
                                                             'fev_despesas_folha': fev_despesas_folha,
                                                             'mar_despesas_folha': mar_despesas_folha,
                                                             'abr_despesas_folha': abr_despesas_folha,
                                                             'mai_despesas_folha': mai_despesas_folha,
                                                             'jun_despesas_folha': jun_despesas_folha,
                                                             'jul_despesas_folha': jul_despesas_folha,
                                                             'ago_despesas_folha': ago_despesas_folha,
                                                             'set_despesas_folha': set_despesas_folha,
                                                             'out_despesas_folha': out_despesas_folha,
                                                             'nov_despesas_folha': nov_despesas_folha,
                                                             'dez_despesas_folha': dez_despesas_folha,

                                                             'jan_despesas_adm': jan_despesas_adm,
                                                             'fev_despesas_adm': fev_despesas_adm,
                                                             'mar_despesas_adm': abr_despesas_adm,
                                                             'mai_despesas_adm': mai_despesas_adm,
                                                             'jun_despesas_adm': jun_despesas_adm,
                                                             'jul_despesas_adm': jul_despesas_adm,
                                                             'set_despesas_adm': set_despesas_adm,
                                                             'out_despesas_adm': out_despesas_adm,
                                                             'nov_despesas_adm': nov_despesas_adm,
                                                             'eez_despesas_adm': dez_despesas_adm,

                                                             'jan_marketing': jan_marketing,
                                                             'fev_marketing': fev_marketing,
                                                             'mar_marketing': mar_marketing,
                                                             'abr_marketing': abr_marketing,
                                                             'mai_marketing': mai_marketing,
                                                             'jun_marketing': jun_marketing,
                                                             'jul_marketing': jul_marketing,
                                                             'ago_marketing': ago_marketing,
                                                             'set_marketing': set_marketing,
                                                             'out_marketing': out_marketing,
                                                             'nov_marketing': nov_marketing,
                                                             'dez_marketing': dez_marketing,

                                                             'jan_tel_mov_fix': jan_tel_mov_fix,
                                                             'fev_tel_mov_fix': fev_tel_mov_fix,
                                                             'mar_tel_mov_fix': mar_tel_mov_fix,
                                                             'abr_tel_mov_fix': abr_tel_mov_fix,
                                                             'mai_tel_mov_fix': mai_tel_mov_fix,
                                                             'jun_tel_mov_fix': jun_tel_mov_fix,
                                                             'jul_tel_mov_fix': jul_tel_mov_fix,
                                                             'ago_tel_mov_fix': ago_tel_mov_fix,
                                                             'set_tel_mov_fix': set_tel_mov_fix,
                                                             'out_tel_mov_fix': nov_tel_mov_fix,
                                                             'dez_tel_mov_fix': dez_tel_mov_fix,

                                                             'jan_deso_ti': jan_deso_ti,
                                                             'fev_deso_ti': fev_deso_ti,
                                                             'mar_deso_ti': mar_deso_ti,
                                                             'abr_deso_ti': abr_deso_ti,
                                                             'mai_deso_ti': mai_deso_ti,
                                                             'jun_deso_ti': jun_deso_ti,
                                                             'jul_deso_ti': jul_deso_ti,
                                                             'ago_deso_ti': ago_deso_ti,
                                                             'set_deso_ti': set_deso_ti,
                                                             'out_deso_ti': out_deso_ti,
                                                             'nov_deso_ti': nov_deso_ti,
                                                             'dez_deso_ti': dez_deso_ti,

                                                             'jan_tax_juros': jan_tax_juros,
                                                             'fev_tax_juros': fev_tax_juros,
                                                             'mar_tax_juros': mar_tax_juros,
                                                             'abr_tax_juros': abr_tax_juros,
                                                             'mai_tax_juros': mai_tax_juros,
                                                             'jun_tax_juros': jun_tax_juros,
                                                             'jul_tax_juros': jul_tax_juros,
                                                             'ago_tax_juros': ago_tax_juros,
                                                             'set_tax_juros': set_tax_juros,
                                                             'out_tax_juros': out_tax_juros,
                                                             'nov_tax_juros': nov_tax_juros,
                                                             'dez_tax_juros': dez_tax_juros,

                                                             'jan_total_receita': jan_total_receita,
                                                             'fev_total_receita': fev_total_receita,
                                                             'mar_total_receita': mar_total_receita,
                                                             'abr_total_receita': abr_total_receita,
                                                             'mai_total_receita': mai_total_receita,
                                                             'jun_total_receita': jun_total_receita,
                                                             'jul_total_receita': jul_total_receita,
                                                             'ago_total_receita': ago_total_receita,
                                                             'set_total_receita': set_total_receita,
                                                             'out_total_receita': out_total_receita,
                                                             'nov_total_receita': nov_total_receita,
                                                             'dez_total_receita': dez_total_receita,

                                                             'jan_total_custo': jan_total_custo,
                                                             'fev_total_custo': fev_total_custo,
                                                             'mar_total_custo': mar_total_custo,
                                                             'abr_total_custo': abr_total_custo,
                                                             'mai_total_custo': mai_total_custo,
                                                             'jun_total_custo': jun_total_custo,
                                                             'jul_total_custo': jul_total_custo,
                                                             'ago_total_custo': ago_total_custo,
                                                             'set_total_custo': set_total_custo,
                                                             'out_total_custo': out_total_custo,
                                                             'nov_total_custo': nov_total_custo,
                                                             'dez_total_custo': dez_total_custo,

                                                             'jan_total_despesas': jan_total_despesas,
                                                             'fev_total_despesas': fev_total_despesas,
                                                             'mar_total_despesas': mar_total_despesas,
                                                             'abr_total_despesas': abr_total_despesas,
                                                             'mai_total_despesas': mai_total_despesas,
                                                             'jun_total_despesas': jun_total_despesas,
                                                             'jul_total_despesas': jul_total_despesas,
                                                             'ago_total_despesas': ago_total_despesas,
                                                             'set_total_despesas': set_total_despesas,
                                                             'out_total_despesas': out_total_despesas,
                                                             'nov_total_despesas': nov_total_despesas,
                                                             'dez_total_despesas': dez_total_despesas,

                                                             'jan_fluxo': jan_fluxo,
                                                             'fev_fluxo': fev_fluxo,
                                                             'mar_fluxo': mar_fluxo,
                                                             'abr_fluxo': abr_fluxo,
                                                             'mai_fluxo': mai_fluxo,
                                                             'jun_fluxo': jun_fluxo,
                                                             'jul_fluxo': jul_fluxo,
                                                             'ago_fluxo': ago_fluxo,
                                                             'set_fluxo': set_fluxo,
                                                             'out_fluxo': out_fluxo,
                                                             'nov_fluxo': nov_fluxo,
                                                             'dez_fluxo': dez_fluxo,

                                                             'total_receita': total_receita,
                                                             'total_receita_cartao': total_receita_cartao,
                                                             'total_receita_boleto': total_receita_boleto,
                                                             'total_rendimentos': total_rendimentos,
                                                             'total_impostos': total_impostos,
                                                             'total_custos': total_custos,
                                                             'total_custo': total_custo,
                                                             'total_trans_correios': total_trans_correios,
                                                             'total_devolucoes': total_devolucoes,
                                                             'total_despesas': total_despesas,
                                                             'total_folha': total_folha,
                                                             'total_adm': total_adm,
                                                             'total_marketing': total_marketing,
                                                             'total_tel_fx_mv': total_tel_fx_mv,
                                                             'total_desp_ti': total_desp_ti,
                                                             'total_tx_jur': total_tx_jur})



class EntradaCartaoList(LoginRequiredMixin, ListView):
    model = BaseCaixaRealizado

    def get_queryset(self):
        return BaseCaixaRealizado.objects.filter(classificacao_caixa='(+) Entradas Cartão')


class EntradaBoletoList(LoginRequiredMixin, ListView):
    model = BaseCaixaRealizado

    def get_queryset(self):
        return BaseCaixaRealizado.objects.filter(classificacao_caixa='(+) Entrada Boleto')


class EntradaRendimentosList(LoginRequiredMixin, ListView):
    model = BaseCaixaRealizado

    def get_queryset(self):
        return BaseCaixaRealizado.objects.filter(classificacao_caixa='(+) Rendimentos')


class ImpostosList(LoginRequiredMixin, ListView):
    model = BaseCaixaRealizado

    def get_queryset(self):
        return BaseCaixaRealizado.objects.filter(classificacao_caixa='(-) Impostos')


class CustoProdutosList(LoginRequiredMixin, ListView):
    model = BaseCaixaRealizado

    def get_queryset(self):
        return BaseCaixaRealizado.objects.filter(classificacao_caixa='( - ) Custo de Produtos')


class TransporteCorreiosList(LoginRequiredMixin, ListView):
    model = BaseCaixaRealizado

    def get_queryset(self):
        return BaseCaixaRealizado.objects.filter(classificacao_caixa='( - ) Transportes e Correios')


class DevolucoesList(LoginRequiredMixin, ListView):
    model = BaseCaixaRealizado

    def get_queryset(self):
        return BaseCaixaRealizado.objects.filter(classificacao_caixa='( - ) Devoluções')



class DespesasFolhaList(LoginRequiredMixin, ListView):
    model = BaseCaixaRealizado

    def get_queryset(self):
        return BaseCaixaRealizado.objects.filter(classificacao_caixa='( - ) Despesas de Folha')



class DespesasAdmList(LoginRequiredMixin, ListView):
    model = BaseCaixaRealizado

    def get_queryset(self):
        return BaseCaixaRealizado.objects.filter(classificacao_caixa='( -  ) Despesas Administrativas')



class MarketingList(LoginRequiredMixin, ListView):
    model = BaseCaixaRealizado

    def get_queryset(self):
        return BaseCaixaRealizado.objects.filter(classificacao_caixa='( - ) Marketing')



class TelMovFixList(LoginRequiredMixin, ListView):
    model = BaseCaixaRealizado

    def get_queryset(self):
        return BaseCaixaRealizado.objects.filter(classificacao_caixa='( - ) Telefonia Fixa e Móvel')



class DespTIList(LoginRequiredMixin, ListView):
    model = BaseCaixaRealizado

    def get_queryset(self):
        return BaseCaixaRealizado.objects.filter(classificacao_caixa='( - ) Despesas TI')



class TxJurosList(LoginRequiredMixin, ListView):
    model = BaseCaixaRealizado

    def get_queryset(self):
        return BaseCaixaRealizado.objects.filter(classificacao_caixa='( - ) Taxas/Juros')