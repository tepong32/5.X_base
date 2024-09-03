
from django.urls import path, include
from .views import homeView

urlpatterns = [
    path('', homeView, name="home"),
    path('<username>/', views.profile, name='profile' ),
    path('<username>/edit/', views.profile_edit, name='profile-edit' ),
]
