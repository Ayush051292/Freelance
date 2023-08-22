from django import forms 
from django.forms import ModelForm
from .models import *


alltype= [
    ('---Select Please---', '---Select Please---'),
    ('All', 'All'),
    ('Customer', 'Customer'),
    ('Management', 'Management'),
    ('Facw', 'Facw'),
    ]

class TermconditionForm(ModelForm):
    class Meta:
        model = Termcondition
        fields = "__all__"
        labels = {'subject': 'Subject'}
        widgets = {'subject': forms.TextInput(attrs={'class': 'form-control'}), 'content': forms.Select({'required':'required'})}
        exclude = {'created_at', 'updated_at', 'created_by', 'subject', 'type', 'status'}