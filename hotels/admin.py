from django.contrib import admin

from .models import Hotel, Bedroom, TaxiRoute


class TaxiRouteInline(admin.TabularInline):
    model = TaxiRoute
    extra = 1


class BedroomInline(admin.TabularInline):
    model = Bedroom
    extra = 1


class HotelAdmin(admin.ModelAdmin):
    inlines = [BedroomInline, TaxiRouteInline]


admin.site.register(Hotel, HotelAdmin)
