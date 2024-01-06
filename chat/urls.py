from django.urls import path
from . import views

urlpatterns = [
    path('', views.lobby, name='lobby'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    # path('lobby/', views.lobby, name='lobby'),
]