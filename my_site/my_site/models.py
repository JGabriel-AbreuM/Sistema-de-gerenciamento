from django.db import models
from django.db.models.aggregates import Max

class Aluno(models.Model):
    
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False,
    )

    curso = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )

    periodo = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    email = models.EmailField(
        max_length=255,
        blank=False,
        null=False
    )

    password = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )
    objeto = models.Manager()