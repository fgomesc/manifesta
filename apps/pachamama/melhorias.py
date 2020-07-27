from django.core.serializers import json
from django.shortcuts import render

from apps.pachamama.models import BaseVendasRealizadas


def vendas_pachamama(request):

    queryset = BaseVendasRealizadas.objects.all()
    mes = [int(obj.mes_faturamento_2) for obj in queryset]
    valor = [int(obj.total_mercadoria_2) for obj in queryset]

    context ={

        'mes': json.dumps(mes),
        'valor': json.dumps(valor),
    }


    return render(request, 'pachamama/vendas.html', context)

