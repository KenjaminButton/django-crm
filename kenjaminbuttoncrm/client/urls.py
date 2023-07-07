from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_clients, name='show_clients'),
    path('<int:pk>/', views.clients_detail, name='clients_detail'),
    path('<int:pk>/delete/', views.clients_delete, name='clients_delete'),
    path('<int:pk>/edit/', views.clients_edit, name='clients_edit'),
    path('add/', views.clients_add, name='clients_add'),
]
