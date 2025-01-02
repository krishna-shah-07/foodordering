from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from django.contrib import messages

def product_list(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", {"products": products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/product_detail.html", {"product": product})

def product_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()
    return render(request, "products/product_form.html", {"form": form})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("/products/")
    else:
        form = ProductForm(instance=product)
    return render(request, "products/product_form.html", {"form": form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect("/products/")
    return render(request, "products/product_confirm_delete.html", {"product": product})

def place_order(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        quantity = int(request.POST.get("quantity"))
        if quantity > product.quantity:
            messages.error(request, "Not enough stock available.")
        else:
            product.quantity -= quantity
            product.save()
            messages.success(request, "Order placed successfully!")
        return redirect("product_detail", pk=pk)
    return redirect("product_detail", pk=pk)