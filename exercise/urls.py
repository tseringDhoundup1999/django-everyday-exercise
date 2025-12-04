from django.urls import path 
from exercise.views import home,delete_category,add_category,add_product
urlpatterns = [
    path('',home,name='exercise_home'),
    path("category/add",add_category,name="add_category"),
    path("category/delete/<int:pk>",delete_category,name="delete_category"),
    path("product/add/",add_product,name="add_product"),


]