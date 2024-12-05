from database import Database
from models.paciente import Paciente
from models.medico import Medico
from models.consulta import Consulta

# Inicialize a conexão com o banco de dados
db = Database("neo4j+s://29696805.databases.neo4j.io:7687", "neo4j", "D3owZat0Ss70knccA9E_SJZ3tNlnr7CLJrGlpFTHm-I")  # Substitua com suas credenciais do Neo4j

# Instanciar as classes de modelos
paciente_model = Paciente(db)
medico_model = Medico(db)
consulta_model = Consulta(db)

# Funções de menu
def menu_principal():
    print("1 - Criar Paciente")
    print("2 - Listar Pacientes")
    print("3 - Atualizar Paciente")
    print("4 - Deletar Paciente")
    print("5 - Criar Médico")
    print("6 - Listar Médicos")
    print("7 - Atualizar Médico")
    print("8 - Deletar Médico")
    print("9 - Agendar Consulta")
    print("10 - Listar Consultas")
    print("11 - Atualizar Consulta")
    print("12 - Deletar Consulta")
    print("13 - Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        criar_paciente()
    elif opcao == '2':
        listar_pacientes()
    elif opcao == '3':
        atualizar_paciente()
    elif opcao == '4':
        deletar_paciente()
    elif opcao == '5':
        criar_medico()
    elif opcao == '6':
        listar_medicos()
    elif opcao == '7':
        atualizar_medico()
    elif opcao == '8':
        deletar_medico()
    elif opcao == '9':
        agendar_consulta()
    elif opcao == '10':
        listar_consultas()
    elif opcao == '11':
        atualizar_consulta()
    elif opcao == '12':
        deletar_consulta()
    elif opcao == '13':
        print("Saindo...")
        exit()
    else:
        print("Opção inválida.")
        menu_principal()

# Funções CRUD para Paciente
def criar_paciente():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    endereco = input("Endereço: ")
    paciente_model.criar_paciente(nome, cpf, telefone, email, endereco)
    print("Paciente criado com sucesso!")
    menu_principal()

def listar_pacientes():
    pacientes = paciente_model.listar_pacientes()
    for paciente in pacientes:
        print(paciente)
    menu_principal()

def atualizar_paciente():
    cpf = input("CPF do paciente a ser atualizado: ")
    nome = input("Novo nome: ")
    telefone = input("Novo telefone: ")
    email = input("Novo email: ")
    endereco = input("Novo endereço: ")
    paciente_model.atualizar_paciente(cpf, nome, telefone, email, endereco)
    print("Paciente atualizado com sucesso!")
    menu_principal()

def deletar_paciente():
    cpf = input("CPF do paciente a ser deletado: ")
    paciente_model.deletar_paciente(cpf)
    print("Paciente deletado com sucesso!")
    menu_principal()

# Funções CRUD para Médico
def criar_medico():
    nome = input("Nome: ")
    crm = input("CRM: ")
    especialidade = input("Especialidade: ")
    telefone = input("Telefone: ")
    medico_model.criar_medico(nome, crm, especialidade, telefone)
    print("Médico criado com sucesso!")
    menu_principal()

def listar_medicos():
    medicos = medico_model.listar_medicos()
    for medico in medicos:
        print(medico)
    menu_principal()

def atualizar_medico():
    crm = input("CRM do médico a ser atualizado: ")
    nome = input("Novo nome: ")
    especialidade = input("Nova especialidade: ")
    telefone = input("Novo telefone: ")
    medico_model.atualizar_medico(crm, nome, especialidade, telefone)
    print("Médico atualizado com sucesso!")
    menu_principal()

def deletar_medico():
    crm = input("CRM do médico a ser deletado: ")
    medico_model.deletar_medico(crm)
    print("Médico deletado com sucesso!")
    menu_principal()

# Funções CRUD para Consulta
def agendar_consulta():
    cpf_paciente = input("CPF do paciente: ")
    crm_medico = input("CRM do médico: ")
    data_hora = input("Data e hora da consulta (AAAA-MM-DD HH:MM): ")
    consulta_model.criar_consulta(cpf_paciente, crm_medico, data_hora)
    print("Consulta agendada com sucesso!")
    menu_principal()

def listar_consultas():
    consultas = consulta_model.listar_consultas()
    for consulta in consultas:
        print(consulta)
    menu_principal()

def atualizar_consulta():
    cpf_paciente = input("CPF do paciente: ")
    crm_medico = input("CRM do médico: ")
    data_hora = input("Data e hora da consulta: ")
    nova_data_hora = input("Nova data e hora: ")
    consulta_model.atualizar_consulta(cpf_paciente, crm_medico, data_hora, nova_data_hora)
    print("Consulta atualizada com sucesso!")
    menu_principal()

def deletar_consulta():
    cpf_paciente = input("CPF do paciente: ")
    crm_medico = input("CRM do médico: ")
    data_hora = input("Data e hora da consulta: ")
    consulta_model.deletar_consulta(cpf_paciente, crm_medico, data_hora)
    print("Consulta deletada com sucesso!")
    menu_principal()

# Inicia o menu principal
menu_principal()
