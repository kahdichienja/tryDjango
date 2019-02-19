from django import forms

class Contanct_form(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)