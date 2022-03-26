from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Client


@login_required
def index(request):
    latest = Client.objects.order_by('-phone_number')[:10]
    return render(request, "index.html", {"clients": latest})


def generate_menu(request):
    return render(request, "generate_menu.html")
