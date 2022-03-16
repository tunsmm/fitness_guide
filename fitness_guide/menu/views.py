from django.shortcuts import render

from django.http import HttpResponse

from .models import Client

# Create your views here.

"""
def index(request):
    # minus - sorts from largest to smallest
    latest = Client.objects.order_by('-phone_number')[:10]
    output = []
    for item in latest:
        output.append(item.full_name)
    return HttpResponse('\n'.join(output))
"""  

def index(request):
    latest = Client.objects.order_by('-phone_number')[:10]
    return render(request, "index.html", {"clients":latest})