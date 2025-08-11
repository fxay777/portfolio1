from django.db import models

class PortfolioProject(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    link = models.URLField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Projeto de Portfólio"
        verbose_name_plural = "Projetos de Portfólio"
        ordering = ["-data_criacao"]

    def __str__(self):
        return self.titulo
