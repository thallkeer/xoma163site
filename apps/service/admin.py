from django.contrib import admin

from apps.service.models import Statistic, Issue, Service, Counter, Cat, Meme, Notify, City


@admin.register(Statistic)
class VkUserAdmin(admin.ModelAdmin):
    list_display = ('command', 'count_queries',)
    ordering = ('-count_queries',)


@admin.register(Issue)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('text',)


admin.site.register(Service)


@admin.register(Counter)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'count', 'chat')


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'preview', 'author')


@admin.register(Meme)
class MemeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link', 'preview', 'author')
    search_fields = ['name', 'link']
    list_filter = ('author',)


@admin.register(Notify)
class NotifyAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'text', 'author', 'chat', 'from_chat')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'synonyms', 'timezone', 'lat', 'lon')
