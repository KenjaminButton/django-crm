from django.urls import path
from . import views

app_name = 'leads'

urlpatterns = [
    path('', views.show_leads, name='show'),
    path('<int:pk>/', views.leads_detail, name='detail'),
    path('<int:pk>/delete/', views.leads_delete, name='delete'),
    path('<int:pk>/edit/', views.leads_edit, name='edit'),
    path('<int:pk>/convert/', views.convert_to_client, name='convert'),
    path('addlead/', views.add_lead, name='addlead'),
]
