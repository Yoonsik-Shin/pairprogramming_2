from django.urls import path
from . import views

app_name = "movie_crud"
urlpatterns = [
    path("", views.main, name="main"),
    path("index/", views.index, name="index"),
    path("create/", views.create, name="create"),
]
