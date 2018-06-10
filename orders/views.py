# """
# WSGI config for DWB project.
#
# It exposes the WSGI callable as a module-level variable named ``application``.
#
# For more information on this file, see
# https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
# """
#
# #import os
#
# from django.shortcuts import render
# from .forms import SubscruberForm
#
# def landing(request):
#
#     dateopening = '28.05.2018'
#
#     request_result_warn_typ = ''
#     request_result_text = ''
#
#     form = SubscruberForm(request.POST or None)
#
#     if request.method == "POST":
#         #
#         #print(form.cleaned_data)
#         #data = form.cleaned_data
#         #print(form.cleaned_data["email"])
#         #print(data["name"])
#         if form.is_valid():
#             save_form = form.save()
#             request_result_warn_typ = 'alert-success'
#             request_result_text = 'Your request was successfully sent!'
#         else:
#             request_result_warn_typ = 'alert-danger'
#             request_result_text = 'Sorry, impossible to sent request. Correct, and try again? '
#
#     return render(request, 'landing/landing.html', locals())
#

from django.http import JsonResponse
from .models import ProductInBusket

def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    product_id = data.get("product_id")
    numb = data.get("numb")
    is_delete = data.get("is_delete")
    print(is_delete)

    if is_delete == 'true':
        ProductInBusket.objects.filter(id=product_id).update(is_active=False)
    else:
        new_product, created = ProductInBusket.objects.get_or_create(session_key=session_key, product_id=product_id, is_active=True, defaults={"number": numb})
        print(new_product)
        if not created:
            print("not created")
            new_product.number += int(numb)
            new_product.save(force_update=True)

    # common code for two cases
    products_in_basket = ProductInBusket.objects.filter(session_key=session_key, is_active=True)
    products_total_numb = products_in_basket.count()
    return_dict["products_total_numb"] = products_total_numb

    return_dict["products"] = list()

    for item in products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["numb"] = item.number
        return_dict["products"].append(product_dict)

    return JsonResponse(return_dict)

