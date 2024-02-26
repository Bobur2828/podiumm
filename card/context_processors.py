from . card import Card
from my_app.models import Product
def card(request):
    return {'card': Card(request)}

def card_summary(request):
    card = Card(request)
    card_prod = card.get_products()
    card_count = card.get_count()
    umumiy_narx = {}  

    for key, value in card_count.items():
        prod = Product.objects.get(id=key)
        if prod.sale == True:
            value = int(value)  
            umumiy_narx[key] = prod.sale_price * value
        else:
            value = int(value)
            umumiy_narx[key] = prod.price * value

    data = {
        'card_prod': card_prod,
        'card_count': card_count,
        'umumiy_narx': umumiy_narx
    }
    return (data)

def umumiy_summary(request):
    card = Card(request)
    card_prod = card.get_products()
    aksiya_hisob = 0
    bezaksiya_hisob = 0
    for prod in card_prod:
        if prod.sale:
            aksiya_hisob += prod.sale_price
        else:
            bezaksiya_hisob += prod.price
    result = aksiya_hisob + bezaksiya_hisob
    return {'result': result}

# def total(request):



#     total = card.get_total()

    
#     return {'total': total}
