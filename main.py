from cadastro import cadastrar_cursos, cadastrar_alunos, adicionar_notas, exibir_relatorio


def main():
    cursos = cadastrar_cursos()
    if not cursos:
        print("Nenhum curso cadastrado. Encerrando.")
        return

    alunos = cadastrar_alunos(cursos)
    if not alunos:
        print("Nenhum aluno cadastrado. Encerrando.")
        return

    adicionar_notas(alunos)
    exibir_relatorio(alunos)


if __name__ == "__main__":
    main()
