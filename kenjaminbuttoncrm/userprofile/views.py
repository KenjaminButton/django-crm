from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from django.shortcuts import render, redirect
from .models import Userprofile
from team.models import Team


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()

            team = Team.objects.create(
                name='The team name', created_by=user)
            team.members.add(user)
            team.save()

            # userprofile = Userprofile.objects.create(user=user)
            Userprofile.objects.create(user=user, active_team=team)

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'userprofile/signup.html', {
        'form': form
    })


@login_required
def myaccount(request):
    team = Team.objects.filter(created_by=request.user)[0]
    # team_queryset = Team.objects.filter(created_by=request.user)
    # team = team_queryset.first() if team_queryset.exists() else None

    return render(request, 'userprofile/myaccount.html', {
        'team': team
    })
