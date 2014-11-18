from django.contrib import admin

from .models import Page, Category, RangoUser


class PageAdmin(admin.ModelAdmin):

    list_display = ['title', 'pub_date', 'category']
    fieldsets = [
        ('Category', {'fields': ['category']}),
        ('Page Details', {'fields': ['title', 'body']}),
        ('URL', {'fields': ['url', 'slug'], 'classes': ['collapse']}),
        ('Date Published', {'fields': ['pub_date']}),
        ('Misc', {'fields': ['views']}), ]

    search_fields = ['title', 'category']


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'views', 'likes']
    fieldsets = [
        (None, {'fields': ['name', ]}),
        ('Misc', {'fields': ['likes', 'views']}),
        ('slug', {'fields': ['slug', ], 'classes': ['collapse', ]}), ]

admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(RangoUser)
