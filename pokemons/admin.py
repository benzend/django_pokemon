from django.contrib import admin

from .models import Pokemon, PokemonInstance, Person


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
  pass


@admin.register(PokemonInstance)
class PokemonInstanceAdmin(admin.ModelAdmin):
  pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
  pass