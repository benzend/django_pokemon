from django.contrib import admin

from .models import Pokemon, PokemonInstance, Person


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
  list_display = ('name', 'creator', 'created_at')
  pass


@admin.register(PokemonInstance)
class PokemonInstanceAdmin(admin.ModelAdmin):
  list_display = ('pokemon', 'nickname', 'current_owner')
  pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
  list_display = ('first_name', 'last_name', 'date_of_birth')
  pass