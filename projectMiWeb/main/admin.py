from django.contrib import admin
from . import models


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'cat_id', 'pk')


class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'pk')


admin.site.register(models.Posts, PostAdmin)
admin.site.register(models.Category, CatAdmin)