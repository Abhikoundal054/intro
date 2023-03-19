from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.urls import reverse_lazy
#from django.views import generic
from django.contrib.auth import login, authenticate ,login as authlogin
from myapp.forms import LoginForm
from django.contrib.auth.decorators import login_required
from myapp import views

#from products.models import Product


# Create your views here.
def index(request):
     return  render(request,'index.html',{})

def about1(request):
     return  render(request,'about.html',{})

def index2(request):
     return  render(request,'index2.html',{})

def newarr1(request):
     return  render(request,'signup.html',{})

def login(request):
     return  render(request,'login.html',{})

#def cart(request):
     #return  render(request,'cart.html',{})

def signup1(request):
     form = UserCreationForm()
     if request.method=='POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('index')
     return render(request,'signup.html',{'form':form})

def login_page(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        if user is not None:
            # Save session as cookie to login the user
            authlogin(request, user)
            # Success, now let's login the user.
            return render(request, 'index2.html')
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'login.html')
    
    
    
    
    # message=''
     #form=UserCreationForm(request.POST or None)
     #if request.method == 'POST':
         # form=UserCreationForm(request.POST or None)
      #    if form.is_valid():
       #        user=authenticate(
        #            username=form.cleaned_data['username'],
         #           password=form.cleaned_data['password'],
          #     )
           #    if user is not None:
            #
            #       return redirect('index')
             #
             #
             #
             #
             #
             #       message=f'Hello{user.username}! You have been logged in'
              # else:
               #     message='login failed!'
     #return render(
      #    request,'login.html',context={'form': form,'message': message})



'''def add_to_cart(request,product_id):
     product = Product.objects.get(id==product_id)
     cart = Cart(user=request.user , product=product)
     cart.save()
     return redirect('cart')

def cart(request):
     cart_items = Cart.objects.filter(user=request.user)
     total = 0
     for item in cart_items:
          total +=item.product.price * item.quantity
     return render(request,'cart.html',{'cart_items':cart_items ,'total':total})

def remove_from_cart(request,cart_id):
     cart_item = Cart.objects.get(id=cart_id)
     cart_item.delete()
     return redirect('cart')'''
