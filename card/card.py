from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from my_app.models import Product
from django import template


class Card:
    def __init__(self, request):
        self.session = request.session
        self.card = self.session.get('card', {})

    def add(self, product, product_count):
        product_id = str(product.id)
        product_count = int(product_count)
       

        if product_id in self.card:
            messages.success(self("Maxsulot allaqachon savatchada mavjud"))

        else:
            self.card[product_id] = product_count

        self.session['card'] = self.card
        self.session.modified = True

    def __len__(self):
        return len(self.card)

    def get_products(self):
        product_ids = self.card.keys()
       
        products= Product.objects.filter(id__in=product_ids)
        return products

    def get_count(self):
         return ( self.card )
    
    def update(self, product_id, product_count):
        product_id = str(product_id)
        product_count = int(product_count)
        
        self.card[product_id] = product_count
        self.session.modified = True
        return self.card

    def delete(self, product_id):
        product_id = str(product_id)
        if product_id in self.card:
            del self.card[product_id]
            
            self.session.modified = True
            return self.card
    
    def get_total(self):
        product_ids = self.card.keys()
        products= Product.objects.filter(id__in=product_ids)
        total=0
        for key,value in self.card.items():
            key=int(key)
            for product in products:
                if product.id == key:
                    if product.sale == True:
                        total += product.sale_price * int(value)
                    else:
                        total += product.price * int(value)
        return total 
    
    def get_all_info(self):
        products=self.get_products()
        quantity=self.get_count() 
        
        result = []

        for product in products:
            if str(product.id) in quantity:
                if product.sale == True:
                    data={
                        'id': product.id,
                        'name': product.name,
                        'price': product.sale_price,
                        'quantity': quantity[str(product.id)],

                    }
                    result.append(data)
                else:
                    data={
                        'id': product.id,
                        'name': product.name,
                        'price': product.price,
                        'quantity': quantity[str(product.id)],

                    }
                    result.append(data)
                    
        return result
    

    def cardclear(self):
        self.card.clear()
        self.session.modified = True
        return self.card