from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "slug", "price", "description", "quantity"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter product name"}),
            "slug": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter product slug"}),
            "price": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter product price"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter product description"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter product quantity"}),
        }
        help_texts = {
            "name": "The name of the product.",
            "slug": "A unique identifier for the product, used in URLs.",
            "price": "The price of the product in USD.",
            "description": "A detailed description of the product.",
            "quantity": "The available quantity of the product.",
        }

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price

    def clean_quantity(self):
        quantity = self.cleaned_data.get("quantity")
        if quantity < 0:
            raise forms.ValidationError("Quantity cannot be negative.")
        return quantity