from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Client
from .forms import ClientForm


@login_required
def index(request):
    latest = Client.objects.order_by('-phone_number')[:10]
    return render(request, "index.html", {"clients": latest})


def generateMenu(request):
    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Форма была неверной'
            
    
    form_class = ClientForm
    data = {
        'form': form_class,
        'error': error
    }
    return render(request, "generate_menu.html", data)
