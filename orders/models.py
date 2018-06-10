from django.db import models
from products.models import Product
from django.db.models.signals import post_save

class Status(models.Model):
   name = models.CharField(max_length=24, blank=True, null=True, default=None)
   is_active = models.BooleanField(default=True)
   created = models.DateTimeField(auto_now_add=True, auto_now=False)
   updated = models.DateTimeField(auto_now_add=False, auto_now=True)

   def __str__(self):
      return 'State: %s' % self.name

   class Meta:
      verbose_name = 'State of Order'
      verbose_name_plural = 'State of Orders'

class Order(models.Model):
   total_price = models.DecimalField(max_digits=100000000, decimal_places=2, default=0)  # total proice for all order in producs
   custemer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
   customer_email = models.EmailField(blank=True, null=True, default=None)
   customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
   customer_adress = models.CharField(max_length=128, blank=True, null=True, default=None)
   comments = models.TextField(blank=True, null=True, default=None)
   status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
   created = models.DateTimeField(auto_now_add=True, auto_now=False)
   updated = models.DateTimeField(auto_now_add=False, auto_now=True)


   def __str__(self):
      return 'Order: %s %s' % (self.id, self.status.name)

   class Meta:
      verbose_name = 'Order'
      verbose_name_plural = 'Orders'

   # this is not needed if small_image is created at set_image
   def save(self, *args, **kwargs):
      super(Order, self).save(*args, **kwargs)

class ProductOrder(models.Model):
   order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, blank=True, null=True, default=None)
   product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, blank=True, null=True, default=None)
   number = models.IntegerField(default=1)
   price_per_item = models.DecimalField(max_digits=1000, decimal_places=2, default=0)
   total_price = models.DecimalField(max_digits=1000, decimal_places=2, default=0) # price*number
   is_active = models.BooleanField(default=True)
   created = models.DateTimeField(auto_now_add=True, auto_now=False)
   updated = models.DateTimeField(auto_now_add=False, auto_now=True)

   def __str__(self):
      return 'Product of Order: %s' % self.product.name

   class Meta:
      verbose_name = 'Product in order'
      verbose_name_plural = 'Products in order'

   # this is not needed if small_image is created at set_image
   def save(self, *args, **kwargs):
      price_per_item = self.product.price
      self.price_per_item = price_per_item
      self.total_price = self.number * price_per_item

      super(ProductOrder, self).save(*args, **kwargs)

def product_in_order_post_save(sender, instance, created, **kwargs):
   order = instance.order
   all_products_in_order = ProductOrder.objects.filter(order=order, is_active=True)

   order_total_price = 0
   for item in all_products_in_order:
      order_total_price += item.total_price

   instance.order.total_price = order_total_price
   instance.order.save(force_update=True)

post_save.connect(product_in_order_post_save, sender=ProductOrder)

class ProductInBusket(models.Model):
   session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
   order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, blank=True, null=True, default=None)
   product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, blank=True, null=True, default=None)
   number = models.IntegerField(default=1)
   price_per_item = models.DecimalField(max_digits=1000, decimal_places=2, default=0)
   total_price = models.DecimalField(max_digits=1000, decimal_places=2, default=0) # price*number
   is_active = models.BooleanField(default=True)
   created = models.DateTimeField(auto_now_add=True, auto_now=False)
   updated = models.DateTimeField(auto_now_add=False, auto_now=True)

   def __str__(self):
      return 'Product in Busket: %s' % self.product.name

   class Meta:
      verbose_name = 'Product in Busket'
      verbose_name_plural = 'Products in Busket'

   # this is not needed if small_image is created at set_image
   def save(self, *args, **kwargs):
      price_per_item = self.product.price
      self.price_per_item = price_per_item
      self.total_price = int(self.number) * price_per_item

      super(ProductInBusket, self).save(*args, **kwargs)