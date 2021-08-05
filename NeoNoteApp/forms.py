from django import forms
from django.forms import ModelForm
from .models import Places, Group

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
         model = User
         fields = ['username', 'email', 'first_name', 'last_name', 'password']

class GroupForm(forms.ModelForm):
    class Meta:
         model = Group
         fields = ['group_name']

class PlacesForm(forms.ModelForm):
    note = forms.CharField(label='Note ', widget=forms.Textarea(attrs={'rows': '3','cols': '30',}),)
    img = forms.ImageField(label='Image ')
    class Meta:
         model = Places
         fields = ['place_name', 'address', 'rate', 'img', 'note']
