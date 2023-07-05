from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Client


@login_required
def show_clients(request):
    clients = Client.objects.filter(created_by=request.user)
    return render(request, 'client/show_clients.html', {
        'clients': clients
    })
