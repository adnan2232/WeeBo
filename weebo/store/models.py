from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BLANK_CHOICE_DASH

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete =models.CASCADE, null=True,blank=True)
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200, null=True,blank=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField()
    description = models.CharField(max_length=500,blank=True,default="")
    CATEGORY = (('shirt','SHIRT'), ('t-shirt','T-SHIRT'),('trouser','TROUSER'))
    categories = models.CharField(max_length=7,choices=CATEGORY,default='shirt')
    image = models.ImageField(null=True,blank = True)
    stock = models.IntegerField(default = 0)
    

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    def __str__(self) :
        return self.name
    class Meta:
        ordering = ['-stock']

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitem = self.orderitem_set.all()
        total =  sum([item.get_total for item in orderitem])
        return total
    @property
    def get_cart_items(self):
        orderitem = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitem])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null =True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True)
    quantity = models.IntegerField(default = 0, null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add = True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    def __str__(self):
        return self.product.name
    

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null= True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

class Ordered(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null= True)
    address = models.ForeignKey(ShippingAddress,on_delete=models.SET_NULL, blank=True, null= True)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
        ordering = ['-datetime']