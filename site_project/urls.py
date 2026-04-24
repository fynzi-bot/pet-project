from django.contrib import admin
from django.urls import path
from site_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page),
    path('shop/', views.shop_page),
    path('shop-single/<int:id>', views.shop_single_page),
    path('news/', views.news_page),
    path('news/<int:id>', views.news_single_page),
    path('login/', views.Login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_page, name='logout'),
    path ('add-to-cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_page, name='cart'),
]
