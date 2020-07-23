from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import ListView
from apps.pachamama.models import BaseCaixaRealizado

@login_required
def home_pachamama(request):
    return render(request, 'pachamama/index.html')



@login_required
def resultado_pachamama(request):
    return render(request, 'pachamama/resultado.html')



@login_required
def fluxo_de_caixa_pachamama(request):

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

    entrada_cartao_realizado = []
    entrada_boleto_realizado = []
    entrada_rendimentos_realizado = []
    saida_imposto_realizado = []
    saida_custo_producao_realizado = []
    saida_trans_correios_realizado = []
    saida_devolucoes_realizado = []
    saida_desp_folha_realizado = []
    saida_desp_adm_realizado = []
    saida_mkt_realizado = []
    saida_tel_realizado =[]
    saida_desp_ti_realizado = []
    saida_tx_juros_realizado = []

    # Entradas

    for mes in MES_PAGAMENTO:
        cartao_lan = BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                       classificacao_caixa=CLASSIFICACAO_CAIXA['entrada_cartao'],
                                                       mes_pagamento=mes, ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']
        entrada_cartao_realizado.append(cartao_lan)


    for mes in MES_PAGAMENTO:
        cartao_lan = BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                       classificacao_caixa=CLASSIFICACAO_CAIXA['entrada_boleto'],
                                                       mes_pagamento=mes, ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']
        entrada_boleto_realizado.append(cartao_lan)


    for mes in MES_PAGAMENTO:
        cartao_lan = BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                       classificacao_caixa=CLASSIFICACAO_CAIXA['rendimentos'],
                                                       mes_pagamento=mes, ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']
        entrada_rendimentos_realizado.append(cartao_lan)


    for mes in MES_PAGAMENTO:
        cartao_lan = BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                       classificacao_caixa=CLASSIFICACAO_CAIXA['impostos'],
                                                       mes_pagamento=mes, ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']
        saida_imposto_realizado.append(cartao_lan)


    # Custos


    for mes in MES_PAGAMENTO:
        cartao_lan = BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                       classificacao_caixa=CLASSIFICACAO_CAIXA['custo_produto'],
                                                       mes_pagamento=mes, ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']
        saida_custo_producao_realizado.append(cartao_lan)


    for mes in MES_PAGAMENTO:
        cartao_lan = BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                       classificacao_caixa=CLASSIFICACAO_CAIXA['trans_correrios'],
                                                       mes_pagamento=mes, ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']
        saida_trans_correios_realizado.append(cartao_lan)


    for mes in MES_PAGAMENTO:
        cartao_lan = BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                       classificacao_caixa=CLASSIFICACAO_CAIXA['devolucoes'],
                                                       mes_pagamento=mes, ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']
        saida_devolucoes_realizado.append(cartao_lan)


    # Despesas


    for mes in MES_PAGAMENTO:
        cartao_lan = BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                       classificacao_caixa=CLASSIFICACAO_CAIXA['desp_folha'],
                                                       mes_pagamento=mes, ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']
        saida_desp_folha_realizado.append(cartao_lan)


    for mes in MES_PAGAMENTO:
        cartao_lan = BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                       classificacao_caixa=CLASSIFICACAO_CAIXA['desp_adm'],
                                                       mes_pagamento=mes, ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']
        saida_desp_adm_realizado.append(cartao_lan)


    for mes in MES_PAGAMENTO:
        cartao_lan = BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                       classificacao_caixa=CLASSIFICACAO_CAIXA['marketing'],
                                                       mes_pagamento=mes, ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']
        saida_mkt_realizado.append(cartao_lan)


    for mes in MES_PAGAMENTO:
        cartao_lan = BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                       classificacao_caixa=CLASSIFICACAO_CAIXA['tel_fx_mv'],
                                                       mes_pagamento=mes, ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']
        saida_tel_realizado.append(cartao_lan)


    for mes in MES_PAGAMENTO:
        cartao_lan = BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                       classificacao_caixa=CLASSIFICACAO_CAIXA['desp_ti'],
                                                       mes_pagamento=mes, ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']
        saida_desp_ti_realizado.append(cartao_lan)


    for mes in MES_PAGAMENTO:
        cartao_lan = BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                       classificacao_caixa=CLASSIFICACAO_CAIXA['tx_jur'],
                                                       mes_pagamento=mes, ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']
        saida_tx_juros_realizado.append(cartao_lan)

    # Totais

    total_receita_realizado = [(a + b + c + d) for a, b, c, d in zip(entrada_cartao_realizado,
                                                                     entrada_boleto_realizado,
                                                                     entrada_rendimentos_realizado,
                                                                     saida_imposto_realizado)]


    total_custo_realizado = [(a + b + c) for a, b, c in zip(saida_custo_producao_realizado,
                                                            saida_trans_correios_realizado,
                                                            saida_devolucoes_realizado)]


    total_despesas_realizado = [(a + b + c + d + e + f) for a, b, c, d, e, f in zip(saida_desp_folha_realizado,
                                                                                    saida_desp_adm_realizado,
                                                                                    saida_mkt_realizado,
                                                                                    saida_tel_realizado,
                                                                                    saida_desp_ti_realizado,
                                                                                    saida_tx_juros_realizado)]


    fluxo_de_caixa_realizado = [(a + b + c) for a, b, c in zip(total_receita_realizado,
                                                               total_custo_realizado,
                                                               total_despesas_realizado)]



    return render(request, 'pachamama/fluxo_de_caixa.html', {'entrada_cartao_realizado': entrada_cartao_realizado,
                                                             'entrada_boleto_realizado': entrada_boleto_realizado,
                                                             'entrada_rendimentos_realizado': entrada_rendimentos_realizado,
                                                             'saida_imposto_realizado': saida_imposto_realizado,

                                                             'saida_custo_producao_realizado': saida_custo_producao_realizado,
                                                             'saida_trans_correios_realizado': saida_trans_correios_realizado,
                                                             'saida_devolucoes_realizado': saida_devolucoes_realizado,

                                                             'saida_desp_folha_realizado': saida_desp_folha_realizado,
                                                             'saida_desp_adm_realizado': saida_desp_adm_realizado,
                                                             'saida_mkt_realizado': saida_mkt_realizado,
                                                             'saida_tel_realizado': saida_tel_realizado,
                                                             'saida_desp_ti_realizado': saida_desp_ti_realizado,
                                                             'saida_tx_juros_realizado': saida_tx_juros_realizado,

                                                             'total_receita_realizado': total_receita_realizado,
                                                             'total_custo_realizado': total_custo_realizado,
                                                             'total_despesas_realizado': total_despesas_realizado,
                                                             'fluxo_de_caixa_realizado': fluxo_de_caixa_realizado})



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