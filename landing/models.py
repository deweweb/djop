from django.db import models

class Subscriber(models.Model):
   email = models.EmailField()
   name  = models.CharField(max_length=128)

   def __str__(self):
      return 'USER: %s E-MAIL: %s' % ( self.name, self.email)

   class Meta:
      verbose_name = 'Profile'
      verbose_name_plural = 'Profiles'