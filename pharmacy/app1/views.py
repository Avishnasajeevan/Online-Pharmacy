from email import message
from http.client import HTTPResponse
from logging import WARNING
from multiprocessing import context

from unicodedata import category
from urllib.request import Request
from django.shortcuts import render,redirect
from .form import CustomUserForm
from .models import Brands, Category, Product,Cart
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import JsonResponse
import json

 
# Create your views here.
def home(request):
     
    dict_brd={
        'brd':Brands.objects.all(),
        'category':Category.objects.all()
    }
    return render(request, "home.html", dict_brd)

def homeView(request, name):
    if request.user.is_authenticated:
        if(Category.objects.filter(name=name)):
            products=Product.objects.filter(category__name=name)
            return render(request, "products/index.html",{"products":products,"category_name":name})
        else:
            return redirect('home')
    else:
        return redirect('home')


def productinfo(request, cname, pname):
    if request.user.is_authenticated:
        if(Category.objects.filter(name=cname)):
            if(Product.objects.filter(pname=pname)):
                products=Product.objects.filter(pname=pname).first()
                return render(request, 'products/productinfo.html',{"products":products, "category_name":cname})
            else:
                messages= WARNING (request,"No such product found")
                return redirect('home.html')
        else:
            messages= WARNING (request,"No such category found")
            return redirect('home.html')
    else:
        return redirect('home')

# def cart(request):
#      return render(request, "cart.html")


def about(request):
    return render(request, "about.html")
   

def faq(request):
    return render(request, "faq.html")

def reg(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form=CustomUserForm()
        if request.method=='POST':
            form=CustomUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Successfully Registered Please Login..!")
                return redirect('login')
        return render(request, "reg.html", {'form':form})
    
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logout successfully")
    return redirect('login')
  

def auth_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                return redirect("/")
            else:
                messages.error(request, "Invalid Username or Password")
                return redirect("/login")
        
        return render(request, "login.html")



def add_to_cart(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_qty=data['product_qty']
            product_id=data['pid']
            # print(request.user.id)
            
            product_status=Product.objects.get(id=product_id) 
            if product_status:
                if Cart.objects.filter(user=request.user,product_id=product_id):
                    return JsonResponse({'status': " already In cart"}, status=200)
                else:
                    if product_status.quantity>= product_qty:
                        Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                        return JsonResponse({'status': "Product added to cart success"}, status=200)
                    else:
                        return JsonResponse({'status': "no stock"}, status=200)
        else:
            return JsonResponse({'status': "please login"}, status=200)
    else:
        return JsonResponse({'status': "invalid Access"}, status=200)

    
def cart_page(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        return render(request, "cart.html",{"cart":cart})

       
    else:
        return redirect('/')
    
def remove_cart(request, cid):
    cartitem=Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect('/cart')

def profile(request):
    return render(request, "home.html")



# json code for addtocart
   