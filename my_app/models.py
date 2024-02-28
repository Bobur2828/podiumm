from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save


DAVLAT = [
    ("UZ", "O'zbekiston"),
    ("KG", "Qirg'iziston"),
    ("KZ", "Qozog'iston"),
    ("TJ", "Tojikiston"),
    ("TM", "Turkmaniston"),
    ("AF", "Afg'oniston")
]
SHAXAR = [
    ("TAS", "Toshkent shahri"),
    ("AND", "Andijon viloyati"),
    ("NAM", "Namangan viloyati"),
    ("SAM", "Samarqand viloyati"),
    ("FAR", "Farg'ona viloyati"),
    ("SUR", "Surxondaryo viloyati"),
    ("JIZ", "Jizzax viloyati"),
    ("KAS", "Qashqadaryo viloyati"),
    ("NAV", "Navoiy viloyati"),
    ("XOR", "Xorazm viloyati"),
    ("KAR", "Karakalpakistan Respublikasi"),
    ("SIR", "Sirdaryo viloyati"),
    ("BUK", "Buxoro viloyati"),
]
class Slider(models.Model):
    title = models.CharField(max_length=100, verbose_name='Birinchi qatorni kiriting')
    title1 = models.CharField(max_length=100, verbose_name='Ikkinchi qatorni kiriting')
    title2 = models.CharField(max_length=100, verbose_name='Uchinchi qatorni kiriting')
    photo = models.ImageField(upload_to="slider/photo", verbose_name='Slide uchun foto kiriting 1920x753 olchamda')
    photo1 = models.ImageField(upload_to="slider/photo", verbose_name='Kichik banner uchun foto kiriting 1170x250 olchamda')
    data_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class Aksiya(models.Model):
    title = models.CharField(max_length=100, verbose_name='Birinchi qatorni kiriting')
    title1 = models.CharField(max_length=100, verbose_name='ikkinchi qatorni kiriting')
    title2 = models.CharField(max_length=100, verbose_name='uchinchi qatorni kiriting')
    photo = models.ImageField(upload_to="aksiya/photo", verbose_name='Aksiya uchun foto kiriting 370x240 olchamda')
    data_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class Size(models.Model):
    name = models.CharField(max_length=100, verbose_name='Size nomini kiriting')
    slug = models.SlugField(max_length=10, unique=True, db_index=True)
    def __str__(self):
        return self.name
    
class Category(models.Model):
    cat_name = models.CharField(max_length=100, verbose_name='Kategoriya nomini kiriting')
    cat_slug = models.SlugField(max_length=10, unique=True, db_index=True)
    cat_photo = models.ImageField(upload_to="category/photo", blank=True, default=None,null=True,  verbose_name='Categoriya uchun foto 370x240 olchamda')
    def __str__(self):
        return self.cat_name
    
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Mahsulot nomini kiriting')
    min_content = models.TextField(max_length=300,verbose_name='Mahsulotga qisqacha tarif')
    max_content = models.TextField(max_length=1500,verbose_name='Mahsulotga batafsil tarif')
    price = models.DecimalField(max_digits=10, decimal_places=0,default='0',verbose_name='Narxni belgilang')
    size = models.ManyToManyField(Size, verbose_name="O'lchamni tanlang")
    category = models.ForeignKey(Category, verbose_name='Kategoriyani tanlang', on_delete=models.CASCADE)
    brand=models.ForeignKey("Brands", verbose_name="Brandni tanlang", on_delete=models.CASCADE)
    articul = models.BigIntegerField( blank=True, default='',null=True,)
    colors=models.ManyToManyField("Colors", verbose_name="Rangini tanlang")
    photo1 = models.ImageField(upload_to="product/photo",   verbose_name='Tovar fotosini kiriting')
    photo2 = models.ImageField(upload_to="product/photo",  blank=True, default=None,null=True, verbose_name='Tovar fotosini kiriting')
    photo3 = models.ImageField(upload_to="product/photo", blank=True, default=None,null=True,  verbose_name='Tovar fotosini kiriting')
    photo4 = models.ImageField(upload_to="product/photo", blank=True, default=None,null=True,  verbose_name='Tovar fotosini kiriting')
    photo5 = models.ImageField(upload_to="product/photo", blank=True, default=None,null=True,  verbose_name='Tovar fotosini kiriting')
    data_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=10, unique=True, db_index=True)
    sale=models.BooleanField(default=False)
    sale_date = models.DateField(blank=True, null=True, verbose_name='Skidka tugash sanasini belgilang')
    data_sale = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)  # %Y/%m/%d ko'rinishidagi tarix

    def save(self, *args, **kwargs):
        if self.sale_date:  # Agar sale_date mavjud bo'lsa
            self.data_sale = self.sale_date.strftime('%Y/%m/%d')
        super().save(*args, **kwargs)  # Obyektni saqlash

    sale_price = models.DecimalField(max_digits=10, decimal_places=0,default='0',blank=True, null=True,verbose_name='Skidka Narxni belgilang')


    def save(self, *args, **kwargs):
        if not self.articul:  # Agar articul bo'sh bo'lsa
            # Yangi articulni o'rnatish logikasi
            last_instance = Product.objects.order_by('-articul').first()
            if last_instance:
                self.articul = last_instance.articul + 1
            else:
                self.articul = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Colors(models.Model):
    name = models.CharField(max_length=100, verbose_name='Rang nomini kiriting')
    slug = models.SlugField(max_length=10, unique=True, db_index=True)
    def __str__(self):
        return self.name

class Brands(models.Model):


    name = models.CharField(max_length=100, verbose_name='Brand nomini kiriting')
    slug = models.SlugField(max_length=10, unique=True, db_index=True)
    photo1 = models.ImageField(upload_to="slider/photo", blank=True, default=None,null=True,  verbose_name='Brand logosini yuklang agar bolsa 370x240 olchamda')

    def __str__(self):
        return self.name
    
class Order(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=40, unique=True,)
    order_date=models.DateTimeField(auto_now_add=True)
    total_price=models.DecimalField(max_digits=16, decimal_places=2)
    
    def __str__(self) -> str:
        return self.order_id
    
class OrderItem(models.Model):
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.CharField(max_length=40, )
    name=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=16, decimal_places=2)
    quantity=models.PositiveIntegerField()
    

    def __str__(self) -> str:
        return f"{self.name} - { self.quantity} "
    
    @property
    def get_total_price(self):
        return self.price * self.quantity
    
    
    

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="product/photo", blank=True, default=None, null=True,
                              verbose_name='Tovar fotosini kiriting')
    date_updated = models.DateField(auto_now=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True, default='nomalum raqam')
    country = models.CharField(max_length=100, choices=DAVLAT, blank=True, null=True,default='Noaniq davlat')
    city = models.CharField(max_length=100, choices=SHAXAR, blank=True, null=True,default='Noaniq shaxar')
    adress = models.CharField(max_length=100, blank=True, null=True,default='Manzil noaniq')
    zipcode = models.CharField(max_length=100, blank=True, null=True, default='Pochta noaniq')




def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()


post_save.connect(create_profile, sender=User)

