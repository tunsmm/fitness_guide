from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView, DeleteView, ListView

from .models import Client, Product
from .forms import ClientForm, ProductForm

from .services.menu_maker import Menumaker


# Main section

@login_required
def index(request):
    return render(request, "index.html")


# Client section

class ClientDetailView(DetailView):
    model = Client
    template_name = "client/details_view.html"
    context_object_name = 'client'


class ClientUpdateView(UpdateView):
    model = Client
    template_name = "client/new_client.html"
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
def client_main(request):
    latest_clients = Client.objects.order_by('-phone_number')[:10]
    return render(request, "client/main.html", {"clients": latest_clients})


@login_required
def add_new_client(request):
    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client-main')
        else:
            error = 'Форма была неверной'

    form_class = ClientForm
    data = {
        'form': form_class,
        'error': error
    }
    return render(request, "client/new_client.html", data)


@login_required
def generate_menu(request, pk):
    client = Client.objects.get(id=pk)

    mm = Menumaker()

    human = {
            "type": client.type_diet,
            "eats_per_day": client.eats_per_day,
            "no_eats_days": client.no_eats_days_per_week,
            "restricted_products": [],
            "loved_products": [],
            "age": 20,
            "weight": client.weight,
            "height": client.height,
            "sex": client.sex,
            "sports": client.sport_on_week,
            }
    generating_menu = mm.make_menu(human)

    return render(request, "menu/generate_menu.html", {"menu": generating_menu, "client": client})


# Product section

def product_main(request):
    latest_products = Product.objects.order_by()[:10]
    return render(request, "product/main.html", {"products": latest_products})


@login_required
def add_new_product(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-main')
        else:
            error = 'Форма была неверной'

    form_class = ProductForm
    data = {
        'form': form_class,
        'error': error
    }
    return render(request, "product/new_product.html", data)


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "product/new_product.html"
    form_class = ProductForm


class ProductDeleteView(DeleteView):
    model = Product
    success_url = "/product"
    template_name = "product/delete.html"
