from django.shortcuts import render

from .models import Client


def index(request):
    latest = Client.objects.order_by('-phone_number')[:10]
    return render(request, "index.html", {"clients": latest})
