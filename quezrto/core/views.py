from django.shortcuts import render, redirect
from item.models import Category,Item
from .forms import SignupForm

# Create your views here.
def index(req):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(req,'core/index.html', {
        'categories': categories,
        'items': items
    })

def contacts(req):
    return render(req,'core/contact.html')

def signup(request):
    print(request.method)
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            print('valid')
            return redirect('/login/')
        else:
            print('Not valid')
    else:
        form = SignupForm

    return render(request,'core/signup.html',{
        'form':form
    })