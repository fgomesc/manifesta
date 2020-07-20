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


