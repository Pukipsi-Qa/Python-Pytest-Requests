import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c88e8b58f70e2df9fe6ab5f68294f3fb'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}

Body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

Body_change = {
    "pokemon_id": "72942",
    "name": "Max",
    "photo_id": 1
}

Body_catch = {
    "pokemon_id": "72942"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = Body_create)
print(response_create.text)

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = Body_change)
print(response_change.text)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = Body_catch)
print(response_catch.text)


