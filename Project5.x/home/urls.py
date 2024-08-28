from django.contrib.auth import views as auth_views     # for auths for logins and logouts
from django.urls import path, include
from .views import homeView

urlpatterns = [
    path('', homeView, name="home"),
]
