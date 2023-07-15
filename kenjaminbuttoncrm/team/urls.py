from django.urls import path

from . import views

app_name = 'team'

urlpatterns = [
    path('', views.teams_show, name='show'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit_team, name='edit'),
]
