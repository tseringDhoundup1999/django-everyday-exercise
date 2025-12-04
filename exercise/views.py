from django.shortcuts import render,redirect,get_object_or_404 
from django.http import HttpResponse
from exercise.models import Category,Product,Student,Course
from exercise.forms import CategoryForm,ProductForm
from django.db.models import ProtectedError 
from django.contrib import messages 

# ------- List categories and product -------------
def home(request):
    

    context = {

    }
    return render(request,"exercise/exercise.html",context)




# --- Add Category ------------
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Category added successfully !")
            return redirect("exercise_home")
    else:
        form = CategoryForm()
    
    context = {
        "form":form 
    }
    return render(request,"exercise/add_category.html",context)




# ------- delete category ----------------

def delete_category(request,pk):
    category = get_object_or_404(Category,id=pk)
    try:
        category.delete()
        messages.success(request,"Category deleted successfully!")
    except Exception as e:
        messages.error(request,F"Error deleting category: {e}")
    return redirect("exercise_home")




# --- Add Product 
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Product added successfully")
            return redirect("exercise_home")

    else:
        form = ProductForm()
    context = {
        "form":form 
    }
    return render(request,"exercise/add_product_form.html",context)