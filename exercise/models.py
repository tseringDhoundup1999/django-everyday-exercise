from django.db import models 

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.PROTECT,null=True,blank=True,related_name="products")

    def __str__(self):
        return self.name 

class Student(models.Model):
    name = models.CharField(max_length=200)
    courses = models.ManyToManyField('Course',related_name="students")

class Course(models.Model):
    title = models.CharField(max_length=200)
