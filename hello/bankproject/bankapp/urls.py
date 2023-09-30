from . import views
from django.urls import path

urlpatterns = [
    path("", views.base, name="base"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('app', views.app, name="app"),
    path('end', views.end, name="end"),

]
