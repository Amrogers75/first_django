from django.contrib import admin

# Register your models here.
from main.models import State, StateCapital, City


class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbrev')


class CapitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'pop')

admin.site.register(State, StateAdmin)
admin.site.register(StateCapital, CapitalAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ('city', 'state', 'zip_code')
    search_fields = ['city']

admin.site.register(City)

