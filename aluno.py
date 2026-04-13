class Aluno:
    def __init__(self, nome, matricula, curso=None):
        self.__nome = None
        self.__matricula = None
        self.__curso = None
        self.__notas = []
        self.set_nome(nome)
        self.set_matricula(matricula)
        self.set_curso(curso)

    # Getter para o nome:
    def get_nome(self):
        return self.__nome

    # Setter para o nome, com validação: não pode ser vazio ou só espaços
    def set_nome(self, nome):
        if nome and nome.strip():
            self.__nome = nome
        else:
            print("Nome inválido. Por favor, insira um nome válido.")

    # Getter para a matrícula
    def get_matricula(self):
        return self.__matricula

    # Setter para matrícula com validação: número entre 8 e 10 dígitos
    def set_matricula(self, matricula):
        if matricula.isdigit() and 8 <= len(matricula) <= 10:
            self.__matricula = matricula
        else:
            print("Matrícula inválida. Deve conter entre 8 e 10 dígitos.")

    # Getter para o curso
    def get_curso(self):
        return self.__curso

    # Setter para o curso. Aceita Curso ou None.
    def set_curso(self, curso):
        if curso is None:
            self.__curso = None
        else:
            from curso import Curso

            if isinstance(curso, Curso):
                self.__curso = curso
            else:
                print("Curso inválido. Informe um objeto Curso.")

    # Adicionar nota com validação
    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.__notas.append(nota)
        else:
            print("Nota inválida!")

    # Calcular média das notas
    def calcular_media(self):
        if len(self.__notas) == 0:
            return 0
        return sum(self.__notas) / len(self.__notas)

    def __str__(self):
        curso_texto = self.__curso.descricao() if self.__curso else "Nenhum curso definido"
        return (
            f"Aluno: {self.get_nome()}, Matrícula: {self.get_matricula()}, "
            f"Curso: {curso_texto}, Média: {self.calcular_media():.2f}"
        )
