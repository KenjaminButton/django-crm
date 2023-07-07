from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Client
from .forms import AddClientForm


@login_required
def clients_add(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()
            messages.success(
                request, 'your client has been created successfully')
            return redirect('show_clients')
    else:
        form = AddClientForm()

    return render(request, 'client/clients_add.html', {
        'form': form
    })


@login_required
def show_clients(request):
    clients = Client.objects.filter(created_by=request.user)
    return render(request, 'client/show_clients.html', {
        'clients': clients
    })


@login_required
def clients_detail(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)

    return render(request, 'client/clients_detail.html', {
        'client': client
    })
