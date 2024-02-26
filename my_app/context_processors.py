from . models import Category,Brands,Colors,Size,Product
from card.card import Card

def categories(request):
    categories=Category.objects.all()
    return {'categories': categories}

def brands(request):
    brands=Brands.objects.all()
    return {'brands': brands}

def colors(request):
    colors=Colors.objects.all()
    return {'colors': colors}

def size(request):
    size=Size.objects.order_by(('?'))
    return {'size': size}

def products(request):
    products=Product.objects.all().select_related('category').prefetch_related('brand','size','colors')
    return {'products': products}

def yangi(request):
    yangi=Product.objects.filter(sale=False)[:4].select_related('category').prefetch_related('brand','size','colors')
    return {'yangi': yangi}

def total(request):
    card = Card(request)


    total = card.get_total()

    
    return {'total': total}
def sanoq(request):
    card = Card(request)
    
    card_count = card.get_count()
    return {'card_count':card_count}

