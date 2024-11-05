class TeacherCRUD:
    def __init__(self, database):
        self.db = database
    
    def create(self, ano_nasc, name, cpf):
        query = "CREATE (:Teacher {ano_nasc: $ano_nasc, name: $name, cpf: $cpf}) "
        parameters = {"ano_nasc": ano_nasc, "name": name, "cpf": cpf}
        self.db.execute_query(query, parameters)
    
    def read(self, name):
        query = "MATCH (t:Teacher {name:$name}) RETURN t.name AS nome LIMIT 1;"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return [results]
    
    def delete(self, name):
      query = "MATCH (t:Teacher {name:$name}) DETACH DELETE t;"
      parameters = {"name": name}
      self.db.execute_query(query, parameters)
    
    def update(self, name, newCpf):
        query =  "MATCH (t:Teacher {name:$name}) SET t.cpf = $newCpf;"
        parameters = {"name": name, "newCpf": newCpf}
        self.db.execute_query(query, parameters)