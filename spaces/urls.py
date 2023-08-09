from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("destination/<str:location>", views.get_spaces, name="get_spaces"),
]
