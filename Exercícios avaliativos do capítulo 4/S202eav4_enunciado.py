###                           ##              ####
  ####                          ###              ####
  ###  ##########   ######## ########  #######   ####
 ####  ##### ####  ####  ####  ###   ####  #### #### 
 ####  ###   ####   ########  ####  ########### #### 
####  ####   #### ####  ####  ####  ####        ###  
####  ###    ### ########### ###### ########## ####                 S202 - Banco de dados II
#### ####   ####  ##########  ####   ######    ###       Prof. Dr. Jonas Lopes de Vilas Boas

# Exercício Avaliativo 4 - Banco de dados orientado à colunas e Cassandra

"""
Estoque da Montadora 

Um fabricante de automóveis contratou você para desenvolver um sistema de banco de dados distribuído usando o Cassandra para as linhas de montagem de toda a corporação, onde cada máquina pudesse acessar a base de dados e buscar as peças de maneira correta para ser montada nos respectivos modelos de veículos. Para isso, você deverá criar a tabela estoque no sistema DataStax ASTRA e inserir as colunas usando o arquivo auxiliar disponibilizado junto com essa atividade. 

Questão 1: Siga os itens listados abaixo: 

Faça a inserção de uma nova peça com os dados abaixo: 

id: 5 
nome: Pistao 
carro: Mustang 
estante: 4 
nível: 1 
quantidade: 167 

Faça a inserção de uma nova peça com os dados abaixo: 

id: 4
nome: Suspencao 
carro: Argo 
estante: 1 
nível: 1 
quantidade: 3500 

Questão 2: Escreva o comando CQL utilizado para cada item abaixo: 

Faça uma busca no banco de dados que retorno todos os dados do item com nome 'Pistão';
Faça uma busca no banco que calcule a média aritmética da quantidade de todas as colunas armazenadas na tabela;
Faça uma busca que retorne quantas colunas tem armazenadas na tabela;
Busque a maior e a menor quantidade de peças usando as alias "maior quantidade" e "menor quantidade" para a tabela estoque. 
Faça uma busca que retorne os atributos nome, carro e quantidade, onde a estante seja igual a 3;
Faça uma busca que retorne a média aritmética da quantidade onde o nível seja igual a 1; 
Faça uma busca retornando todos os atributos onde a estante seja menor do que 3 e o nível seja maior do que 4.
 

Questão 3: Elabore um script Python que seja capaz de fazer uma consulta mostrando nome, estante e quantidade do carro fornecido pelo usuário. 

"""

import json
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import dict_factory

class CassandraConnector:
    def __init__(self):
        self.cassandra_session = None

    def get_cassandra_connector(self):
        if self.cassandra_session is None:
            # Configuração da conexão segura com o Astra
            cloud_config = {
                "secure_connect_bundle": "c:\Users\ViniS\OneDrive\Downloads\secure-connect-db-estoque.zip"  # Substitua <database_name> pelo nome do seu banco de dados
            }

            # Carregar credenciais do arquivo JSON
            with open("s202-token.json") as f:
                secrets = json.load(f)

            CLIENT_ID = secrets["clientId"]
            CLIENT_SECRET = secrets["secret"]

            # Configuração do provedor de autenticação
            auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            self.cassandra_session = cluster.connect()
            self.cassandra_session.row_factory = dict_factory
            
            # Definir o keyspace para uso
            self.cassandra_session.set_keyspace("ksestoque")  # Substitua "montadora" pelo seu keyspace

        return self.cassandra_session

# Classe representando uma peça de automóvel
class AutoPart:
    def __init__(self, name, car, shelf, level, amount):
        self.name = name
        self.car = car
        self.shelf = shelf
        self.level = level
        self.amount = amount

    def to_dict(self):
        return {
            "name": self.name,
            "car": self.car,
            "shelf": self.shelf,
            "level": self.level,
            "amount": self.amount
        }


class AutoPartDAO:
    def __init__(self):
        self.cassandra_session = CassandraConnector.get_cassandra_connector()

    def create_table(self):
        pass
    
    def add_part(self, part):
        pass
    
    def get_part(self, part_name):
        pass

    def calculate_average_amount(self):
        pass

    def compute_total_amount(self):
        pass

    def find_max_min_amount(self):
        pass

    def get_shelf_parts(self, shelf):
        pass

    def get_average_amount_from_level(self, shelf, level):
        pass

    def fetch_parts_by_shelf_and_level(self, shelf, level):
        pass

    def retrieve_car_parts(self, car):  # Questão 3 (Buscar peças de um carro específico)
        query = """
        SELECT nome, estante, quantidade FROM estoque WHERE carro = %s ALLOW FILTERING;
        """
        rows = self.cassandra_session.execute(query, (car,))
        return [row for row in rows]
    
    def check_inventory(self):  # Questão 3 (Consulta de estoque)
        car = input("Informe o modelo do carro desejado: ")
        parts = self.retrieve_car_parts(car)
        if parts:
            for part in parts:
                print(f"Peça: {part['nome']}, Estante: {part['estante']}, Quantidade: {part['quantidade']}")
        else:
            print("Nenhuma peça encontrada para o carro especificado.")

AutoPartDAO().check_inventory()  # Executa a consulta de estoque