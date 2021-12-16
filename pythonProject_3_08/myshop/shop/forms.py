from django import forms

from shop.models import TestUser


class TestUserForm(forms.Form):
    login = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'class': 'block'}))
    password = forms.CharField(max_length=100, widget = forms.PasswordInput())


class TestUserModelForm(forms.ModelForm):
    class Meta:
        model = TestUser
        fields = ['login','password']