import requests
import random

BASE_URL = 'https://pokeapi.co/api/v2/pokemon/ditto'


def get_pokemon_data(pokemon_name):
    response = requests.get(BASE_URL + pokemon_name.lower())
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Pokemon {pokemon_name} not found!")
        return None


def display_pokemon_info(pokemon):
    print(f"{pokemon['name'].capitalize()} - Type: {[t['type']['name'] for t in pokemon['types']]}")
    print("Abilities:", [a['ability']['name'] for a in pokemon['abilities']])
    print("Moves:", [m['move']['name'] for m in pokemon['moves'][:5]])
    print("HP:", pokemon['stats'][0]['base_stat'])
    print("Attack:", pokemon['stats'][1]['base_stat'])
    print("Defense:", pokemon['stats'][2]['base_stat'])


def battle(pokemon1, pokemon2):
    hp1 = pokemon1['stats'][0]['base_stat']
    hp2 = pokemon2['stats'][0]['base_stat']

    attack1 = pokemon1['stats'][1]['base_stat']
    defense2 = pokemon2['stats'][2]['base_stat']

    attack2 = pokemon2['stats'][1]['base_stat']
    defense1 = pokemon1['stats'][2]['base_stat']

    print("Battle Start!")
    while hp1 > 0 and hp2 > 0:
        damage_to_2 = max(1, attack1 - defense2 // 2)
        damage_to_1 = max(1, attack2 - defense1 // 2)

        if random.choice([True, False]):
            hp2 -= damage_to_2
            print(f"{pokemon1['name']} attacks {pokemon2['name']} and deals {damage_to_2} damage. {pokemon2['name']} has {hp2} HP left.")
        else:
            hp1 -= damage_to_1
            print(f"{pokemon2['name']} attacks {pokemon1['name']} and deals {damage_to_1} damage. {pokemon1['name']} has {hp1} HP left.")

    if hp1 > 0:
        print(f"{pokemon1['name']} wins!")
    else:
        print(f"{pokemon2['name']} wins!")


def main():
    pokemon_name1 = input("Enter the name of the first Pokemon: ")
    pokemon_name2 = input("Enter the name of the second Pokemon: ")

    pokemon1 = get_pokemon_data(pokemon_name1)
    pokemon2 = get_pokemon_data(pokemon_name2)

    if pokemon1 and pokemon2:
        print("\nPokemon 1 Info:")
        display_pokemon_info(pokemon1)

        print("\nPokemon 2 Info:")
        display_pokemon_info(pokemon2)

        battle(pokemon1, pokemon2)


if __name__ == '__main__':
    main()
