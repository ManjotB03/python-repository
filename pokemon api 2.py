import requests
import random

# Fetch Pokemon data from PokeAPI
def get_pokemon(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {pokemon_name}")
        return None

# Display basic Pokemon info
def display_pokemon(pokemon):
    name = pokemon['name'].capitalize()
    types = [t['type']['name'] for t in pokemon['types']]
    abilities = [a['ability']['name'] for a in pokemon['abilities']]
    moves = [m['move']['name'] for m in pokemon['moves'][:4]]  # Get first 4 moves
    print(f"{name}: Type(s): {', '.join(types)} | Abilities: {', '.join(abilities)} | Moves: {', '.join(moves)}")

# Simulate a battle between two Pokemon
def battle(pokemon1, pokemon2):
    print(f"Battle: {pokemon1['name'].capitalize()} vs {pokemon2['name'].capitalize()}")

    p1_hp = pokemon1['stats'][0]['base_stat']
    p2_hp = pokemon2['stats'][0]['base_stat']

    p1_moves = [m['move']['name'] for m in pokemon1['moves'][:4]]
    p2_moves = [m['move']['name'] for m in pokemon2['moves'][:4]]

    while p1_hp > 0 and p2_hp > 0:
        p1_move = random.choice(p1_moves)
        p2_move = random.choice(p2_moves)
        p1_attack = random.randint(10, 30)
        p2_attack = random.randint(10, 30)

        print(f"{pokemon1['name'].capitalize()} uses {p1_move} and deals {p1_attack} damage!")
        p2_hp -= p1_attack
        if p2_hp <= 0:
            print(f"{pokemon2['name'].capitalize()} fainted!")
            break

        print(f"{pokemon2['name'].capitalize()} uses {p2_move} and deals {p2_attack} damage!")
        p1_hp -= p2_attack
        if p1_hp <= 0:
            print(f"{pokemon1['name'].capitalize()} fainted!")
            break

    if p1_hp > 0:
        print(f"{pokemon1['name'].capitalize()} wins!")
    else:
        print(f"{pokemon2['name'].capitalize()} wins!")

# Main game loop
def main():
    pokemon_name1 = input("Enter the name of your first Pokemon: ").strip()
    pokemon_name2 = input("Enter the name of your second Pokemon: ").strip()

    pokemon1 = get_pokemon(pokemon_name1)
    pokemon2 = get_pokemon(pokemon_name2)

    if pokemon1 and pokemon2:
        display_pokemon(pokemon1)
        display_pokemon(pokemon2)
        battle(pokemon1, pokemon2)

if __name__ == "__main__":
    main()
