from django.shortcuts import render, redirect,get_object_or_404
from site_app.models import News, Goods, Profile, Reviews, Forum
from rest_framework.permissions import IsAuthenticated
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
        username = request.POST.get("username")
        password = request.POST.get("password")
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
        Profile.objects.create(user=user)
        login(request, user)
        return redirect("http://127.0.0.1:8000/shop")
    return render(request, "register.html")

def logout_page(request):
    logout(request)
    return redirect ("login")

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
def Profile (request, username):
    user = get_object_or_404(User, username=username)
    return render (request, 'profile.html', {'profile_user' : user})
def editProfile(request):
    if request.method == "POST":
        user = request.user
        profile, created = Profile.objects.get_or_create(user=user)
        description = request.POST.get("description")
        username = request.POST.get("username")
        if username:
            user.username = username
        if 'img' in request.FILES:
            profile.img = request.FILES['img']
        if description:
            profile.description = description
        user.save()
        profile.save()
        return redirect ('profile', username=request.user.username)
    return render(request, "EditProfile.html")

def reviews_page(request):
    return render (request,'rewiews_page.html')

def reviews_view(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return render (request, "login.html", {'err': 'login required'})
        title = request.POST.get("title")
        description = request.POST.get("description")
        stars = request.POST.get("stars")
        if not title:
            return render (request, "Reviews.html", {'err': 'title required'})
        stars = int(stars)
        if not 1<=stars<=5:
            return render (request, "Reviews.html", {'err': 'ur rating <1 or >5'})
        review , created = Reviews.objects.get_or_create(user=request.user)
        review.title = title
        review.description = description
        review.stars = stars
        review.save()
        return redirect ('/reviews')
    return render(request, "Reviews.html")
def forum(request):
    return render(request, "forum.html")
def create_forum(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return render (request, "login.html", {'err': 'login required'})
        title = request.POST.get("title")
        description = request.POST.get("description")
        img = request.FILES.get('img')
        if not title:
            return render (request, "forum.html", {'err': 'title required'})
        if not description:
            return render (request, "forum.html", {'err': 'description required'})
        forum = Forum.objects.create(
            user=request.user,
            title=title,
            description=description,
            img=img
        )
        return redirect('/forum')
    return render(request, "forum.html")

