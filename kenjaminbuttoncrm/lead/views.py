from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import AddLeadForm
from .models import Lead


@login_required
def leads_detail(request, pk):
    # Django shortcut for the same functionality as below
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    # lead = Lead.objects.filter(created_by=request.user).get(pk=pk)
    return render(request, 'lead/leadsdetail.html', {
        'lead': lead
    })


@login_required
def show_leads(request):
    leads = Lead.objects.filter(created_by=request.user)
    return render(request, 'lead/showleads.html', {
        'leads': leads
    })


@login_required
def add_lead(request):
    if request.method == 'POST':
        form = AddLeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()

            return redirect('dashboard')
    else:
        form = AddLeadForm()

    return render(request, 'lead/addlead.html', {
        'form': form
    })
