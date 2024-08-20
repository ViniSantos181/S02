from database import Database
from helper.WriteAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")

#pokemons por fraquesas
def getPokemonsByWeaknesses(weaknesses: list):
    return db.collection.find({"weaknesses": {"$in": weaknesses}})

types = ["Fire","Ice"]
pokemons1 = getPokemonsByWeaknesses(types)

writeAJson(pokemons1, "pokemons_by_weaknesses")

#pokemons por chance de spawn
def getPokemonsBySpawn_chance(min: float, max: float):
    return db.collection.find({"spawn_chance": {"$gt": min, "$lt": max}})

spawn_chance_min = 0.2
spawn_chance_max = 0.8
pokemons2 = getPokemonsBySpawn_chance(spawn_chance_min, spawn_chance_max)

writeAJson(pokemons2, "PokemonsBySpawn_chance")

#pokemons por peso
def getPokemonsByWeight(weight: str):
    return db.collection.find({"weight": {"$in": weight}})

weight = ["1.0 kg"]
pokemons3 = getPokemonsByWeight(weight)

writeAJson(pokemons3, "PokemonsByWeight")

#pokemons por doces
def getPokemonsByCandy_count(min: int, max: int):
    return db.collection.find({"candy_count": {"$gt": min, "$lt": max}})

candy_min = [25]
candy_max = [100]
pokemons4 = getPokemonsByCandy_count(candy_min, candy_max)

writeAJson(pokemons4, "PokemonsByHeight")

#pokemons por altura
def getPokemonsByHeight(height: str):
    return db.collection.find({"height": {"$in": weight}})

height = ["0.5 m"]
pokemons5 = getPokemonsByHeight(height)

writeAJson(pokemons5, "PokemonsByHeight")