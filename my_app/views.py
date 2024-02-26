from django.shortcuts import render,get_object_or_404
from random import sample
from django.http import HttpResponse
from django.contrib import messages
from .models import Slider,Aksiya,Product,Brands,Category,Colors,Size
from card.card import Card


def index(request):
    slider=Slider.objects.all()
    aksiya=Aksiya.objects.order_by('data_created')[:3]
    product=Product.objects.order_by(('?')).select_related('category').prefetch_related('brand','size','colors')
    sale_products = Product.objects.filter(sale=True).exclude(sale_date__isnull=True).select_related('category').prefetch_related('brand','size','colors')
    products =  product.order_by('-data_created').select_related('category').prefetch_related('brand','size','colors')
    brand= Brands.objects.all()
    sale_products = Product.objects.filter(sale=True).exclude(sale_date__isnull=True).select_related('category').prefetch_related('brand','size','colors')
    
    for prod in sale_products:
        prod.foiz = round(((prod.price - prod.sale_price) / prod.price) * 100, 0)

    
        
    data={
        "slider":slider,
        "aksiya":aksiya,
        "product":product,
        "products":products,
        "brand":brand,
        "sale_products":sale_products,
        
    }
    return render(request, 'my_app/index.html',context=data)

def about(request):
    slider=Slider.objects.all()
    data={
        "slider":slider
    }
    return render(request, 'my_app/about.html', context=data)

def blog_left_sidebar(request):
    return render(request, 'my_app/blog-left-sidebar.html')

def cart(request):
    return render(request, 'my_app/cart.html')

def checkout(request):
    return render(request, 'my_app/checkout.html')

def compare(request):
    return render(request, 'my_app/compare.html')

def contact(request):
    data={
        'page': 'Aloqa',
        'title': 'Biz bilan aloqa'
    }
    return render(request, 'my_app/contact.html', context=data)

def faq(request):
    return render(request, 'my_app/faq.html')

def my_account(request):
    return render(request, 'my_app/my-account.html')

def shop_left_sidebar(request):
    return render(request, 'my_app/shop-left-sidebar.html')

def show_category(request, slug):
    cat = get_object_or_404(Category, cat_slug=slug)
    products=Product.objects.filter(category=cat).select_related('category').prefetch_related('brand','size','colors')
    data = {
        'page':cat.cat_name, 
        'title': f'{cat.cat_name} turkumiga oid mahsulotlar',
        "cat": cat,
        "products":products, 
    }
    return render(request, 'my_app/shop-left-sidebar.html', context=data)


def show_brands(request, slug):
    brand = get_object_or_404(Brands, slug=slug)
    products=Product.objects.filter(brand=brand).select_related('category').prefetch_related('brand','size','colors')
    data = {
        'page':brand.name,  
        'title': f'{brand.name} turkumiga oid mahsulotlar',
        "brand": brand,
        "products":products,
    }
    return render(request, 'my_app/shop-left-sidebar.html', context=data)

def show_colors(request, slug):
    color = get_object_or_404(Colors, slug=slug)
    products=Product.objects.filter(colors=color).select_related('category').prefetch_related('brand','size','colors')
    data = {
        'title': f'{color.name} rangiga oid mahsulotlar',
        'page':color.name,
        "color": color,
        "products":products,
    }
    return render(request, 'my_app/shop-left-sidebar.html', context=data)

def show_size(request, slug):
    size = get_object_or_404(Size, slug=slug)
    products=Product.objects.filter(size=size).select_related('category').prefetch_related('brand','size','colors')
    data = {
        'page':{size.name}, 
        'title': f'{size.name,} turkumiga oid mahsulotlar',
        "products":products,  
    }
    return render(request, 'my_app/shop-left-sidebar.html', context=data)

def single_product_sale(request):
    return render(request, 'my_app/single-product-sale.html')

def single_product(request, slug):
    product=get_object_or_404(Product, slug=slug)
    products =  Product.objects.order_by('?').select_related('category').prefetch_related('brand','size','colors')
    data={
        'title': f'{product.name} Eng sara narxlarda sotib oling',
        'page':product.name,
        "product":product,
        "products":products,
    }
    return render(request, 'my_app/single-product.html', context=data)

def wishlist(request):
    return render(request, 'my_app/wishlist.html')

def error(request):
    return render(request, 'my_app/404-error.html')


