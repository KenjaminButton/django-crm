from team.models import Team


def active_team(request):
    active_team = None
    if request.user.is_authenticated:
        teams = Team.objects.filter(created_by=request.user)
        if teams.exists():
            active_team = teams[0]
    return {'active_team': active_team}
