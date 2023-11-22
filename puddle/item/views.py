from django.contrib.auth.decorators import login_required
from django.db.models import Q # This is a class that allows you to make complex queries.
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EditItemForm, NewItemForm
from .models import Item, Category 

def items(request):
    query = request.GET.get('query', '') # get the query from the url
    category_id = request.GET.get('category', 0) # get the category from the url
    categories = Category.objects.all() # get all categories
    items = Item.objects.filter(is_sold=False).order_by('-created_at') # get all items that are not sold and order them by the created_at field.
    
    if category_id:
        items = items.filter(category_id=category_id) # filter the items by the category_id.
    
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query)) # filter the items by the query. The __icontains is a field lookup that is case-insensitive.
        
    return render(request, 'item/items.html', {'items': items, 'query': query, 'categories': categories, 'category_id': int(category_id)})


def detail(request, pk): # pk is the primary key of the item
    item = get_object_or_404(Item, pk=pk)
    releted_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk).order_by('-created_at')[0:4] # This is a list of items that are in the same category as the item being viewed. It excludes the item being viewed and orders the list by the created_at field. It then slices the list to only show the first 4 items.
    #TO DO: there is a type in related_items
    return render(request, 'item/detail.html', {'item': item, 'releted_items': releted_items})

@login_required # This is a decorator that requires the user to be logged in to access the view.
def new(request):
    
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            
            return redirect('item:detail', pk=item.id)
    
    else:
        form = NewItemForm()
    
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New Item',
    })

@login_required # This is a decorator that requires the user to be logged in to access the view.
def edit(request, pk):
    
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        
        if form.is_valid():
            form.save() # created_by is not included because it is already set to the user.
            
            return redirect('item:detail', pk=item.id)
    
    else:
        form = EditItemForm(instance=item)
    
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New Item',
    })
    
@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user) # get item or 404
    item.delete()
    
    return redirect('dashboard:index')