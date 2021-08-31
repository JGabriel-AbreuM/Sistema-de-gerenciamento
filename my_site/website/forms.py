from django.db import models
from my_site.models import Aluno
from django import forms

#Inscrição de funcionário
class InsereAlunoForm(forms.ModelForm):    
    class Meta:
        model = Aluno

        fields = [
            "nome",
            "sobrenome",
            "cpf",
            "curso",
            "periodo",
            "email",
            "password"
        ]