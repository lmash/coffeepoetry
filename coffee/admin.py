from django.contrib import admin

from . models import User, CoffeeShop, Review


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", )
    prepopulated_fields = {"slug": ["username",]}


admin.site.register(User, UserAdmin)
admin.site.register(CoffeeShop)
