from django import forms
from .models import *

class SendMessageForm(forms.ModelForm):
    class Meta:
        model = SendMessage
        fields = '__all__'