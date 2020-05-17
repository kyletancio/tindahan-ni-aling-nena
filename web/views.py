from django.shortcuts import render, redirect
from .models import Products
from .forms import ProductForm, EditForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

# Create your views here.
def home(request):
    return render(request, 'home.html', {'curr':'home'})

def products(request):
    if request.method == "POST":
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = Products.objects.all()
            return render(request, 'products.html', {'curr':'products','all_items': all_items })
    else:
        all_items = Products.objects.all()
        return render(request, 'products.html', {'curr':'products','all_items': all_items })
        
def about(request):
    return render(request, 'about.html', {'curr':'about'})

def delete(request, product_id):
    product = Products.objects.get(pk=product_id)
    product.delete()
    return redirect('products')

def edit(request, product_id):
    if request.method == 'POST':
        product_item = Products.objects.get(pk=product_id)
        form = EditForm(request.POST or None)
        if form.is_valid():
            # GET UPDATED VALUES
            updated_name = form.cleaned_data.get("name")
            updated_details = form.cleaned_data.get("details")
            updated_qty = form.cleaned_data.get("qty")
            updated_price = form.cleaned_data.get("price")

            # UPDATE OLD VALUES TO NEW
            product_item.name = updated_name
            product_item.details = updated_details
            product_item.qty = updated_qty
            product_item.price = updated_price

            product_item.save()
            return redirect('products')
    else:
        product_item=Products.objects.get(pk=product_id)
        context = {"product_id": product_id, "product_item": product_item}
        return render (request, 'edit.html', context)

def view(request, product_id):
    product = Products.objects.get(pk=product_id)
    context = {
        'name':product.name,
        'details':product.details,
        'qty':product.qty,
        'price':product.price,
        'add_date':product.add_date,
    }
    return render(request, 'view.html', context)

def login(request):
    return render(request, 'login.html', {'form':form, 'userCreated':False})
    

def signup(request):
    return render(request, 'signup.html', {'form': form})
      
