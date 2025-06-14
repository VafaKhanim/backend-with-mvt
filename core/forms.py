from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 255)
    email = forms.EmailField()
    phone = forms.IntegerField()
    message = forms.CharField(widget = forms.Textarea())

class SubscribeForm(forms.Form):
    email = forms.EmailField()