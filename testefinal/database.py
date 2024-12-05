from neo4j import GraphDatabase
import logging

class Database:
    def __init__(self, uri, user, password):
        self.uri = uri
        self.user = user
        self.password = password
        self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))
        logging.basicConfig(level=logging.DEBUG)

    def execute_query(self, query):
        logging.debug(f"Executing query: {query}")
        with self.driver.session() as session:
            result = session.run(query)
            return result