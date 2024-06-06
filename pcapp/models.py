from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=50,unique=True)
    des=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='category',blank=True)
    
    class Meta:
        ordering=('name', )
        verbose_name='category'
        verbose_name_plural='categories'
        
        def __str__(self):
            return '{}'.format (self.name)

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=50,unique=True)
    des=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='product',blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    stock=models.IntegerField(null=True)
    available=models.BooleanField(default=True,null=True)
    created=models.DateTimeField(auto_now_add=True,null=True)
    updated=models.DateTimeField(auto_now=True,null=True)
      
    class Meta:
        ordering=('name', )
        verbose_name='product'
        verbose_name_plural='products'       
         
        def __str__(self):
            return '{}'.format (self.name)
    
    
    