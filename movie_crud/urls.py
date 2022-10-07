from django.urls import path
from . import views

app_name = "movie_crud"
urlpatterns = [
    path("", views.index, name="index"),
]
