from django.contrib import admin
from .models import Empresas, Usuario
from import_export.admin import ImportExportModelAdmin


@admin.register(Empresas, Usuario)
class ViewAdmin(ImportExportModelAdmin):
    pass

