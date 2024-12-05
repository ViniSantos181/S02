import logging

class Medico:
    def __init__(self, db):
        self.db = db
        logging.basicConfig(level=logging.DEBUG)

    def criar_medico(self, nome, crm, especialidade, telefone):
        query = (
            f"CREATE (m:Medico {{nome: '{nome}', crm: '{crm}', especialidade: '{especialidade}', telefone: '{telefone}'}})"
        )
        logging.debug(f"Executing query: {query}")
        self.db.execute_query(query)

    def listar_medicos(self):
        query = "MATCH (m:Medico) RETURN m"
        logging.debug(f"Executing query: {query}")
        result = self.db.execute_query(query)
        
        records = list(result)
        
        medicos = []
        for record in records:
            medico = {
                "nome": record["m"]["nome"],
                "crm": record["m"]["crm"],
                "especialidade": record["m"]["especialidade"],
                "telefone": record["m"]["telefone"]
            }
            medicos.append(medico)
        return medicos

    def atualizar_medico(self, crm, nome, especialidade, telefone):
        query = (
            f"MATCH (m:Medico {{crm: '{crm}'}}) "
            f"SET m.nome = '{nome}', m.especialidade = '{especialidade}', m.telefone = '{telefone}'"
        )
        logging.debug(f"Executing query: {query}")
        self.db.execute_query(query)

    def deletar_medico(self, crm):
        query = f"MATCH (m:Medico {{crm: '{crm}'}}) DELETE m"
        logging.debug(f"Executing query: {query}")
        self.db.execute_query(query)