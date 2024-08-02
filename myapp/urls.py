from . import views
from django.urls import path

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home_page, name='home_page'),
    path('register', views.registration, name='registration'),
]