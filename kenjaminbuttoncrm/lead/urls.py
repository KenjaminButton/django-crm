from django.urls import path


from . import views


urlpatterns = [
    path('addlead/', views.add_lead, name='addlead')
]
