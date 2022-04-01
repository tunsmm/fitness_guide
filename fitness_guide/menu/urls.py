from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("client/new", views.add_new_client, name="add_new_client"),
    path("client/<int:pk>", views.ClientDetailView.as_view(), name="client-detail"),
    path("client/<int:pk>/update", views.ClientUpdateView.as_view(), name="client-update"),
    path("client/<int:pk>/delete", views.ClientDeleteView.as_view(), name="client-delete"),
]
