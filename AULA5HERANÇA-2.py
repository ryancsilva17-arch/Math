class Aluno:
    def __init__(self, nome, matricula):
        self.__nome = None
        self.__matricula = None
        self.__notas = []
        self.set_nome(nome)
        self.set_matricula(matricula)

    def get_nome(self): return self.__nome
    def set_nome(self, nome):
        if nome.strip(): self.__nome = nome
        else: print("Nome inválido.")

    def get_matricula(self): return self.__matricula
    def set_matricula(self, matricula):
        if matricula.isdigit() and 8 <= len(matricula) <= 10: self.__matricula = matricula
        else: print("Matrícula inválida.")

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10: self.__notas.append(nota)

    def calcular_media(self):
        return sum(self.__notas) / len(self.__notas) if self.__notas else 0

    def mostrar_dados(self):
        print(f"Nome: {self.get_nome()} | Matrícula: {self.get_matricula()} | Média: {self.calcular_media():.2f}")

# --- SUBCLASSES ---

class AlunoSubsequente(Aluno):
    def __init__(self, nome, matricula, turno):
        super().__init__(nome, matricula) 
        self.turno = turno

    def mostrar_dados(self):
        # Polimorfismo: Adiciona o cabeçalho e chama o comportamento da classe pai
        print(f"[SUBSEQUENTE] ", end="")
        super().mostrar_dados()
        print(f"Turno: {self.turno}")
        print("-" * 30)

class AlunoPosGraduacao(Aluno):
    def __init__(self, nome, matricula, area_pesquisa):
        super().__init__(nome, matricula)
        self.area_pesquisa = area_pesquisa

    def mostrar_dados(self):
        print(f"[PÓS-GRADUAÇÃO] ", end="")
        super().mostrar_dados()
        print(f"Área de Pesquisa: {self.area_pesquisa}")
        print("-" * 30)

# --- EXECUÇÃO ---

aluno1 = AlunoSubsequente("João Silva", "12345678", "Noturno")
aluno1.adicionar_nota(8.5)

aluno2 = AlunoPosGraduacao("Ana Costa", "987654321", "Inteligência Artificial")
aluno2.adicionar_nota(9.8)

list_alunos = [aluno1, aluno2]

print("\n--- CADASTRO DE ALUNOS ---")
for aluno in list_alunos:
    aluno.mostrar_dados()