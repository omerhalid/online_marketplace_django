from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .forms import NewItemForm
from .models import Item


def detail(request, pk): # pk is the primary key of the item
    item = get_object_or_404(Item, pk=pk)
    releted_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk).order_by('-created_at')[0:4] # This is a list of items that are in the same category as the item being viewed. It excludes the item being viewed and orders the list by the created_at field. It then slices the list to only show the first 4 items.
    
    return render(request, 'item/detail.html', {'item': item, 'releted_items': releted_items})

@login_required # This is a decorator that requires the user to be logged in to access the view.
def new(request):
    form = NewItemForm()
    
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New Item',
    })