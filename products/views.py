from django.shortcuts import render,redirect,get_object_or_404
# message
from django.contrib import messages 

# models 
from products.models import Products,Category
import pprint

# Create your views here.

def product_list(request):
    products = Products.objects.all()
    context = {
        "products":products
    }
    return render(request,"products/products.html",context)


def category_list(request):
    category_list = Category.objects.all()
    context = {"categories":category_list}
    return render(request,"products/category.html",context)

    


def category_create(request):   
    if request.method =="POST":
        category_name = request.POST.get("category_name").strip()

         # Check if the input is empty
        if not category_name:
            messages.error(request,"Category name cannot be empty")
            return redirect("categories-list")
            
        # check if category already exits 
        if Category.objects.filter(name__iexact=category_name).exists():
            messages.error(request,"Category already exits")
            return redirect("categories-list")
        # Save Category 
        Category.objects.create(name=category_name)
        messages.success(request,f"Category {category_name} is created successfully")
        return redirect("categories-list")

    



def category_delete(request,id):
    # get the category or return 404 error 
    category = get_object_or_404(Category,id=id)
    category.delete()
    messages.success(request,f"Category {category.name}  deleted successfully")

    return redirect("categories-list")




def product_create(request):
    categories = Category.objects.all()
    errors ={}
    data = {}
     # default context
    context = {
        "categories": categories,
        "errors": errors,
        "data": data,
    }

    required_fields = ["product_name","product_price","product_desc","product_category"]

    if request.method == "POST":
        data["product_name"] = request.POST.get("product_name").strip()
        data["product_price"] = request.POST.get("product_price").strip()
        data["product_desc"] = request.POST.get("product_description")
        data["product_stock_quantity"] = request.POST.get("product_stock_quantity")
        data["product_available"] = request.POST.get("product_available") == "on"
        data["product_is_featured"] = request.POST.get("product_is_featured") == "on"
        data["product_category"] = request.POST.get("product_category").strip()
        data["product_image"] = request.FILES.get("product_image") 

        # check required fields contain value otherwise raise and error 
        for field in required_fields:
            if not data.get(field):
                errors[field] = f"{field.replace('_',' ').title()} is required field"

        if errors:
         return render(request,"products/add_product.html",context)
        
        category = categories.get(id=int(data["product_category"]))
        
        # save the product 
        Products.objects.create(
            name = data['product_name'],
            price = data['product_price'],
            image=data['product_image'],
            category=category,
            description=data['product_desc'],
            stock_quantity=data['product_stock_quantity'],
            available=data['product_available'],
            is_featured=data['product_is_featured'],
        )

     
        # send success message
        messages.success(request,f"Product {data['product_name']} is created successfully! ")
        return redirect("product-list")

    return render(request,"products/add_product.html",context)