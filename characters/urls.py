from django.urls import path

from characters.views import CharacterListView, get_random_character_view

urlpatterns = [
    path("characters/random/", get_random_character_view, name="character-random"),
    path("characters/", CharacterListView.as_view(), name="character-list"),
]

app_name = "characters"