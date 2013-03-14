#encoding: utf-8

from django.contrib import admin

from .models import Sponsor

class SponsorAdmin(admin.ModelAdmin):

    list_display = ['name', 'type', 'created_at']
    search_fields = ['name']


admin.site.register(Sponsor, SponsorAdmin)