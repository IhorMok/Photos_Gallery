from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('about/', views.about, name='about'),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('page-user/', views.page_user, name='page_user'),
    path('create-album/', views.create_album, name='create_album'),
]
