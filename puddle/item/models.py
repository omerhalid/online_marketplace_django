from django.contrib.auth.models import User 
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name',) # This is to make the categories be ordered by name
        verbose_name_plural = 'Categories' # This is to make the plural of Category be Categories instead of Categorys
        
    def __str__(self):
        return self.name # This is to make the name of the category be the name of the category instead of Category object (1)
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE) # This is to make the item be in a category
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True) # This is to make the description be optional
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True) # This is to make the image be optional
    is_sold = models.BooleanField(default=False) # This is to make the item be not sold by default
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE) # This is to make the item be created by a user
    created_at = models.DateTimeField(auto_now_add=True) # This is to make the created_at be the time the item was created
    
    def __str__(self):
        return self.name # This is to make the name of the category be the name of the category instead of Category object (1)