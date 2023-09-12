from django.urls import path
from . import views

urlpatterns = [
    path("signin/", views.SignIn, name="signin"),
    path("signup/", views.SingUp, name="signup"),
    path("logout/", views.logoutpage, name="logout"),
]