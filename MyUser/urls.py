from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('homepage', views.homepage, name='homepage'),
    path('additional', views.add_info, name='additional'),
]