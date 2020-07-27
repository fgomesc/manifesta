from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import ListView
from apps.pachamama.models import BaseCaixaRealizado, BaseVendasRealizadas

@login_required
def home_pachamama(request):
    return render(request, 'pachamama/index.html')



@login_required
def vendas_pachamama(request):




    return render(request, 'pachamama/vendas.html')





@login_required
def resultado_pachamama(request):

    STATUS = {
        'status_1': 'Conciliado'
    }


    CLASSIFICACAO_RESULTADO = {
        'produtos': '( + ) Produtos',
    }


    MES_PAGAMENTO = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        '11': 11,
        '12': 12,
    }

    taxa_imposto = 0.083

    produtos = []
    insumos = []
    frete = []
    folha =[]
    ocupacao = []
    marketing = []
    consul_asse = []
    demais_desp = []

    # ( + ) Produtos

    for mes in MES_PAGAMENTO:
        cartao_lan = int(BaseVendasRealizadas.objects.filter(situacao_faturamento_2=STATUS['status_1'],
                                                             classificacao_resultado_faturamento_2=CLASSIFICACAO_RESULTADO['produtos'],
                                                             mes_faturamento_2=mes,
                                                             ano_faturamento_2='2020').aggregate(Sum('total_mercadoria_2'))['total_mercadoria_2__sum'])
        produtos.append(cartao_lan)

    # ( - ) Impostos

    impostos = [(int(a * taxa_imposto) * (-1)) for a in produtos]

    # ( - ) Insumos
    for mes in MES_PAGAMENTO:
        cartao_lan = int(BaseVendasRealizadas.objects.filter(situacao_faturamento_2=STATUS['status_1'],
                                                             classificacao_resultado_faturamento_2=CLASSIFICACAO_RESULTADO['produtos'],
                                                             mes_faturamento_2=mes,
                                                             ano_faturamento_2='2020').aggregate(Sum('valor_cmv_total_2'))['valor_cmv_total_2__sum']) * (-1)
        insumos.append(cartao_lan)

    # ( - ) Frete
    for mes in MES_PAGAMENTO:
        cartao_lan = int(BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                           classificacao_caixa='( - ) Transportes e Correios',
                                                           mes_pagamento=mes,
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum'])
        frete.append(cartao_lan)


    # ( - ) Folha
    for mes in MES_PAGAMENTO:
        cartao_lan = int(BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                           classificacao_caixa='( - ) Despesas de Folha',
                                                           mes_pagamento=mes,
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum'])
        folha.append(cartao_lan)


    # ( - ) Ocupação
    for mes in MES_PAGAMENTO:
        cartao_lan = int(BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                           classificacao_caixa='( -  ) Despesas Administrativas',
                                                           mes_pagamento=mes,
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum'])
        ocupacao.append(cartao_lan)


    # ( - ) Marketing
    for mes in MES_PAGAMENTO:
        cartao_lan = int(BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                           classificacao_caixa='( - ) Marketing',
                                                           mes_pagamento=mes,
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum'])
        marketing.append(cartao_lan)

    # ( - ) Consultoria e Assessoria
    for mes in MES_PAGAMENTO:
        cartao_lan = int(BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                           classificacao_caixa='( - ) Telefonia Fixa e Móvel',
                                                           mes_pagamento=mes,
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum']) + \
                     int(BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                           classificacao_caixa='( - ) Despesas TI',
                                                           mes_pagamento=mes,
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum'])
        consul_asse.append(cartao_lan)

    # ( - ) Demais Despesas
    for mes in MES_PAGAMENTO:
        cartao_lan = int(BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                           classificacao_caixa='( - ) Taxas/Juros',
                                                           mes_pagamento=mes,
                                                           ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum'])
        demais_desp.append(cartao_lan)

    # Receita Bruta

    receita_bruta = [(a + b) for a, b in zip(produtos, impostos)]

    # Custos Operacionais

    custos_operacionais = [(a + b) for a, b in zip(insumos, frete)]

    # Resultado Operacional

    result_operacional = [(a + b) for a, b in zip(receita_bruta, custos_operacionais)]

    # Total Despesas

    total_desp = [(a + b + c + d + e) for a, b, c, d, e in zip(folha, ocupacao, marketing, consul_asse, demais_desp)]

    # EBITDA

    ebitda = [(a + b) for a, b in zip(result_operacional, total_desp)]

    total_receita_bruta = sum(receita_bruta)
    total_impostos = sum(impostos)
    total_receita_liquida = sum(receita_bruta)
    total_custos = sum(custos_operacionais)
    total_insumos = sum(insumos)
    total_frete = sum(frete)
    total_resultado_operacional = sum(result_operacional)
    total_despesas = sum(total_desp)
    total_folha = sum(folha)
    total_ocupacao = sum(ocupacao)
    total_marketing = sum(marketing)
    total_consul_asse = sum(consul_asse)
    total_demais_desp = sum(demais_desp)
    total_ebitda = sum(ebitda)


    return render(request, 'pachamama/resultado.html', {'produtos': produtos,
                                                        'impostos': impostos,
                                                        'insumos': insumos,
                                                        'frete': frete,
                                                        'folha': folha,
                                                        'ocupacao': ocupacao,
                                                        'marketing': marketing,
                                                        'consul_asse': consul_asse,
                                                        'demais_desp': demais_desp,

                                                        'receita_bruta': receita_bruta,
                                                        'custos_operacionais': custos_operacionais,
                                                        'result_operacional': result_operacional,
                                                        'total_desp': total_desp,
                                                        'ebitda': ebitda,

                                                        'total_receita_bruta': total_receita_bruta,
                                                        'total_impostos': total_impostos,
                                                        'total_receita_liquida': total_receita_liquida,
                                                        'total_custos': total_custos,
                                                        'total_insumos': total_insumos,
                                                        'total_frete': total_frete,
                                                        'total_resultado_operacional': total_resultado_operacional,
                                                        'total_despesas': total_despesas,
                                                        'total_folha': total_folha,
                                                        'total_ocupacao': total_ocupacao,
                                                        'total_marketing': total_marketing,
                                                        'total_consul_asse': total_consul_asse,
                                                        'total_demais_desp': total_demais_desp,
                                                        'total_ebitda': total_ebitda})

class ProdutoList(LoginRequiredMixin, ListView):
    model = BaseVendasRealizadas

    def get_queryset(self):
        return BaseVendasRealizadas.objects.filter(classificacao_resultado_faturamento_2='( + ) Produtos')




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
        cartao_lan = int(BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                       classificacao_caixa=CLASSIFICACAO_CAIXA['entrada_cartao'],
                                                       mes_pagamento=mes, ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum'])
        entrada_cartao_realizado.append(cartao_lan)


    for mes in MES_PAGAMENTO:
        cartao_lan = int(BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                       classificacao_caixa=CLASSIFICACAO_CAIXA['entrada_boleto'],
                                                       mes_pagamento=mes, ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum'])
        entrada_boleto_realizado.append(cartao_lan)


    for mes in MES_PAGAMENTO:
        cartao_lan = int(BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                       classificacao_caixa=CLASSIFICACAO_CAIXA['rendimentos'],
                                                       mes_pagamento=mes, ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum'])
        entrada_rendimentos_realizado.append(cartao_lan)


    for mes in MES_PAGAMENTO:
        cartao_lan = int(BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                       classificacao_caixa=CLASSIFICACAO_CAIXA['impostos'],
                                                       mes_pagamento=mes, ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum'])
        saida_imposto_realizado.append(cartao_lan)


    # Custos


    for mes in MES_PAGAMENTO:
        cartao_lan = int(BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                       classificacao_caixa=CLASSIFICACAO_CAIXA['custo_produto'],
                                                       mes_pagamento=mes, ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum'])
        saida_custo_producao_realizado.append(cartao_lan)


    for mes in MES_PAGAMENTO:
        cartao_lan = int(BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                       classificacao_caixa=CLASSIFICACAO_CAIXA['trans_correrios'],
                                                       mes_pagamento=mes, ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum'])
        saida_trans_correios_realizado.append(cartao_lan)


    for mes in MES_PAGAMENTO:
        cartao_lan = int(BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                       classificacao_caixa=CLASSIFICACAO_CAIXA['devolucoes'],
                                                       mes_pagamento=mes, ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum'])
        saida_devolucoes_realizado.append(cartao_lan)


    # Despesas


    for mes in MES_PAGAMENTO:
        cartao_lan = int(BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                       classificacao_caixa=CLASSIFICACAO_CAIXA['desp_folha'],
                                                       mes_pagamento=mes, ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum'])
        saida_desp_folha_realizado.append(cartao_lan)


    for mes in MES_PAGAMENTO:
        cartao_lan = int(BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                       classificacao_caixa=CLASSIFICACAO_CAIXA['desp_adm'],
                                                       mes_pagamento=mes, ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum'])
        saida_desp_adm_realizado.append(cartao_lan)


    for mes in MES_PAGAMENTO:
        cartao_lan = int(BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                       classificacao_caixa=CLASSIFICACAO_CAIXA['marketing'],
                                                       mes_pagamento=mes, ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum'])
        saida_mkt_realizado.append(cartao_lan)


    for mes in MES_PAGAMENTO:
        cartao_lan = int(BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                       classificacao_caixa=CLASSIFICACAO_CAIXA['tel_fx_mv'],
                                                       mes_pagamento=mes, ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum'])
        saida_tel_realizado.append(cartao_lan)


    for mes in MES_PAGAMENTO:
        cartao_lan = int(BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                       classificacao_caixa=CLASSIFICACAO_CAIXA['desp_ti'],
                                                       mes_pagamento=mes, ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum'])
        saida_desp_ti_realizado.append(cartao_lan)


    for mes in MES_PAGAMENTO:
        cartao_lan = int(BaseCaixaRealizado.objects.filter(situacao=STATUS['status_1'],
                                                       classificacao_caixa=CLASSIFICACAO_CAIXA['tx_jur'],
                                                       mes_pagamento=mes, ano_pagamento='2020').aggregate(Sum('valor'))['valor__sum'])
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
    total_receitas = sum(total_receita_realizado)
    total_cartao_realizado = sum(entrada_cartao_realizado)
    total_boletos = sum(entrada_boleto_realizado)
    total_rendimentos = sum(entrada_rendimentos_realizado)
    total_impostos = sum(saida_imposto_realizado)
    total_custo = sum(total_custo_realizado)
    total_custo_produto = sum(saida_custo_producao_realizado)
    total_trans_correios = sum(saida_trans_correios_realizado)
    total_devolucoes = sum(saida_devolucoes_realizado)
    total_desp = sum(total_despesas_realizado)
    total_folha = sum(saida_desp_folha_realizado)
    total_desp_adm = sum(saida_desp_adm_realizado)
    total_marketing = sum(saida_mkt_realizado)
    total_tel = sum(saida_tel_realizado)
    total_desp_ti = sum(saida_desp_ti_realizado)
    total_tx_juros = sum(saida_tx_juros_realizado)
    total_fluxo_caixa = sum(fluxo_de_caixa_realizado)

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
                                                             'fluxo_de_caixa_realizado': fluxo_de_caixa_realizado,

                                                             'total_cartao_realizado': total_cartao_realizado,
                                                             'total_receitas': total_receitas,
                                                             'total_boletos': total_boletos,
                                                             'total_rendimentos': total_rendimentos,
                                                             'total_impostos': total_impostos,
                                                             'total_custo': total_custo,
                                                             'total_custo_produto': total_custo_produto,
                                                             'total_trans_correios': total_trans_correios,
                                                             'total_devolucoes': total_devolucoes,
                                                             'total_desp': total_desp,
                                                             'total_folha': total_folha,
                                                             'total_desp_adm': total_desp_adm,
                                                             'total_marketing': total_marketing,
                                                             'total_tel': total_tel,
                                                             'total_desp_ti': total_desp_ti,
                                                             'total_fluxo_caixa': total_fluxo_caixa,
                                                             'total_tx_juros': total_tx_juros})



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