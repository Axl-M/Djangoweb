from django import forms

class OrderForm(forms.Form):
    # name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'css_input'}))
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))