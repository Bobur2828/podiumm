from django.urls import path
from .import views

app_name='card'

urlpatterns = [
    path('',views.card_summary,name='card_summary'),
    path('card_add/',views.card_add,name='card_add'),
    path('card_delete/',views.card_delete,name='card_delete'),
    path('card_update/',views.card_update,name='card_update'),
    path('order/',views.order_details,name='order'),
    path('orders/',views.order_info,name='orders'),
    path('check/<order_id>/',views.check, name='check'),


    




]