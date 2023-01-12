from django.urls import path

from . import views

app_name = 'pokemons'
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:pokemon_id>/', views.detail, name='detail')
]