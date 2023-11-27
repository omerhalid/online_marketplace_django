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
    
class Note(models.Model):
    subject = models.ForeignKey(Category, related_name='notes', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='item_images')  # File field for uploading PDFs
    is_free = models.BooleanField(default=True)  # Indicates if the note is free or for sale
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)  # Price for the note
    created_by = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title