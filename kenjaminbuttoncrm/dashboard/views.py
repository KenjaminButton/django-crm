from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from lead.models import Lead
from client.models import Client
from team.models import Team


@login_required
def dashboard(request):
    # team = Team.objects.filter(created_by=request.user)[0]
    team_queryset = Team.objects.filter(created_by=request.user)
    team = team_queryset.first() if team_queryset.exists() else None

    # Filter out everyone connected to team
    leads = Lead.objects.filter(
        team=team, converted_to_client=False).order_by('-created_at')[0:5]
    clients = Client.objects.filter(team=team).order_by('-created_at')[0:5]

    return render(request, 'dashboard/dashboard.html', {
        'leads': leads,
        'clients': clients,
    })
