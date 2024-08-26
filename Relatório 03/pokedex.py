from database import Database
from helper.writeAJson import writeAJson

class Pokedex:
    def __init__(self, database: Database):
        self.db = database

    def getPokemonsByWeaknesses(self, weaknesses: list):
        result = list(self.db.collection.find({"weaknesses": {"$in": weaknesses}}))
        writeAJson({"query": "getPokemonsByWeaknesses", "weaknesses": weaknesses, "result": result}, "log_getPokemonsByWeaknesses.json")
        return result

    def getPokemonsBySpawn_chance(self, min: float, max: float):
        result = list(self.db.collection.find({"spawn_chance": {"$gt": min, "$lt": max}}))
        writeAJson({"query": "getPokemonsBySpawn_chance", "min": min, "max": max, "result": result}, "log_getPokemonsBySpawn_chance.json")
        return result

    def getPokemonsByWeight(self, weight: str):
        result = list(self.db.collection.find({"weight": {"$in": [weight]}}))
        writeAJson({"query": "getPokemonsByWeight", "weight": weight, "result": result}, "log_getPokemonsByWeight.json")
        return result

    def getPokemonsByCandy_count(self, min: int, max: int):
        result = list(self.db.collection.find({"candy_count": {"$gt": min, "$lt": max}}))
        writeAJson({"query": "getPokemonsByCandy_count", "min": min, "max": max, "result": result}, "log_getPokemonsByCandy_count.json")
        return result

    def getPokemonsByHeight(self, height: str):
        result = list(self.db.collection.find({"height": {"$in": [height]}}))
        writeAJson({"query": "getPokemonsByHeight", "height": height, "result": result}, "log_getPokemonsByHeight.json")
        return result





        