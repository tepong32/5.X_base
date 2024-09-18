
from django.urls import path, include
from .views import homeView, profile, profile_edit

urlpatterns = [
    path('', homeView, name="home"),
    path('<username>/', profile, name='profile' ),
    path('<username>/edit/', profile_edit, name='profile-edit' ),
]
