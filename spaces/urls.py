from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addspace/", views.add_space, name="add_space"),
]
