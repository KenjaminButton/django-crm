from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_clients, name='show_clients'),
    path('<int:pk>', views.clients_detail, name='clients_detail'),
]
