from django.urls import path
from .views import home_pachamama,\
    fluxo_de_caixa_pachamama, \
    EntradaCartaoList, \
    EntradaBoletoList, \
    EntradaRendimentosList, \
    ImpostosList, \
    CustoProdutosList, \
    TransporteCorreiosList, \
    DevolucoesList, \
    DespesasFolhaList, \
    DespesasAdmList, \
    MarketingList, \
    TelMovFixList, \
    DespTIList, \
    TxJurosList, \
    resultado_pachamama, \
    ProdutoList, \
    vendas_pachamama



urlpatterns = [
    path('', home_pachamama, name='home_pachamama'),
    path('resultado', resultado_pachamama, name='resultado_pachamama'),
    path('fluxo-caixa/', fluxo_de_caixa_pachamama, name='fluxo_caixa_pachamama'),
    path('entrada-cartao-list', EntradaCartaoList.as_view(), name='list_entrada_cartao'),
    path('entrada-boleto-list', EntradaBoletoList.as_view(), name='list_entrada_boleto'),
    path('entrada-rendimentos-list', EntradaRendimentosList.as_view(), name='list_entrada_rendimentos'),
    path('impostos-list', ImpostosList.as_view(), name='list_impostos'),
    path('custo-produtos-list', CustoProdutosList.as_view(), name='list_custo_produtos'),
    path('transporte-correios-list', TransporteCorreiosList.as_view(), name='list_transporte_correios'),
    path('devolucoes-list', DevolucoesList.as_view(), name='list_devolucoes'),
    path('desp-folha-list', DespesasFolhaList.as_view(), name='list_desp_folha'),
    path('desp-adm-list', DespesasAdmList.as_view(), name='list_desp_adm'),
    path('mkt-list', MarketingList.as_view(), name='list_mkt'),
    path('tel-mov-fix-list', TelMovFixList.as_view(), name='list_tel_fix_mov'),
    path('desp-ti-list', DespTIList.as_view(), name='list_desp_ti'),
    path('tx-juros-list', TxJurosList.as_view(), name='list_tx_juros'),

    path('produto-list', ProdutoList.as_view(), name='list_produto'),
    path('vendas', vendas_pachamama, name='vendas_pachamama'),



]
