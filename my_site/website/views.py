#Esse Arquivo vai realizar as operações de CRUD
from django.http import request
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DeleteView, CreateView, UpdateView, ListView
from my_site.models import Aluno
from website.forms import InsereAlunoForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render


#Página de Login
class IndexTemplateView(TemplateView):
    template_name = "website/index.html"
    context_object_name = "aluno"

class ErroLogin(TemplateView):
    template_name = "website/erro.html"

#Cadastra alunos 
#C do Crud
class AlunoCreateView(CreateView):
    template_name = "website/cria.html"
    model = Aluno
    form_class = InsereAlunoForm
    context_object_name = "aluno"
    success_url = reverse_lazy("website:lista_aluno")

#Listagem de alunos
#R do cRud
class AlunoListView(ListView):
    template_name = "website/lista.html"
    model = Aluno
    context_object_name = "alunos"

#Atualiza Alunos
#U do crUd
class AlunoUpdateView(UpdateView):
    template_name = "website/atualiza.html"
    model = Aluno
    context_object_name = "aluno"
    fields = "__all__"
    success_url = reverse_lazy("website:lista_aluno")

#Deleta Alunos 
#D do cruD
class AlunoDeleteView(DeleteView):
    template_name = "website/remove.html"
    model = Aluno
    context_object_name = "aluno"
    success_url = reverse_lazy("website:lista_aluno")


#Realiza login
def Login(request):
    template_name = 'website/login.html'

    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('website:perfil_aluno')

        else:
            return redirect('website:erro_login')

    return render(request, template_name, {})

