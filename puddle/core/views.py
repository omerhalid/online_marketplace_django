from django.shortcuts import redirect, render
from django.contrib.auth import logout
from item.models import Item, Category

from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False).order_by('-created_at')[0:6]
    categories = Category.objects.all()
    
    return render(request, 'core/index.html', {
        'categories': categories, 
        'items': items
        })

def contact(request):
    return render(request, 'core/contact.html')


def singup(request):
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    
    else:
        form = SignupForm()
    
    return render(request, 'core/signup.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('core:index')