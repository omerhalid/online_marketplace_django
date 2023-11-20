from django.shortcuts import get_object_or_404, render

from .models import Item


def detail(request, pk): # pk is the primary key of the item
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item/detail.html', {'item': item})