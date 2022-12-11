import requests
import json

trainer_token = 'fe7ef58b8cef60e47ca59d0f82a009c3'

response_create = requests.post('https://pokemonbattle.me:5000/pokemons', headers = {'trainer_token' : trainer_token}, json = {
    "name": "ФАПАХ",
    "photo": "https://www.transparentpng.com/thumb/pokemon/IJXG81-pokemon-hd-image.png"
})

print(response_create.text)

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers = {'trainer_token' : trainer_token}, json = {
    "pokemon_id": 1502,
    "name": "aRolf",
    "photo": "https://www.transparentpng.com/thumb/pokemon/IJXG81-pokemon-hd-image.png"
})

print(response_put.text)

response_pokeball = requests.post('https://pokemonbattle.me:5000/trainers/addPokebol', headers = {'trainer_token' : trainer_token}, json = {
    "pokemon_id": 1502
})

print(response_pokeball.text)
