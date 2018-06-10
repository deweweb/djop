"""
WSGI config for DWB project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

#import os

from django.shortcuts import render
from .forms import SubscruberForm
from products.models import *

def landing(request):

    dateopening = '28.05.2018'

    request_result_warn_typ = ''
    request_result_text = ''

    form = SubscruberForm(request.POST or None)

    if request.method == "POST":
        #
        #print(form.cleaned_data)
        #data = form.cleaned_data
        #print(form.cleaned_data["email"])
        #print(data["name"])
        if form.is_valid():
            save_form = form.save()
            request_result_warn_typ = 'alert-success'
            request_result_text = 'Your request was successfully sent!'
        else:
            request_result_warn_typ = 'alert-danger'
            request_result_text = 'Sorry, impossible to sent request. Correct, and try again? '

    return render(request, 'landing/landing.html', locals())

def home(request):
    product_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    product_images_phones = product_images.filter(product__category__id = 1)
    product_images_laptops = product_images.filter(product__category__id = 2)
    return render(request, 'landing/home.html', locals())
