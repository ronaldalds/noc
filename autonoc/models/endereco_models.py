from django.db import models

class Operacao(models.Model):
    nome = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "Operações"
    
    def __str__(self) -> str:
        return self.nome

class Estado(models.Model):
    nome = models.CharField(max_length=128)
    uf = models.CharField(max_length=2)
    operacao = models.ForeignKey(Operacao, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Estados"
    
    def __str__(self) -> str:
        return self.uf

class Cidade(models.Model):
    nome = models.CharField(max_length=128)
    sigla = models.CharField(max_length=3)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Cidades"
    
    def __str__(self) -> str:
        return f"{self.nome} - {self.estado.uf}"