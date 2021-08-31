from django.urls import path
from website.views import IndexTemplateView, AlunoListView, \
    AlunoUpdateView, AlunoCreateView, AlunoDeleteView, Login, ErroLogin

from . import views
app_name = "website"

urlpatterns = [
    path("", views.Login, name="login"),
    path("perfil/<pk>", IndexTemplateView.as_view(), name="perfil_aluno"),
    path("aluno/cadastrar", AlunoCreateView.as_view(), name="cadastra_aluno"),
    path("erro", ErroLogin.as_view(), name="erro_login" ),
    path("aluno/", AlunoListView.as_view(), name="lista_aluno"),
    path("aluno/<pk>", AlunoUpdateView.as_view(), name="atualiza_aluno"),
    path("aluno/excluir/<pk>", AlunoDeleteView.as_view(), name="deleta_aluno"),
]