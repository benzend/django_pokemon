from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Pokemon

# Create your views here.
def index(request):
  ctx = {'pokemons': get_list_or_404(Pokemon)}
  return render(request, 'pokemons/index.html', ctx)

def detail(request, pokemon_id):
  ctx = {'pokemon': get_object_or_404(Pokemon, pk=pokemon_id)}
  return render(request, 'pokemons/detail.html', ctx)