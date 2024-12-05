import logging

class Consulta:
    def __init__(self, db):
        self.db = db
        logging.basicConfig(level=logging.DEBUG)

    def criar_consulta(self, cpf_paciente, crm_medico, data_hora):
        query = (
            f"MATCH (p:Paciente {{cpf: '{cpf_paciente}'}}), (m:Medico {{crm: '{crm_medico}'}}) "
            f"CREATE (p)-[:AGENDOU]->(c:Consulta {{data_hora: '{data_hora}'}}), (m)-[:REALIZA]->(c)"
        )
        logging.debug(f"Executing query: {query}")
        self.db.execute_query(query)

    def listar_consultas(self):
        query = "MATCH (c:Consulta)-[:AGENDOU]->(p:Paciente), (c)-[:REALIZA]->(m:Medico) RETURN c, p, m"
        logging.debug(f"Executing query: {query}")
        result = self.db.execute_query(query)
        
        # Consumir o resultado antes de iterar
        records = list(result)
        
        consultas_info = []
        for record in records:
            consulta = record["c"]
            paciente = record["p"]
            medico = record["m"]
            consulta_info = {
                "data_hora": consulta["data_hora"],
                "paciente_nome": paciente["nome"],
                "medico_nome": medico["nome"]
            }
            consultas_info.append(consulta_info)
        return consultas_info

    def atualizar_consulta(self, cpf_paciente, crm_medico, data_hora, nova_data_hora):
        query = (
            f"MATCH (p:Paciente {{cpf: '{cpf_paciente}'}})-[:AGENDOU]->(c:Consulta {{data_hora: '{data_hora}'}}), "
            f"(m:Medico {{crm: '{crm_medico}'}})-[:REALIZA]->(c) "
            f"SET c.data_hora = '{nova_data_hora}'"
        )
        logging.debug(f"Executing query: {query}")
        self.db.execute_query(query)

    def deletar_consulta(self, cpf_paciente, crm_medico, data_hora):
        query = (
            f"MATCH (p:Paciente {{cpf: '{cpf_paciente}'}})-[:AGENDOU]->(c:Consulta {{data_hora: '{data_hora}'}}), "
            f"(m:Medico {{crm: '{crm_medico}'}})-[:REALIZA]->(c) "
            f"DELETE c"
        )
        logging.debug(f"Executing query: {query}")
        self.db.execute_query(query)