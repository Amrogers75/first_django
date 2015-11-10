from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from main.models import State, StateCapital, City, UserProfile


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
admin.site.register(UserProfile)
