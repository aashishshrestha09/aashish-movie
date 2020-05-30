from django import forms
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import POST


class POSTFORM(ModelForm):

    name = forms.CharField(label='Name',
                           widget=forms.TextInput(attrs={'placeholder': 'Enter name', 'class': 'your_css_code'}))

    picture = forms.URLField(label='URL', required=False,
                             widget=forms.TextInput(attrs={'placeholder': "Picture's Url", 'class': 'your_css_code'}))

    class Meta:
        model = POST
        fields = "__all__"
        exclude = ['user']


class CreateUserModel(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
