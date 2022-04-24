from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("client", views.client_main, name="client-main"),
    path("client/new", views.client_new, name="client-new"),
    path("client/<int:pk>", views.ClientDetailView.as_view(), name="client-detail"),
    path("client/<int:pk>/update", views.ClientUpdateView.as_view(), name="client-update"),
    path("client/<int:pk>/delete", views.ClientDeleteView.as_view(), name="client-delete"),
    path("client/<int:pk>/generate_menu", views.generate_menu, name="menu-generate"),

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
]
