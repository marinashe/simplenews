from django.contrib import admin

# Register your models here.
from news import models


class NewsAdmin(admin.ModelAdmin):
    date_hierarchy = 'posted_time'
    list_filter = (
        'source',
    )
    search_fields = (
        'id',
        'title',
    )
    list_display = (
        'id',
        'title',
        'description',
        'posted_time',
        'source',
    )


admin.site.register(models.News, NewsAdmin)