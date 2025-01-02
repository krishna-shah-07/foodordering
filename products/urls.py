from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("<uuid:pk>/", views.product_detail, name="product_detail"),
    path("add/", views.product_add, name="product_add"),
    path("<uuid:pk>/edit/", views.product_edit, name="product_edit"),
    path("<uuid:pk>/delete/", views.product_delete, name="product_delete"),
    path("<uuid:pk>/order/", views.place_order, name="place_order"),
]