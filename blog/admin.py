from django.contrib import admin
from .models import Post, PortfolioProject

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "autor", "criado_em")  # ajuste os nomes dos campos conforme estão no seu models.py
    search_fields = ("titulo", "conteudo")
    list_filter = ("criado_em", "autor")

@admin.register(PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ("titulo", "data_criacao", "data_atualizacao")
    search_fields = ("titulo", "descricao")
