from django.urls import path


from . import views


urlpatterns = [
    path('', views.show_leads, name='showleads'),
    path('<int:pk>/', views.leads_detail, name='leadsdetail'),
    path('addlead/', views.add_lead, name='addlead'),
]
