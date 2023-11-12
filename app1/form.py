from django.forms import ModelForm
from .models import *



class buyproductform(ModelForm):
    class Meta:
        model=Buyproduct
        fields='__all__'