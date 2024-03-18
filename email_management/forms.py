from django import forms
from django.conf import settings



class SMSSendForm(forms.Form):
    recipients = forms.CharField(label="Recipients")
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Type your message here...', 'rows': 10, 'cols': 150}))