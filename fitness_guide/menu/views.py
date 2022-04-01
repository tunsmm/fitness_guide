from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView, DeleteView

from .models import Client
from .forms import ClientForm


class ClientDetailView(DetailView):
    model = Client
    template_name = "client/details_view.html"
    context_object_name = 'client'


class ClientUpdateView(UpdateView):
    model = Client
    template_name = "new_client.html"
    form_class = ClientForm
    """
    fields = ("full_name", "sex", "height", "weight", 
                  "sport_on_week", "no_eats_days_per_week", 
                  "eats_per_day", "phone_number", "type_diet")
    """


class ClientDeleteView(DeleteView):
    model = Client
    success_url = "/"
    template_name = "client/delete.html"
    


@login_required
def index(request):
    latest = Client.objects.order_by('-phone_number')[:10]
    return render(request, "index.html", {"clients": latest})


@login_required
def add_new_client(request):
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
    return render(request, "client/new_client.html", data)
