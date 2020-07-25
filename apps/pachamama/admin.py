from django.contrib import admin
from .models import BaseCaixaRealizado, BaseVendasRealizadas
from import_export.admin import ImportExportModelAdmin


@admin.register(BaseCaixaRealizado, BaseVendasRealizadas)
class ViewAdmin(ImportExportModelAdmin):
    pass



