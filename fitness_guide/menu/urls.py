from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("client", views.client_main, name="client-main"),
    path("client/new", views.client_new, name="client-new"),
    path("client/<int:pk>", views.client_detail, name="client-detail"),
    path("client/<int:pk>/update", views.ClientUpdateView.as_view(), name="client-update"),
    path("client/<int:pk>/delete", views.ClientDeleteView.as_view(), name="client-delete"),
    path("client/<int:pk>/generate_menu", views.generate_menu, name="menu-generate"),
    path("client/<int:pk>/loved_product/new", views.loved_product_new, name="loved-product-new"),
    path("client/<int:pk>/loved_product/delete", views.loved_product_delete, name="loved-product-delete"),

    path("product", views.product_main, name="product-main"),
    path("product/new", views.product_new, name="product-new"),
    path("product/<int:pk>/update", views.ProductUpdateView.as_view(), name="product-update"),
    path("product/<int:pk>/delete", views.ProductDeleteView.as_view(), name="product-delete"),

    path("dish", views.dish_main, name="dish-main"),
    path("dish/new", views.dish_new, name="dish-new"),
    path("dish/<int:pk>", views.dish_detail, name="dish-detail"),
    path("dish/<int:pk>/update", views.DishUpdateView.as_view(), name="dish-update"),
    path("dish/<int:pk>/delete", views.DishDeleteView.as_view(), name="dish-delete"),
    path("dish/<int:pk>/ingredient", views.ingredient_new, name="ingredient-new"),
    path("dish/<int:pk>/ingredient/update", views.IngredientUpdateView.as_view(), name="ingredient-update"),
    path("dish/<int:pk>/ingredient/delete", views.ingredient_delete, name="ingredient-delete"),

    path("meal", views.meal_main, name="meal-main"),
    path("meal/new", views.meal_new, name="meal-new"),
    path("meal/<int:pk>", views.meal_detail, name="meal-detail"),
    path("meal/<int:pk>/update", views.MealUpdateView.as_view(), name="meal-update"),
    path("meal/<int:pk>/delete", views.MealDeleteView.as_view(), name="meal-delete"),
    path("meal/<int:pk>/dish", views.dishes_of_meal_new, name="dishes-of-meal-new"),
    path("meal/<int:pk>/dish/update", views.DishesOfMealUpdateView.as_view(), name="dishes-of-meal-update"),
    path("meal/<int:pk>/dish/delete", views.dishes_of_meal_delete, name="dishes-of-meal-delete"),

    path("day", views.day_main, name="day-main"),
    path("day/new", views.day_new, name="day-new"),
    path("day/<int:pk>", views.day_detail, name="day-detail"),
    path("day/<int:pk>/update", views.DayUpdateView.as_view(), name="day-update"),
    path("day/<int:pk>/delete", views.DayDeleteView.as_view(), name="day-delete"),
    path("day/<int:pk>/meal", views.meals_of_day_new, name="meals-of-day-new"),
    path("day/<int:pk>/meal/update", views.MealsOfDayUpdateView.as_view(), name="meals-of-day-update"),
    path("day/<int:pk>/meal/delete", views.meals_of_day_delete, name="meals-of-day-delete"),

    path("menu", views.menu_main, name="menu-main"),
    path("menu/new", views.menu_new, name="menu-new"),
    path("menu/<int:pk>", views.menu_detail, name="menu-detail"),
    path("menu/<int:pk>/update", views.MenuUpdateView.as_view(), name="menu-update"),
    path("menu/<int:pk>/delete", views.MenuDeleteView.as_view(), name="menu-delete"),
    path("menu/<int:pk>/day", views.days_of_menu_new, name="days-of-menu-new"),
    path("menu/<int:pk>/day/update", views.DaysOfMenuUpdateView.as_view(), name="days-of-menu-update"),
    path("menu/<int:pk>/day/delete", views.days_of_menu_delete, name="days-of-menu-delete"),

    path("template", views.template_main, name="template-main"),
    path("template/new", views.template_new, name="template-new"),
    path("template/<int:pk>", views.template_detail, name="template-detail"),
    path("template/<int:pk>/update", views.TemplateUpdateView.as_view(), name="template-update"),
    path("template/<int:pk>/delete", views.TemplateDeleteView.as_view(), name="template-delete"),
]
