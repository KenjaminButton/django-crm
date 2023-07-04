from django.urls import path


from . import views


urlpatterns = [
    path('', views.show_leads, name='showleads'),
    path('<int:pk>/', views.leads_detail, name='leadsdetail'),
    path('<int:pk>/delete/', views.leads_delete, name='leads_delete'),
    path('<int:pk>/edit/', views.leads_edit, name='leads_edit'),
    path('addlead/', views.add_lead, name='addlead'),
]
