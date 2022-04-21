from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy


from .models import Client, Dish, Ingredient, Ingredient, MeasureScale, Product
from .forms import ClientForm, DishForm, IngredientForm, ProductForm

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
    template_name = "client/new.html"
    form_class = ClientForm


class ClientDeleteView(DeleteView):
    model = Client
    success_url = "/"
    template_name = "client/delete.html"


@login_required
def client_main(request):
    latest_clients = Client.objects.order_by('-phone_number')[:6]
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
    return render(request, "client/new.html", data)


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

@login_required
def product_main(request):
    latest_products = Product.objects.order_by()[:6]
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
    return render(request, "product/new.html", data)


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "product/new.html"
    form_class = ProductForm


class ProductDeleteView(DeleteView):
    model = Product
    success_url = "/product"
    template_name = "product/delete.html"


# Dish section

@login_required
def dish_main(request):
    latest_dish = Dish.objects.order_by()[:6]
    return render(request, "dish/main.html", {"dishes": latest_dish})


@login_required
def add_new_dish(request):
    error = ''
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dish-main')
        else:
            error = 'Форма была неверной'

    form_class = DishForm
    data = {
        'form': form_class,
        'error': error
    }
    return render(request, "dish/new.html", data)


@login_required
def dish_detail(request, pk):
    dish = Dish.objects.get(pk=pk)
    ingredients = Ingredient.objects.filter(dish=pk)

    data = {"dish": dish, "ingredients": ingredients}

    return render(request, "dish/details_view.html", data)


# Ingredient section

@login_required
def add_new_ingredient(request, pk):
    error = ''
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dish-detail', pk=form.cleaned_data['dish'].id, permanent=True)
        else:
            error = 'Форма была неверной'

    form_class = IngredientForm({'dish': pk})
    data = {
        'form': form_class,
        'error': error
    }
    return render(request, "dish/ingredient.html", data)


def delete_ingredient(request, pk):
    query = Ingredient.objects.get(pk=pk)
    dish_id = query.dish.id
    query.delete()
    return HttpResponseRedirect(reverse_lazy('dish-detail', kwargs={'pk': dish_id}))


class IngredientUpdateView(UpdateView):
    model = Ingredient
    template_name = "dish/ingredient.html"
    form_class = IngredientForm
