from django.db import models

from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=210,unique=True)
    slug = models.SlugField(max_length=250,unique=True,blank=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)
    def __str__(self):
        return self.name 

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=150,)
    slug = models.SlugField(max_length=200,unique=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField(blank=True)
    stock_quantity  = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="products/images",blank=True,null=True)

    is_featured= models.BooleanField(default=False)

    # Timestamps 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name 
