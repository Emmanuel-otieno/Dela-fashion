from django import forms

class OrderForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
    phone = models.CharField(max_length=15