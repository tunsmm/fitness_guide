from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView

from .forms import ClientForm, DayForm, DaysOfMenuForm, DishForm, DishesOfMealForm, IngredientForm, LovedProductForm
from .forms import MealForm, MealsOfDayForm, MenuForm, ProductForm, RestrictedProductForm, TemplateForm
from .models import Client, Day, DaysOfMenu, Dish, DishesOfMeal, Ingredient, LovedProduct
from .models import Meal, MealsOfDay, Menu, Product, RestrictedProduct, Template
from .services.menu_maker import Menumaker


# Main section

@login_required
def index(request):
    return render(request, "index.html")


# Client section

@login_required
def client_main(request):
    latest_clients = Client.objects.order_by('-phone_number')[:8]
    return render(request, "client/main.html", {"clients": latest_clients})


@login_required
def client_detail(request, pk):
    client = Client.objects.get(pk=pk)
    loved_products = LovedProduct.objects.filter(client=pk)
    restricted_products = RestrictedProduct.objects.filter(client=pk)
    data = {"client": client, "loved_products": loved_products, "restricted_products": restricted_products}
    return render(request, "client/detail.html", data)


class ClientUpdateView(UpdateView):
    model = Client
    template_name = "client/new.html"
    form_class = ClientForm


class ClientDeleteView(DeleteView):
    model = Client
    success_url = "/"
    template_name = "client/delete.html"


@login_required
def client_new(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client-main')
    form_class = ClientForm
    data = {
        'form': form_class,
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


@login_required
def loved_product_new(request, pk):
    error = ''
    if request.method == 'POST':
        form = LovedProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client-detail', pk=form.cleaned_data['client'].id, permanent=True)
        else:
            error = form.non_field_errors
    form_class = LovedProductForm({'client': pk})
    data = {
        'form': form_class,
        'error': error
    }
    return render(request, "client/loved_product.html", data)


@login_required
def loved_product_delete(request, pk):
    query = LovedProduct.objects.get(pk=pk)
    client_id = query.client.id
    query.delete()
    return HttpResponseRedirect(reverse_lazy('client-detail', kwargs={'pk': client_id}))


@login_required
def restricted_product_new(request, pk):
    error = ''
    if request.method == 'POST':
        form = RestrictedProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client-detail', pk=form.cleaned_data['client'].id, permanent=True)
        else:
            error = form.non_field_errors
    form_class = RestrictedProductForm({'client': pk})
    data = {
        'form': form_class,
        'error': error
    }
    return render(request, "client/loved_product.html", data)


@login_required
def restricted_product_delete(request, pk):
    query = RestrictedProduct.objects.get(pk=pk)
    client_id = query.client.id
    query.delete()
    return HttpResponseRedirect(reverse_lazy('client-detail', kwargs={'pk': client_id}))


# Product section

@login_required
def product_main(request):
    latest_products = Product.objects.order_by("name").all()
    paginator = Paginator(latest_products, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        "product/main.html",
        {"page": page, "paginator": paginator}
    )


@login_required
def product_new(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-main')
    form_class = ProductForm
    data = {
        'form': form_class,
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
    latest_dish = Dish.objects.order_by()[:10]
    return render(request, "dish/main.html", {"dishes": latest_dish})


@login_required
def dish_new(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dish-main')
    form_class = DishForm
    data = {
        'form': form_class,
    }
    return render(request, "dish/new.html", data)


@login_required
def dish_detail(request, pk):
    dish = Dish.objects.get(pk=pk)
    ingredients = Ingredient.objects.filter(dish=pk)
    data = {"dish": dish, "ingredients": ingredients}
    return render(request, "dish/detail.html", data)


class DishDeleteView(DeleteView):
    model = Dish
    success_url = "/dish"
    template_name = "dish/delete.html"


class DishUpdateView(UpdateView):
    model = Dish
    template_name = "dish/new.html"
    form_class = DishForm


# Ingredient section

@login_required
def ingredient_new(request, pk):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dish-detail', pk=form.cleaned_data['dish'].id, permanent=True)
    form_class = IngredientForm({'dish': pk})
    data = {
        'form': form_class,
        
    }
    return render(request, "dish/ingredient.html", data)


@login_required
def ingredient_delete(request, pk):
    query = Ingredient.objects.get(pk=pk)
    dish_id = query.dish.id
    query.delete()
    return HttpResponseRedirect(reverse_lazy('dish-detail', kwargs={'pk': dish_id}))


class IngredientUpdateView(UpdateView):
    model = Ingredient
    template_name = "dish/ingredient.html"
    form_class = IngredientForm


# Meal section

@login_required
def meal_main(request):
    latest_meal = Meal.objects.order_by()[:10]
    return render(request, "meal/main.html", {"meals": latest_meal})


@login_required
def meal_new(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meal-main')
    form_class = MealForm
    data = {
        'form': form_class,
        
    }
    return render(request, "meal/new.html", data)


@login_required
def meal_detail(request, pk):
    meal = Meal.objects.get(pk=pk)
    dishes_of_meal = DishesOfMeal.objects.filter(meal=pk)
    data = {"meal": meal, "dishes_of_meal": dishes_of_meal, }
    return render(request, "meal/detail.html", data)


class MealDeleteView(DeleteView):
    model = Meal
    success_url = "/meal"
    template_name = "meal/delete.html"


class MealUpdateView(UpdateView):
    model = Meal
    template_name = "meal/new.html"
    form_class = MealForm


# DishesOfMeal section

@login_required
def dishes_of_meal_new(request, pk):
    if request.method == 'POST':
        form = DishesOfMealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meal-detail', pk=form.cleaned_data['meal'].id, permanent=True)
    form_class = DishesOfMealForm({'meal': pk})
    data = {
        'form': form_class,
        
    }
    return render(request, "meal/dish.html", data)


@login_required
def dishes_of_meal_delete(request, pk):
    query = DishesOfMeal.objects.get(pk=pk)
    meal_id = query.meal.id
    query.delete()
    return HttpResponseRedirect(reverse_lazy('meal-detail', kwargs={'pk': meal_id}))


class DishesOfMealUpdateView(UpdateView):
    model = DishesOfMeal
    template_name = "meal/dish.html"
    form_class = DishesOfMealForm


# Day section

@login_required
def day_main(request):
    latest_day = Day.objects.order_by()[:10]
    return render(request, "day/main.html", {"days": latest_day})


@login_required
def day_new(request):
    if request.method == 'POST':
        form = DayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('day-main')
    form_class = DayForm
    data = {
        'form': form_class,
        
    }
    return render(request, "day/new.html", data)


@login_required
def day_detail(request, pk):
    day = Day.objects.get(pk=pk)
    meals_of_day = MealsOfDay.objects.filter(day=pk)
    data = { "day": day, "meals_of_day": meals_of_day, }
    return render(request, "day/detail.html", data)


class DayDeleteView(DeleteView):
    model = Day
    success_url = "/day"
    template_name = "day/delete.html"


class DayUpdateView(UpdateView):
    model = Day
    template_name = "day/new.html"
    form_class = DayForm


# MealsOfDay section

@login_required
def meals_of_day_new(request, pk):
    if request.method == 'POST':
        form = MealsOfDayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('day-detail', pk=form.cleaned_data['day'].id, permanent=True)            
    form_class = MealsOfDayForm({'day': pk})
    data = {
        'form': form_class,
        
    }
    return render(request, "day/meal.html", data)


@login_required
def meals_of_day_delete(request, pk):
    query = MealsOfDay.objects.get(pk=pk)
    day_id = query.day.id
    query.delete()
    return HttpResponseRedirect(reverse_lazy('day-detail', kwargs={'pk': day_id}))


class MealsOfDayUpdateView(UpdateView):
    model = MealsOfDay
    template_name = "day/meal.html"
    form_class = MealsOfDayForm


# Menu section

@login_required
def menu_main(request):
    latest_menu = Menu.objects.order_by()[:10]
    return render(request, "menu/main.html", {"menus": latest_menu})


@login_required
def menu_new(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu-main')
    form_class = MenuForm
    data = {
        'form': form_class,
        
    }
    return render(request, "menu/new.html", data)


@login_required
def menu_detail(request, pk):
    menu = Menu.objects.get(pk=pk)
    days_of_menu = DaysOfMenu.objects.filter(menu=pk)
    data = { "menu": menu, "days_of_menu": days_of_menu, }
    return render(request, "menu/detail.html", data)


class MenuDeleteView(DeleteView):
    model = Menu
    success_url = "/menu"
    template_name = "menu/delete.html"


class MenuUpdateView(UpdateView):
    model = Menu
    template_name = "menu/new.html"
    form_class = MenuForm


# DaysOfMenu section

@login_required
def days_of_menu_new(request, pk):
    if request.method == 'POST':
        form = DaysOfMenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu-detail', pk=form.cleaned_data['menu'].id, permanent=True)
    form_class = DaysOfMenuForm({'menu': pk})
    data = {
        'form': form_class,
        
    }
    return render(request, "menu/day.html", data)


@login_required
def days_of_menu_delete(request, pk):
    query = DaysOfMenu.objects.get(pk=pk)
    menu_id = query.menu.id
    query.delete()
    return HttpResponseRedirect(reverse_lazy('menu-detail', kwargs={'pk': menu_id}))


class DaysOfMenuUpdateView(UpdateView):
    model = DaysOfMenu
    template_name = "menu/day.html"
    form_class = DaysOfMenuForm


# Template section

@login_required
def template_main(request):
    latest_template = Template.objects.order_by()[:10]
    return render(request, "template/main.html", {"templates": latest_template})


@login_required
def template_new(request):
    if request.method == 'POST':
        form = TemplateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('template-main')
    form_class = TemplateForm
    data = {
        'form': form_class,
        
    }
    return render(request, "template/new.html", data)


@login_required
def template_detail(request, pk):
    template = Template.objects.get(pk=pk)
    data = { "template": template, }
    return render(request, "template/detail.html", data)


class TemplateDeleteView(DeleteView):
    model = Template
    success_url = "/template"
    template_name = "template/delete.html"


class TemplateUpdateView(UpdateView):
    model = Template
    template_name = "template/new.html"
    form_class = TemplateForm
