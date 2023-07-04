from django.urls import path


from . import views


urlpatterns = [
    path('', views.show_leads, name='showleads'),
    path('addlead/', views.add_lead, name='addlead'),
]
