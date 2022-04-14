from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("client", views.client_main, name="client-main"),
    path("client/new", views.add_new_client, name="add-new-client"),
    path("client/<int:pk>", views.ClientDetailView.as_view(), name="client-detail"),
    path("client/<int:pk>/update", views.ClientUpdateView.as_view(), name="client-update"),
    path("client/<int:pk>/delete", views.ClientDeleteView.as_view(), name="client-delete"),
    path("client/<int:pk>/generate_menu", views.generate_menu, name="menu-generate"),

    path("product", views.product_main, name="product-main"),
    path("product/new", views.add_new_product, name="add-new-product"),
    path("product/<int:pk>/update", views.ProductUpdateView.as_view(), name="product-update"),
    path("product/<int:pk>/delete", views.ProductDeleteView.as_view(), name="product-delete"),

    path("dish", views.dish_main, name="dish-main"),
    path("dish/new", views.add_new_dish, name="add-new-dish"),
    path("dish/<int:pk>", views.dish_detail, name="dish-detail"),
]
