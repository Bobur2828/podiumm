from django.shortcuts import render,get_object_or_404
from .card import Card
from django.http import HttpResponse
from my_app.models import Product
from django.http import JsonResponse
from django.contrib import messages
def card_summary(request):
    card = Card(request)
    card_prod = card.get_products()
    card_count = card.get_count()
    total = card.get_total()

    

    data = {
        'card_prod': card_prod,
        'card_count': card_count,

        'total': total
    }
    return render(request, 'card/card_sum.html', context=data)

def umumiy_summary(request):
    
    return render(request, 'card/card_sum.html', )

def card_add(request):
    card=Card(request)
    if request.POST.get('action')=='post':
        product_id=(request.POST.get('product_id'))
        product_count=int(request.POST.get('product_count'))
        product=get_object_or_404(Product, id=product_id)
        print(request.POST.get('product_count'))


        if product is not card:
            print(product,product_count)
            card.add(product,product_count)
            
        card_items=card.__len__()
        return JsonResponse({"card_items": card_items})
    return render(request, 'my_app/index.html')
     



def card_delete(request):
    card=Card(request)
    if request.POST.get('action')=='post':
        product_id=(request.POST.get('product_id'))

        card.delete(product_id)
        
        return JsonResponse({"product_id": product_id})
    

def card_update(request):
    card=Card(request)
    if request.POST.get('action')=='post':
        product_id=(request.POST.get('product_id'))
        product_count=int(request.POST.get('product_count'))
        print(product_id, product_count )

        card.update(product_id,product_count)
        return JsonResponse({"product_id": product_id})
    