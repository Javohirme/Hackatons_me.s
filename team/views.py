from django.shortcuts import render
from .models import TeamMember, Destination


def team_page(request):
    team_members = TeamMember.objects.all()
    return render(request, "team.html", {"team_members": team_members})


def support_page(request):
    return render(request, "support.html")


def privacy_policy(request):
    return render(request, "privacy_policy.html")


def destinations_list(request):
    destinations = Destination.objects.all()
    return render(request, "destinations.html", {"destinations": destinations})
