from neo4j import GraphDatabase

class FamilyGraphClient:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
    
    def close(self):
        self.driver.close()
    
    # Consulta para encontrar os membros da familia com uma determinada profissao
    def find_family_members_with_profession(self, profession):
        with self.driver.session() as session:
            result = session.run(f"MATCH (p:Pessoa:{profession}) RETURN p.nome AS nome")
            for record in result:
                print(f"{record['nome']}")
    
    # Consulta para encontrar os pais de uma pessoa
    def find_parents_of_person(self, child_name):
        with self.driver.session() as session:
            result = session.run(
                "MATCH (p:Pessoa)-[r:PAI_DE|MAE_DE]->(c:Pessoa {nome: $child_name}) "
                "RETURN p.nome AS nome, type(r) AS relacao", 
                child_name=child_name)
            for record in result:
                print(f"{record['nome']} e {record['relacao']} {child_name}.")
    
    # Consulta para encontrar um relacionamento de uma pessoa e desde quando
    def find_relationship_of_person(self, person_name, relationship_type):
        with self.driver.session() as session:
            result = session.run(
                f"MATCH (p:Pessoa {{nome: $person_name}})-[r:{relationship_type}]->(q:Pessoa) "
                "RETURN q.nome AS nome, r.desde AS desde", 
                person_name=person_name)
            for record in result:
                print(f"{person_name} namora com {record['nome']} desde {record['desde']}.")

if __name__ == "__main__":

    client = FamilyGraphClient("bolt://localhost:7687", "neo4j", "12345678")

    # Consultas
    print("Engenheiros na familia:")
    client.find_family_members_with_profession("Engenheiro")
    
    print("\nPais de Joao:")
    client.find_parents_of_person("Joao")
    
    print("\nQuem Pedro namora e desde quando:")
    client.find_relationship_of_person("Pedro", "NAMORA_COM")

    client.close()