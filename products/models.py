from django.db import models

class Product(models.Model):
   name  = models.CharField(max_length=64, blank=True, null=True, default=None)
   price = models.DecimalField(max_digits=1000, decimal_places=2, default=0)
   short_description = models.TextField(blank=True, null=True, default=None)
   description = models.TextField(blank=True, null=True, default=None)
   is_active = models.BooleanField(default=True)
   created = models.DateTimeField(auto_now_add=True, auto_now=False)
   updated = models.DateTimeField(auto_now_add=False, auto_now=True)

   def __str__(self):
      return '%s,  %s' % (self.price, self.name)

   class Meta:
      verbose_name = 'Product'
      verbose_name_plural = 'Product'

class ProductImage(models.Model):
   product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, blank=True, null=True, default=None)
   image = models.ImageField(upload_to='products_images/')
   is_main = models.BooleanField(default=False)
   is_active = models.BooleanField(default=True)
   created = models.DateTimeField(auto_now_add=True, auto_now=False)
   updated = models.DateTimeField(auto_now_add=False, auto_now=True)

   def __str__(self):
      return 'Product itself: %s' % self.id

   class Meta:
      verbose_name = 'Photo'
      verbose_name_plural = 'Photos'