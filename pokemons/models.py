from django.db import models
import uuid

EVOLUTIONS = [
  ('e0', 'Evolution 0'),
  ('e1', 'Evolution 1'),
  ('e2', 'Evolution 2'),
  ('e3', 'Evolution 3'),
  ('e4', 'Evolution 4'),
  ('e5', 'Evolution 5'),
  ('e6', 'Evolution 6'),
]


POWER_TYPES = [
  ('fi', 'Fire'),
  ('wa', 'Water'),
  ('ai', 'Air'),
  ('ea', 'Earth'),
  ('el', 'Electric'),
  ('ps', 'Psychic'),
  ('da', 'Dark'),
  ('li', 'Light')
]


class Person(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  date_of_birth = models.DateTimeField('born at')
  where_born = models.CharField('what location concieved at', max_length=80)
  is_dead = models.BooleanField(default=False)

  def __str__(self):
    return f'{self.last_name}, {self.first_name}'


class Pokemon(models.Model):
  name = models.CharField(max_length=50)
  created_at = models.DateTimeField('created at')
  last_changed_at = models.DateTimeField('last changed at')
  creator = models.ForeignKey(Person, on_delete=models.SET_NULL, blank=True, null=True)

  power_type = models.CharField(
    max_length=2,
    choices=POWER_TYPES
  )
  
  def __str__(self):
    return self.name


class PokemonInstance(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4())
  pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
  current_owner = models.ForeignKey(Person, on_delete=models.SET_NULL, blank=True, null=True)
  owner_history = models.ManyToManyField(Person, related_name='current_owner')
  nickname = models.CharField('custom name given by owner', max_length=80, blank=True, null=True, default=None)

  evolution = models.CharField(
    max_length=2,
    choices=EVOLUTIONS,
    default='e0'
  )

  def __str__(self):
    if self.nickname and self.current_owner:
      return f'{self.current_owner.first_name}\'s {self.nickname}'
    elif self.current_owner:
      return f'{self.current_owner.name}\'s {self.pokemon.name}'
    else:
      return f'{self.pokemon.name}'