from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import Page, Category

def index(request):
    latest_pages = Page.objects.order_by('-pub_date')[:5]
    categories = Category.objects.all()
    return render(request, 'rango/page_list.html', {'latest_pages':latest_pages, 'categories':categories})

def detail(request, page_id):

    page = get_object_or_404(Page, pk=page_id)
    page.views += 1
    page.category.views += 1
    page.save()
    return render(request, 'rango/page_detail.html', {'page':page})

def about(request):
    return render(request, 'rango/about.html')

def category(request, cat_slug):

    cat = Category.objects.get(slug=cat_slug)
    cat.views += 1 
    cat.save()
    return render(request, 'rango/category_detail.html',{'cat':cat})

def like(request, category_id):
    cat = get_object_or_404(Category, pk=category_id)
    cat.likes += 1
    cat.save()
    return HttpResponseRedirect(reverse('rango:category', args=(cat.slug,)))