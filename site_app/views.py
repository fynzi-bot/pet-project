from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
def main_page(request):
    return render(request, "main_page.html")

def shop_page(request):
    context = {
        "goods_list": Goods.objects.all()
    }
    return render(request, "shop.html", context)


def shop_single_page(request, id):
    context = {}
    good = Goods.objects.filter(id=id)
    if len(good) > 0:
        context = {"good": good[0]}
    return render(request, "shop-single.html", context)


def news_page(request):
    context = {}
    context["news"] = News.objects.filter(category="N")
    context["updates"] = News.objects.filter(category="U")
    return render(request, "news.html", context)


def news_single_page(request, id=0):
    context = {}
    news_list = News.objects.filter(id=id)
    if len(news_list) > 0:
        context["news"] = news_list[0]
    else:
        context["news"] = {}

    return render(request, "news-single.html", context)

def Login(request):
    if request.method == "POST":
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("http://127.0.0.1:8000/shop")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "login.html")
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, "register.html")
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("http://127.0.0.1:8000/shop")
    return render(request, "register.html")

def logout_page(request):
    logout(request)

def add_to_cart(request, id):
    cart = request.session.get('cart', {})
    id = str(id)
    if id in cart:
        cart[id] += 1
    else:
        cart[id] = 1
    request.session['cart'] = cart
    return redirect('/shop')

def cart_page(request):
    cart = request.session.get('cart', {})
    ids = cart.keys()
    products = Goods.objects.filter(id__in=ids)
    for product in products:
        product.count = cart[str(product.id)]
    return render(request, "cart.html", {"products": products})

def aboutUs(request):
    return render(request, "aboutus.html")

def contactUs(request):
    return render(request, "contactus.html")

def locations(request):
    return render(request, "locations.html")

def faq(request):
    return render(request, "faq.html")

def remove_from_cart(request, id):
    cart = request.session.get('cart', {})
    id = str(id)
    if id in cart:
        del cart[id]
    request.session['cart'] = cart
    return redirect('/cart')