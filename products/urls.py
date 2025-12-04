from django.urls import path 
from products.views import product_list,product_create,category_list,category_create,category_delete


urlpatterns = [
    # category 
    path("categories",category_list,name='categories-list'),
    path("categories/add",category_create,name='categories-create'),
    path("categories/<int:id>/delete",category_delete,name='category-delete'),

    # product specific 
    path("products/",product_list,name='product-list'),
    path("products/add/",product_create,name='product-create'),

]
