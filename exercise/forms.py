from django import forms 
from exercise.models import Product,Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']