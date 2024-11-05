from database import Database
db = Database("bolt://98.84.114.137", "neo4j", "rest-lesson-stopper")

query = "MATCH (t:Teacher {name:'Renzo'}) RETURN t.ano_nasc AS ano, t.cpf AS cpf"
results = db.execute_query(query)
print ([(result["ano"], result["cpf"]) for result in results])

query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS nome, t.cpf AS cpf;"
results = db.execute_query(query)
print([(result["nome"], result["cpf"]) for result in results])

query = "MATCH (c:City) RETURN c.name AS cidade, c.cep AS cep, c.population AS populacao;"
results = db.execute_query(query)
print ([(result["cidade"], result["cep"],result["populacao"]) for result in results])

query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name AS nome, s.endereco AS endereco, s.number AS numero;"
results = db.execute_query(query)
print ([(result["nome"], result["endereco"],result["numero"]) for result in results])

query = "MATCH (t:Teacher) RETURN min(t.ano_nasc) AS mais_velho, max(t.ano_nasc) AS mais_jovem;"
results = db.execute_query(query)
print([(result["mais_velho"], result["mais_jovem"]) for result in results])

query = "MATCH (c:City) RETURN avg(c.population) AS media;"
results = db.execute_query(query)
print([(result["media"]) for result in results])

query = "MATCH (c:City {cep: '37540-000'}) RETURN replace(c.name, 'a', 'A') AS nome;"
results = db.execute_query(query)
print([(result["nome"]) for result in results])