from django.contrib import admin
from django.urls import path
from site_app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name='main_page'),
    path('shop/', views.shop_page, name='shop'),
    path('shop-single/<int:id>/', views.shop_single_page),
    path('news/', views.news_page),
    path('news/<int:id>/', views.news_single_page),
    path('login/', views.Login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_page, name='logout'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_page, name='cart'),
    path('reviews/', views.reviews_page, name='reviews'),
    path('edit-review/', views.reviews_view, name='edit_review'),
    path('forum/', views.forum, name='forum'),
    path('create-blank/', views.create_forum, name='create_blank'),
    path('profile/<str:username>/', views.Profile, name='profile'),
    path('edit-profile/', views.editProfile, name='edit_profile'),
    path('forum/<int:id>/',views.forum_task, name='single_task' ),
    path('forum/<int:id>/comment/', views.add_comment, name='add_a_comment'),
       ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
