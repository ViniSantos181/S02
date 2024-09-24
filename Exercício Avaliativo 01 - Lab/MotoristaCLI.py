from classes import Passageiro
from classes import Corrida
from classes import Motorista
from motoristaDAO import MotoristaDAO

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista):
        super().__init__()
        self.motorista = motorista
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)
    def create_motorista(self):
        continuar = True
        nota = int(input("Digite a nota do Motorista: "))
        
        corridas = []    
        while(continuar):
            print("Dados da corrida: ")
            nome = input("Digite o nome do passageiro: ")
            documento = input("Digite o documento do passageiro: ")
            passageiro = Passageiro(nome, documento)
            nota = int(input("Digite a nota da Corrida: "))
            distancia = float(input("Digite a distancia da Corrida: "))
            valor = float(input("Digite o valor da Corrida: "))
            addCorrida = 0
            while addCorrida not in [1, 2]:
                addCorrida = int(input("Adicionar outra corrida (1-Sim 2-Não)"))
                if addCorrida == 2:
                    continuar = False
            corrida = Corrida(nota, distancia, valor, passageiro)
            corridas.append(corrida)

        motorista = Motorista(corridas, nota)
        self.motorista.create_motorista(motorista)

    def read_motorista(self):
        id = input("Digite o id do motorista: ")
        motorista = self.motorista.read_motorista_by_id(id)
        if motorista:
            print(f"Nota do motorista: {motorista['nota']}")
            print(f"Corridas: {motorista['corridas']}")

    def update_motorista(self):
        id = input("Digite o id do motorista que deseja atualizar: ")
        nota = int(input("Digite a nova nota do Motorista: "))
        self.motorista.update_motorista(id, nota)

    def delete_motorista(self):
        id = input("Digite o id: ")
        self.motorista.delete_motorista(id)

    def run(self):
        print("Bem vindo ao Motorista CLI")
        print("Comandos: create, read, update, delete, quit ")
        super().run()