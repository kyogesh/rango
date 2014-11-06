from django import forms
from .models import Page, Category

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ('title', 'body', 'category',)

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name')