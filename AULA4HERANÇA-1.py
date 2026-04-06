class Aluno:
    def __init__(self, nome, matricula):
        # Atributos privados
        self.__nome = None
        self.__matricula = None
        self.__notas = []

        # Inicialização com validação
        self.set_nome(nome)
        self.set_matricula(matricula)

    # Getter e Setter para nome
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if nome and nome.strip():
            self.__nome = nome
        else:
            print("Nome inválido. Por favor, insira um nome válido.")

    # Getter e Setter para matrícula
    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        if matricula.isdigit() and 8 <= len(matricula) <= 10:
            self.__matricula = matricula
        else:
            print("Matrícula inválida. Deve conter entre 8 e 10 dígitos.")

    # Adicionar nota
    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.__notas.append(nota)
        else:
            print("Nota inválida!")

    # Calcular média
    def calcular_media(self):
        if len(self.__notas) == 0:
            return 0
        return sum(self.__notas) / len(self.__notas)

    # Novo método solicitado
    def mostrar_dados(self):
        print(f"Nome: {self.get_nome()}")
        print(f"Matrícula: {self.get_matricula()}")
        print(f"Média: {self.calcular_media():.2f}")
        print("-" * 30)


# Criando os alunos
aluno1 = Aluno("João", "2025101035")
aluno1.adicionar_nota(8.0)
aluno1.adicionar_nota(7.0)

aluno2 = Aluno("Maria", "2025123456")
aluno2.adicionar_nota(9.0)
aluno2.adicionar_nota(6.5)

aluno3 = Aluno("Carlos", "2025987654")
aluno3.adicionar_nota(5.0)
aluno3.adicionar_nota(7.5)
aluno3.adicionar_nota(8.0)

# Exibindo os dados
aluno1.mostrar_dados()
aluno2.mostrar_dados()
aluno3.mostrar_dados()

# Definição da classe Aluno
class Aluno:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula
        self.__notas = []

    def get_nome(self):
        return self.__nome

    def get_matricula(self):
        return self.__matricula

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.__notas.append(nota)
        else:
            print("Nota inválida.")

    def calcular_media(self):
        if self.__notas:
            return sum(self.__notas) / len(self.__notas)
        return 0


# Subclasse de Aluno
class AlunoGraduacao(Aluno):
    def __init__(self, nome, matricula, curso):
        # Chamando o construtor da classe pai
        super().__init__(nome, matricula)
        self.__curso = curso

    # Getter e Setter para curso
    def get_curso(self):
        return self.__curso

    def set_curso(self, curso):
        if curso and curso.strip():
            self.__curso = curso
        else:
            print("Curso inválido.")

    # Sobrescrevendo mostrar_dados para incluir curso
    def mostrar_dados(self):
        print(f"Nome: {self.get_nome()}")
        print(f"Matrícula: {self.get_matricula()}")
        print(f"Curso: {self.get_curso()}")
        print(f"Média: {self.calcular_media():.2f}")
        print("-" * 30)


# Testando a subclasse
aluno_grad = AlunoGraduacao("Ana", "GRAD20251234", "Engenharia de Software")
aluno_grad.adicionar_nota(9.0)
aluno_grad.adicionar_nota(8.5)

aluno_grad.mostrar_dados()

# Definição da classe Aluno
class Aluno:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula
        self.__notas = []

    def get_nome(self):
        return self.__nome

    def get_matricula(self):
        return self.__matricula

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.__notas.append(nota)
        else:
            print("Nota inválida.")

    def calcular_media(self):
        if self.__notas:
            return sum(self.__notas) / len(self.__notas)
        return 0


# Subclasse de Aluno
class AlunoTecnico(Aluno):
    def __init__(self, nome, matricula, curso):
        # Chamando o construtor da classe pai
        super().__init__(nome, matricula)
        self.__curso = curso

    # Getter e Setter para curso
    def get_curso(self):
        return self.__curso

    def set_curso(self, curso):
        if curso and curso.strip():
            self.__curso = curso
        else:
            print("Curso inválido.")

    # Sobrescrevendo mostrar_dados para incluir curso
    def mostrar_dados(self):
        print(f"Nome: {self.get_nome()}")
        print(f"Matrícula: {self.get_matricula()}")
        print(f"Curso: {self.get_curso()}")
        print(f"Média: {self.calcular_media():.2f}")
        print("-" * 30)


# Testando a subclasse
aluno_grad = AlunoTecnico("RYAN", "TEC30154252", "REDE DE COMPUTADORES") 
aluno_grad.adicionar_nota(8.0)
aluno_grad.adicionar_nota(8.0)

aluno_grad.mostrar_dados()