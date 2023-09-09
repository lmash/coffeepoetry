from django.contrib import admin

from . models import User, Cafe, Review, Image, CoffeeDescription, Poem


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", )
    prepopulated_fields = {"slug": ["username", ]}


class CafeAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "check_for_haiku")


class CoffeeDescriptionAdmin(admin.ModelAdmin):
    list_display = ("cafe", "created_at", "description")


class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "cafe", "path")


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("cafe", "reviewer", "created_at", "score")


admin.site.register(User, UserAdmin)
admin.site.register(Cafe)
admin.site.register(CoffeeDescription, CoffeeDescriptionAdmin)
admin.site.register(Image)
admin.site.register(Poem)
admin.site.register(Review, ReviewAdmin)

