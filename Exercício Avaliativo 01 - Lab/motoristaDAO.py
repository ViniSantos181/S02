from pymongo import MongoClient
from bson.objectid import ObjectId

class MotoristaDAO: 
    def __init__(self, database):
        self.db = database
    
    def create_motorista(self, motorista):
        try:
            res = self.db.collection.insert_one({
                "corridas": [{
                    "nota": corrida.nota,
                    "distancia": corrida.distancia,
                    "valor": corrida.valor,
                    "passageiro": {
                        "nome": corrida.passageiro.nome,
                        "documento": corrida.passageiro.documento
                    }
                } for corrida in motorista.corridas], 
                "nota": motorista.nota
            })
            print(f"Motorista criado com o id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar motorista: {e}")
            return None
    
    def read_motorista_by_id(self,id:str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Motorista encontrado:")
            return res
        except Exception as e:
            print(f"Ocorreu um erro procurando motorista: {e}")
            return None
        
    def update_motorista(self, id: str, nota:int):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"nota": nota}})
            print(f"Motorista atualizado.")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro atualizando motorista: {e}")
            return None
        
    def delete_motorista(self, id:str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deletado.")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro deletando motorista: {e}")
            return None