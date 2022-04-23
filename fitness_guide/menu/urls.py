from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("client", views.client_main, name="client-main"),
    path("client/new", views.add_new_client, name="client-new"),
    path("client/<int:pk>", views.ClientDetailView.as_view(), name="client-detail"),
    path("client/<int:pk>/update", views.ClientUpdateView.as_view(), name="client-update"),
    path("client/<int:pk>/delete", views.ClientDeleteView.as_view(), name="client-delete"),
    path("client/<int:pk>/generate_menu", views.generate_menu, name="menu-generate"),

    path("product", views.product_main, name="product-main"),
    path("product/new", views.add_new_product, name="product-new"),
    path("product/<int:pk>/update", views.ProductUpdateView.as_view(), name="product-update"),
    path("product/<int:pk>/delete", views.ProductDeleteView.as_view(), name="product-delete"),

    path("dish", views.dish_main, name="dish-main"),
    path("dish/new", views.add_new_dish, name="dish-new"),
    path("dish/<int:pk>", views.dish_detail, name="dish-detail"),
    path("dish/<int:pk>/update", views.DishUpdateView.as_view(), name="dish-update"),
    path("dish/<int:pk>/delete", views.DishDeleteView.as_view(), name="dish-delete"),
    path("dish/<int:pk>/ingredient", views.add_new_ingredient, name="ingredient-new"),
    path("dish/<int:pk>/ingredient/update", views.IngredientUpdateView.as_view(), name="ingredient-update"),
    path("dish/<int:pk>/ingredient/delete", views.delete_ingredient, name="ingredient-delete"),
]
