from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name','details','qty','price','add_date']

class EditForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name','details','qty','price']
