from django.db import models


class BaseCaixaRealizado(models.Model):
    situacao = models.CharField(max_length=240)
    classificacao_caixa = models.CharField(max_length=240)
    dia_pagamento = models.DecimalField(max_digits=2, decimal_places=0)
    mes_pagamento = models.DecimalField(max_digits=2, decimal_places=0)
    ano_pagamento = models.DecimalField(max_digits=4, decimal_places=0)
    classificacao_resultado = models.CharField(max_length=240)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    cliente = models.CharField(max_length=240)
    data = models.DateField()

    def __str__(self):
        return self.situacao



class BaseVendasRealizadas(models.Model):
    situacao_faturamento_2 = models.CharField(max_length=240)
    cliente_faturamento_2 = models.CharField(max_length=1000)
    pedido_vendas_2 = models.DecimalField(max_digits=100000, decimal_places=0)
    produto_2 = models.CharField(max_length=1000)
    ano_faturamento_2 = models.DecimalField(max_digits=4, decimal_places=0)
    dia_faturamento_2 = models.DecimalField(max_digits=2, decimal_places=0)
    mes_faturamento_2 = models.DecimalField(max_digits=2, decimal_places=0)
    quantidade_2 = models.DecimalField(max_digits=100, decimal_places=0)
    total_mercadoria_2 = models.DecimalField(max_digits=10000, decimal_places=2)
    desconto_2 = models.DecimalField(max_digits=10000, decimal_places=2)
    valor_icms_st_2 = models.DecimalField(max_digits=10000, decimal_places=2)
    frete_2 = models.DecimalField(max_digits=10000, decimal_places=2)
    seguro_2 = models.DecimalField(max_digits=10000, decimal_places=2)
    outras_desp_2 = models.DecimalField(max_digits=10000, decimal_places=2)
    valor_ipi_2 = models.DecimalField(max_digits=10000, decimal_places=2)
    notal_nf_2 = models.DecimalField(max_digits=10000, decimal_places=2)
    valor_icms_2 = models.DecimalField(max_digits=10000, decimal_places=2)
    valor_pis_2 = models.DecimalField(max_digits=10000, decimal_places=2)
    valor_cofins_2 = models.DecimalField(max_digits=10000, decimal_places=2)
    classificacao_resultado_faturamento_2 = models.CharField(max_length=240)
    data_faturamento_2 = models.DateField()
    valor_cmv_unit_2 = models.DecimalField(max_digits=1000, decimal_places=2)
    valor_cmv_total_2 = models.DecimalField(max_digits=1000, decimal_places=2)


    def __str__(self):
        return self.cliente_faturamento_2