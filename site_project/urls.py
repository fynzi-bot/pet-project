from django.contrib import admin
from django.urls import path
from site_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', views.news_page),
    path('login/', views.Login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_page, name='logout'),
    path('cart/', views.cart_page, name='cart'),
]
