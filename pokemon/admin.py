from django.contrib import admin
from .models import Pokemon

# Register your models here.
@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "hp", "active",)
    list_display_links = ("id", "name",)
    list_filter = ("active",)

    fieldsets = (
        (
            None,  {
                'fields': ["name", "type", "hp", "active",]
            }
        ),
        (
            'Localizations', {
            'fields': ['name_fr','name_ar','name_jp',],
        }),
       
    )

