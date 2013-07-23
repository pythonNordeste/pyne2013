#coding: utf-8

from django.contrib import admin
from .models import Speaker, Reference, Slot


class ReferenceAdmin(admin.StackedInline):
    model = Reference
    extra = 1


class TalkAdmin(admin.ModelAdmin):
    inlines = (ReferenceAdmin, )


admin.site.register(Speaker)
admin.site.register(Slot, TalkAdmin)
