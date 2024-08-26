from pokedex import Pokedex
from database import Database

def main():
    # Instancia o objeto Database
    db = Database(database="pokedex", collection="pokemons")

    # Instancia a classe Pokedex
    pokedex = Pokedex(db)

    # Pokémons por fraquezas
    types = ["Fire", "Ice"]
    pokedex.getPokemonsByWeaknesses(types)
    

    # Pokémons por chance de spawn
    spawn_chance_min = 0.2
    spawn_chance_max = 0.8
    pokedex.getPokemonsBySpawn_chance(spawn_chance_min, spawn_chance_max)
    

    # Pokémons por peso
    weight = "1.0 kg"
    pokedex.getPokemonsByWeight(weight)

    # Pokémons por doces
    candy_min = 25
    candy_max = 100
    pokedex.getPokemonsByCandy_count(candy_min, candy_max)

    # Pokémons por altura
    height = "1.60 m"
    pokedex.getPokemonsByHeight(height)

if __name__ == "__main__":
    main()