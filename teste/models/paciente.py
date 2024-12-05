class Paciente:
    def __init__(self, db):
        self.db = db

    def criar_paciente(self, nome, cpf, telefone, email, endereco):
        query = (
            f"CREATE (p:Paciente {{nome: '{nome}', cpf: '{cpf}', telefone: '{telefone}', email: '{email}', endereco: '{endereco}'}})"
        )
        self.db.execute_query(query)

    def listar_pacientes(self):
        query = "MATCH (p:Paciente) RETURN p"
        results = self.db.execute_query(query)
        
        # Armazena todos os registros em uma lista
        pacientes = [record["p"] for record in results]
        
        pacientes_info = []
        for paciente in pacientes:
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
        self.db.execute_query(query)

    def deletar_paciente(self, cpf):
        query = f"MATCH (p:Paciente {{cpf: '{cpf}'}}) DELETE p"
        self.db.execute_query(query)