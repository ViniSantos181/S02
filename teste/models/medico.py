class Medico:
    def __init__(self, db):
        self.db = db

    def criar_medico(self, nome, crm, especialidade, telefone):
        query = (
            f"CREATE (m:Medico {{nome: '{nome}', crm: '{crm}', especialidade: '{especialidade}', telefone: '{telefone}'}})"
        )
        self.db.execute_query(query)

    def listar_medicos(self):
        query = "MATCH (m:Medico) RETURN m"
        result = self.db.execute_query(query)
        medicos = []
        for record in result:
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
        self.db.execute_query(query)

    def deletar_medico(self, crm):
        query = f"MATCH (m:Medico {{crm: '{crm}'}}) DELETE m"
        self.db.execute_query(query)
