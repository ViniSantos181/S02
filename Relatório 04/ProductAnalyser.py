from database import Database
from helper.writeAJson import writeAJson

db = Database(database="mercado", collection="compras")
#db.resetDatabase()

class ProductAnalyzer:
    def total_sales_per_day(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": {"data": "$data_compra"},  
                "total_vendas": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}
            }},
            {"$group": {
                "_id": None,
                "vendas_por_dia": {
                    "$push": {
                        "data": "$_id.data",
                        "total_vendas": "$total_vendas"
                    }
                }
            }}
        ])
        writeAJson(result, "total de vendas por dia")

    def most_sold_product(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": "$produtos.descricao", 
                "quantidade_total": {"$sum": "$produtos.quantidade"}
            }},
            {"$sort": {"quantidade_total": -1}},  
            {"$limit": 1}  
        ])
        writeAJson(result, "Produto mais vendido")

    def highest_single_purchase(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": {"cliente_id": "$cliente_id", "compra_id": "$compra_id"},
                "total_compra": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}
            }},
            {"$group": {
                "_id": "$_id.cliente_id",
                "max_gasto": {"$max": "$total_compra"}
            }},
            {"$sort": {"max_gasto": -1}},
            {"$limit": 1} 
        ])
        writeAJson(result, "Maior compra única")

    def products_sold_more_than_once(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": "$produtos.descricao", 
                "quantidade_total": {"$sum": "$produtos.quantidade"}
            }},
            {"$match": {
                "quantidade_total": {"$gt": 1}  
            }},
            {"$project": {
                "_id": 0, 
                "produto": "$_id",  
                "quantidade_total": 1  
            }}
        ])
        writeAJson(result, "Produtos vendidos mais de uma vez")