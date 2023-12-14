from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("forms-colaborador", views.formsColaborador, name="formsColaborador"),
    path("forms-usuario", views.formsUsuario, name="formsUsuario"),
    path("formspostusuario", views.forms_post_usuario, name="forms_post_usuario"),
    path("formspostcolaborador", views.forms_post_colaborador, name="forms_post_colaborador"),
    path("lista", views.lista, name="lista"),
    path("<int:chamado_id>", views.detail, name="detail"),
    path("relatorio", views.relatorio, name="relatorio"),
    path("login", views.login, name="login")
]