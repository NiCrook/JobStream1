from django.shortcuts import render

from . import models


def agent_registration_view(request):
    return render(request, 'AgentRegistration/agent_registration.html')