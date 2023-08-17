from django.contrib import admin

from . models import User, Cafe, Review, Image


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", )
    prepopulated_fields = {"slug": ["username", ]}


class CafeAdmin(admin.ModelAdmin):
    list_display = ("name", "location")


class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "cafe", "path")


admin.site.register(User, UserAdmin)
admin.site.register(Cafe)
admin.site.register(Image)
