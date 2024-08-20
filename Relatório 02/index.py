class Professor:
    def __init__(self, nome):
        self.nome = nome

class Aluno:
    def __init__(self, nome):
        self.nome = nome

class Aula:
    def __init__(self, professor, assunto):
        self.professor = professor
        self.assunto = assunto
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

professor1 = Professor("Lucas Souza")
professor2 = Professor("Ana Silva")
professor3 = Professor("Carlos Mendes")

alunos_aula1 = [Aluno("Maria"), Aluno("Pedro"), Aluno("João"), Aluno("Ana")]
alunos_aula2 = [Aluno("Mariana"), Aluno("Roberto"), Aluno("Fernanda"), Aluno("José")]
alunos_aula3 = [Aluno("Lucas"), Aluno("Bruna"), Aluno("Tiago"), Aluno("Carla")]

aula1 = Aula(professor1, "Matemática")
for aluno in alunos_aula1:
    aula1.adicionar_aluno(aluno)

aula2 = Aula(professor2, "História")
for aluno in alunos_aula2:
    aula2.adicionar_aluno(aluno)

aula3 = Aula(professor3, "Química")
for aluno in alunos_aula3:
    aula3.adicionar_aluno(aluno)

collection_aula = {
    "aulas": [
        {
            "professor": {"nome": aula1.professor.nome},
            "assunto": aula1.assunto,
            "alunos": [{"nome": aluno.nome} for aluno in aula1.alunos]
        },
        {
            "professor": {"nome": aula2.professor.nome},
            "assunto": aula2.assunto,
            "alunos": [{"nome": aluno.nome} for aluno in aula2.alunos]
        },
        {
            "professor": {"nome": aula3.professor.nome},
            "assunto": aula3.assunto,
            "alunos": [{"nome": aluno.nome} for aluno in aula3.alunos]
        }
    ]
}