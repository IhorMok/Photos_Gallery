from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('about/', views.about, name='about'),
    path('register/', views.register_page, name='register'),
]
