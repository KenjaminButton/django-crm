from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import AddLeadForm
from .models import Lead
from team.models import Team
from client.models import Client


@login_required
def convert_to_client(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    team = Team.objects.filter(created_by=request.user)[0]

    client = Client.objects.create(
        name=lead.name,
        email=lead.email,
        description=lead.description,
        created_by=request.user,
        team=team,
    )
    lead.converted_to_client = True
    lead.save()
    messages.success(request, 'lead has been converted to a client')
    return redirect('leads:show')


@login_required
def leads_detail(request, pk):
    # Django shortcut for the same functionality as below
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    # lead = Lead.objects.filter(created_by=request.user).get(pk=pk)
    return render(request, 'lead/leadsdetail.html', {
        'lead': lead
    })


@login_required
def leads_edit(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

    if request.method == 'POST':
        form = AddLeadForm(request.POST, instance=lead)

        if form.is_valid():
            form.save()
            messages.success(
                request, 'your lead has been edited successfully and saved')
            return redirect('leads:show')
    else:
        form = AddLeadForm(instance=lead)

    return render(request, 'lead/leadsedit.html', {
        'form': form
    })


@login_required
def leads_delete(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    lead.delete()
    messages.success(request, 'your lead has been deleted')
    return redirect('leads:show')


@login_required
def show_leads(request):
    leads = Lead.objects.filter(
        created_by=request.user, converted_to_client=False)
    return render(request, 'lead/showleads.html', {
        'leads': leads
    })


@login_required
def add_lead(request):
    team = Team.objects.filter(created_by=request.user)[0]
    if request.method == 'POST':
        form = AddLeadForm(request.POST)
        if form.is_valid():
            team = Team.objects.filter(created_by=request.user)[0]
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.team = team
            lead.save()
            messages.success(
                request, 'your lead has been created successfully')
            return redirect('leads:show')
    else:
        form = AddLeadForm()

    return render(request, 'lead/addlead.html', {
        'form': form,
        'team': team
    })
