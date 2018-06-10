"""
WSGI config for DWB project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

#import os

from django.shortcuts import render
from products.models import *

def product(request, product_id):
    product = Product.objects.get(id=product_id)

    return render(request, 'products/product.html', locals())