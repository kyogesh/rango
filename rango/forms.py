from django import forms
from .models import Page, Category, RangoUser
from django.contrib.auth.models import User

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ('title', 'body', 'category')

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name',)

class RangoUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class RangoUserProfileForm(forms.ModelForm):

    class Meta:
        model = RangoUser
        fields = ('website', 'profile_pic')