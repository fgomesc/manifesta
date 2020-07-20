from django.contrib import admin
from .models import BaseCaixaRealizado
from import_export.admin import ImportExportModelAdmin


@admin.register(BaseCaixaRealizado)
class ViewAdmin(ImportExportModelAdmin):
    pass


