from django.db import models


class BaseCaixaRealizado(models.Model):
    situacao = models.CharField(max_length=240, null=True, blank=True, default=0)
    classificacao_caixa = models.CharField(max_length=240, default=0)
    dia_pagamento = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    mes_pagamento = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    ano_pagamento = models.DecimalField(max_digits=4, decimal_places=0, default=0)
    classificacao_resultado = models.CharField(max_length=240, default=0)
    valor = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    cliente = models.CharField(max_length=240, default=0)
    data = models.DateField(default=0)

    def __str__(self):
        return self.situacao



class BaseVendasRealizadas(models.Model):
    situacao_faturamento_2 = models.CharField(max_length=240, default=0)
    cliente_faturamento_2 = models.CharField(max_length=1000, default=0)
    pedido_vendas_2 = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    produto_2 = models.CharField(max_length=1000, default=0)
    ano_faturamento_2 = models.DecimalField(max_digits=4, decimal_places=0, default=0)
    dia_faturamento_2 = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    mes_faturamento_2 = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    quantidade_2 = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    total_mercadoria_2 = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    desconto_2 = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    valor_icms_st_2 = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    frete_2 = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    seguro_2 = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    outras_desp_2 = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    valor_ipi_2 = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    notal_nf_2 = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    valor_icms_2 = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    valor_pis_2 = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    valor_cofins_2 = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    classificacao_resultado_faturamento_2 = models.CharField(max_length=240, default=0)
    data_faturamento_2 = models.DateField(default=0)
    valor_cmv_unit_2 = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    valor_cmv_total_2 = models.DecimalField(max_digits=7, decimal_places=2, default=0)


    def __str__(self):
        return self.situacao_faturamento_2