from django.contrib import admin
from .models import sovrinlar, liga, davlat, kamanda, oyincilar, pazitsiya,bozor

@admin.register(sovrinlar)
class SovrinlarAdmin(admin.ModelAdmin):
    list_display = ('name', 'qita')
    search_fields = ('name',)

@admin.register(liga)
class LigaAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(davlat)
class DavlatAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(kamanda)
class KamandaAdmin(admin.ModelAdmin):
    list_display = ('name', 'liga', 'sovrinlar', 'murabbiy')
    list_filter = ('liga',)
    search_fields = ('name', 'murabbiy')

@admin.register(oyincilar)
class OyincilarAdmin(admin.ModelAdmin):
    list_display = ('name', 'nomer', 'kamanda', 'davlat', 'gollar', 'asiste')
    list_filter = ('kamanda', 'davlat')
    search_fields = ('name',)
    # Gollar soni bo'yicha saralash imkoniyati
    ordering = ('-gollar',)

@admin.register(pazitsiya)
class PazitsiyaAdmin(admin.ModelAdmin):
    list_display = ('name', 'oyincilar')
    list_filter = ('name',)


@admin.register(bozor)
class BozorAdmin(admin.ModelAdmin):
    list_display = ('name','narxi')
