from django.shortcuts import redirect, render
from .models import *
from django.http import JsonResponse
import json
import datetime
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_items":0,"get_cart_total":0}
        cartItems = order["get_cart_items"]
    cat = request.GET.get("selection")

    query = request.GET.get('search','')
    

    if len(query) > 0:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    
    
    context = {'products':products, "cartItems": cartItems,"cat":cat}
    return render(request,'store/store.html',context)

def cart(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_items":0,"get_cart_total":0}
        cartItems = order["get_cart_items"]
    context = {"items":items, "order":order, "cartItems": cartItems}
    return render(request,'store/cart.html',context)

def checkout(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete = False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    context = {"items":items, "order":order, "cartItems": cartItems}
    return render(request,'store/checkout.html',context)


def updateItem(request):

    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    customer = request.user.customer
    product = Product.objects.get(id = productId)
    order,created = Order.objects.get_or_create(customer = customer, complete = False)

    orderItem, created = OrderItem.objects.get_or_create(order = order, product=product)

    if action == "add":
        product.stock = product.stock - 1
        orderItem.quantity  = orderItem.quantity + 1
    elif action == "remove":
        product.stock = product.stock + 1
        orderItem.quantity = orderItem.quantity - 1
    product.save()
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item added successfully',safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    customer = request.user.customer
    order,created = Order.objects.get_or_create(customer = customer, complete = False)
    total = float(data["form"]["total"])
    order.transaction_id = transaction_id

    if total == float(order.get_cart_total) :
        order.complete = True

    order.save()

    ShippingAddress.objects.create(
        customer = customer,
        order = order,
        address = data["shipping"]["address"],
        city = data["shipping"]["city"],
        state = data["shipping"]["state"],
        zipcode = data["shipping"]["zipcode"],
    )

    return JsonResponse('Payment successfully',safe=False)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('store')
    else:
        context = {}
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('store')
            else:
                messages.warning(request,"Username or Password is incorrect")
                
        return render(request,"store/login.html",context)
    

def register(request):

    if request.user.is_authenticated:
        return redirect('store')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data["username"]
                Customer.objects.create(user = User.objects.get(username=username), name = username, email = form.cleaned_data["email"])
            
                messages.success(request,"Account: "+username+" created succefully")
                return redirect('login')

        context = { 'form': form}
        return render(request,'store/register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('store')