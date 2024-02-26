

from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog-left-sidebar/', views.blog_left_sidebar, name='blog_left_sidebar'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('compare/', views.compare, name='compare'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('my-account/', views.my_account, name='my_account'),
    path('shop-left-sidebar/', views.shop_left_sidebar, name='shop_left_sidebar'),
    path('showcategory/<slug:slug>/', views.show_category, name='showcategory'),
    path('showbrands/<slug:slug>/', views.show_brands, name='showbrands'),
    path('showcolors/<slug:slug>/', views.show_colors, name='showcolors'),
    path('single-product-sale/', views.single_product_sale, name='single_product_sale'),
    path('single-product/<slug:slug>/', views.single_product, name='single_product'),
    path('showsize/<slug:slug>/', views.show_size, name='showsize'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('error/', views.error, name='error'),
    



]
