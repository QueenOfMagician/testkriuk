from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/grup/<int:grup_id>/", views.gruphome, name='grup'),
]