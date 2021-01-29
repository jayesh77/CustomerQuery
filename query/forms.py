from django import forms
from django.forms import Textarea

from . import models
class queryform(forms.ModelForm):
    class Meta:
        model=models.querydata
        fields=['name','email_id','mobile_number','query']
        widgets = {'query':forms.Textarea()}
        labels={'email_id':'email','mobile_number':'mobile'}
class EditForm(forms.ModelForm):
    add_to_customer_list = forms.BooleanField()
    class Meta:
        model=models.querydata
        fields='__all__'
