from django import forms
from django.contrib.auth.models import User

from .models import Page, Category, RangoUser


class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ('title', 'body', 'category')


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name', )


class RangoUserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class RangoUserProfileForm(forms.ModelForm):

    class Meta:
        model = RangoUser
        fields = ('website', 'profile_pic')
