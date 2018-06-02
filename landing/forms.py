from django import forms
from .models import *

class SubscruberForm(forms.ModelForm):

    class Meta:
        model  = Subscriber
        exclude = ["uuid", "is_featured", "created_by", "update_by", "created", "updated" ]

