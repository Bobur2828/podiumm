from django.shortcuts import render,get_object_or_404,redirect,reverse,redirect
from .card import Card
from django.http import HttpResponseRedirect
from my_app.models import Product,Order,OrderItem,Profile
from django.http import JsonResponse
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import uuid
from decimal import Decimal
from .telegram import main
import asyncio

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
    

def order_details(request):
    card = Card(request)
    all_info = card.get_all_info()
    
    if all_info:
        name = []
        name1 = {}
        user = request.user
        print(request.user)
        if request.user.is_anonymous:
            return HttpResponseRedirect(reverse('userauth:login'))
        
        order = Order()
        order.user_id = user
        profile = Profile.objects.filter(user=user).first()
        order.order_id = ''.join(c for c in str(uuid.uuid4().int)[:5] if c.isdigit())
        order.total_price = card.get_total()
        order.save()

        data = {}
        for info in all_info:
            order_item = OrderItem(
                order=order,
                product=int(info['id']),
                name=info['name'],
                price=info['price'],
                quantity=int(info['quantity'])
            )
            order_item.save()

        for info in all_info:
            name1 = {
                'NOMi': info['name'],
                'NARXI': int(info['price']),
                'SANOGI': int(info['quantity'])
            }
            name.append(name1)

        message = f'Buyurtma raqami: {order.order_id}\n'
        for item in name:
            message += f"Nomi: {item['NOMi']},\n Narxi: {item['NARXI']} so'm,\n Sanogi: {item['SANOGI']} dona\n"

        asyncio.run(main(f"""{message}\n 
                            Umumiy hisob {order.total_price} so'm 
                            Buyurtmachi: {user.username}
                            Tel: {profile.phone_number}
                            E-mail: {user.email}
                            Shaxar: {profile.city}
                            Manzil: {profile.adress}
                            Pochta indeks: {profile.zipcode}
                            """))
                            
        messages.success(request, "Buyurtmangiz qabul qilindi iltimos javob habarini kuting")
        card.cardclear()
        return redirect('index')
    else:
        messages.error(request, "Savatchangizda mahsulot topilmadi")
        return redirect('index')


@login_required
def order_info(request):
    orders = Order.objects.filter(user_id=request.user)
    result = []
    
    if orders:  # Agar orders bo'sh bo'lmasa
        for order in orders:
            order_items = OrderItem.objects.filter(order=order)
            data = {'order': order.order_id, 'items': order_items}
            result.append(data)
        data = {'orders': result, 'obj': orders}
        return render(request, 'card/order.html', context=data)
    else:  # Agar orders bo'sh bo'lsa
        return render(request, 'card/order.html')


def check(request, order_id):
    orders = Order.objects.filter(order_id=order_id)
    result = []
    
    if orders:  # Agar orders bo'sh bo'lmasa
        for order in orders:
            order_items = OrderItem.objects.filter(order=order)
            
            data = {'order': order.order_id, 'items': order_items, 'order_date': order.order_date}
            result.append(data)
        data = {'orders': result, 'obj': orders}
 
    return render(request, 'card/check.html',context=data)