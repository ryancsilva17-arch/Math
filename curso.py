class Curso:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao  # em semestres

    def descricao(self):
        return f"Curso de {self.nome}, duração de {self.duracao} semestres."
