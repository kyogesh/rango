import requests

from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

from .models import Page, Category
from .forms import PageForm, CategoryForm, RangoUserForm, RangoUserProfileForm


def list_categories():
    return Category.objects.all()


def index(request):
    r = requests.get('http://httpbin.org/status/418')
    latest_pages = Page.objects.order_by('-pub_date')[:5]
    categories = list_categories()
    return render(request, 'rango/page_list.html',
                  {'latest_pages': latest_pages,
                   'categories': categories,
                   'teapot': r.text, })


def detail(request, page_id):

    page = get_object_or_404(Page, pk=page_id)
    page.views += 1
    page.category.views += 1
    page.save()
    categories = list_categories()
    return render(request, 'rango/page_detail.html',
                  {'page': page, 'categories': categories})


def about(request):
    return render(request, 'rango/about.html')


def category(request, cat_slug):

    cat = Category.objects.get(slug=cat_slug)
    cat.views += 1
    cat.save()
    categories = list_categories()

    return render(request, 'rango/category_detail.html',
                  {'cat': cat, 'categories': categories})


def list_pages(request):
    pages = Page.objects.all()
    categories = list_categories()
    return render(request, 'rango/pages.html',
                  {'pages': pages, 'categories': categories})


def like(request, category_id):
    cat = get_object_or_404(Category, pk=category_id)
    cat.likes += 1
    cat.save()
    return HttpResponseRedirect(reverse('rango:category', args=(cat.slug, )))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = RangoUserForm(data=request.POST)
        profile_form = RangoUserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = RangoUserForm()
        profile_form = RangoUserProfileForm()

    return render(request, 'rango/register.html',
                  {'user_form': user_form, 'profile_form': profile_form,
                   'registered': registered})


def signin(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value),
        # no user with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect(reverse('rango:index'))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        categories = list_categories()
        return render_to_response('rango/login.html',
                                  {'categories': categories},
                                  RequestContext(request))


@login_required
def restricted(request):
    return HttpResponse("You're seeing this page because you're logged in.")


@login_required
def signout(request):

    logout(request)

    return HttpResponseRedirect(reverse('rango:index'))


@login_required
def add_page(request):

    if request.method == 'POST':
        new_form = PageForm(data=request.POST)
        if new_form.is_valid:
            new_page = new_form.save(commit=False)
            new_page.pub_date = datetime.now().date()
            new_page.save()
            return HttpResponseRedirect(reverse('rango:detail',
                                                args=(new_page.id, )))
        else:
            new_form.errors
    else:
        new_form = PageForm()

    categories = list_categories()
    return render(request, 'rango/add_page.html',
                  {'new_form': new_form, 'categories': categories})


def add_category(request):

    if request.method == 'POST':
        new_form = CategoryForm(data=request.POST)
        if new_form.is_valid():
            new_category = new_form.save()
            return HttpResponseRedirect(reverse('rango:category',
                                                args=(new_category.slug, )))
        else:
            new_form.errors
    else:
        new_form = CategoryForm()

    categories = list_categories()
    return render(request, 'rango/add_category.html',
                  {'new_form': new_form, 'categories': categories})


def jq(request):
    return render(request, 'rango/test_doc.html', {})
