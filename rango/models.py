from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.sites.models import Site

#class RangoUser(AbstractUser):
#
#    def __unicode__(self):
#        return self.username

class Category(models.Model):

    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, blank=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name    

    def save(self, *args, **kwargs):
        self.slug = self.name.replace(' ','-').lower()
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"

class Page(models.Model):

    title = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    slug = models.SlugField(max_length=100, blank=True)
    body = models.TextField()
    pub_date = models.DateField()
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category)

    def save(self, *args, **kwargs):
        site = Site.objects.get_current()
        self.slug = self.title.replace(' ','-').lower()
        self.url = site.domain+self.slug+'/'
        super(Page, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title