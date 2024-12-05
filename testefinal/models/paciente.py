import logging

class Paciente:
    def __init__(self, db):
        self.db = db
        logging.basicConfig(level=logging.DEBUG)

    def criar_paciente(self, nome, cpf, telefone, email, endereco):
        query = (
            f"CREATE (p:Paciente {{nome: '{nome}', cpf: '{cpf}', telefone: '{telefone}', email: '{email}', endereco: '{endereco}'}})"
        )
        logging.debug(f"Executing query: {query}")
        self.db.execute_query(query)

    def listar_pacientes(self):
        query = "MATCH (p:Paciente) RETURN p"
        logging.debug(f"Executing query: {query}")
        results = self.db.execute_query(query)
        
        # Consumir o resultado antes de iterar
        records = list(results)
        
        pacientes_info = []
        for record in records:
            paciente = record["p"]
            paciente_info = {
                "nome": paciente["nome"],
                "cpf": paciente["cpf"],
                "telefone": paciente["telefone"],
                "email": paciente["email"],
                "endereco": paciente["endereco"]
            }
            pacientes_info.append(paciente_info)
        return pacientes_info

    def atualizar_paciente(self, cpf, nome, telefone, email, endereco):
        query = (
            f"MATCH (p:Paciente {{cpf: '{cpf}'}}) "
            f"SET p.nome = '{nome}', p.telefone = '{telefone}', p.email = '{email}', p.endereco = '{endereco}'"
        )
        logging.debug(f"Executing query: {query}")
        self.db.execute_query(query)

    def deletar_paciente(self, cpf):
        query = f"MATCH (p:Paciente {{cpf: '{cpf}'}}) DELETE p"
        logging.debug(f"Executing query: {query}")
        self.db.execute_query(query)