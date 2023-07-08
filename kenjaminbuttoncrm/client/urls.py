from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    path('', views.clients_show, name='show'),
    path('<int:pk>/', views.clients_detail, name='detail'),
    path('<int:pk>/delete/', views.clients_delete, name='delete'),
    path('<int:pk>/edit/', views.clients_edit, name='edit'),
    path('add/', views.clients_add, name='add'),
]
