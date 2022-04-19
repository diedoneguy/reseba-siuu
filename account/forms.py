from django import forms

class AccountForm(forms.Form):
    user_name = forms.CharField(required=True)
    password = forms.EmailField(required=True)
    email = forms.EmailField(required=True)