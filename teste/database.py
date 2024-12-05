from neo4j import GraphDatabase

class Database:
    def __init__(self, uri, user, password):
        self.uri = uri
        self.user = user
        self.password = password
        self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))

    def execute_query(self, query):
        with self.driver.session() as session:
            result = session.run(query)
            return result
