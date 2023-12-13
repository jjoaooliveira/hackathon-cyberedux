from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("forms", views.forms, name="forms"),
    path("formspost/", views.forms_post, name="forms_post"),
    path("lista", views.lista, name="lista"),
    path("<int:denunciante_id>/", views.detail, name="detail")
]