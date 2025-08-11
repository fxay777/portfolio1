from django.contrib import admin

# Register your models here.
from .models import Post

from django.contrib import admin
from .models import PortfolioProject

@admin.register(PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ("titulo", "data_criacao", "data_atualizacao")
    search_fields = ("titulo", "descricao")
