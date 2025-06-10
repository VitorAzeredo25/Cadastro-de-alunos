alunos_turma_1 = []
alunos_turma_2 = []
alunos_turma_3 = []

#Descrição de cada aluno
def mostrar_turma(nome_turma, turma):
    print(f"\n--- Alunos da {nome_turma} ---")
    for aluno in turma:
        print(f"Nome: {aluno['nome']}")
        print(f"Notas: {aluno['notas']}")
        print(f"Média: {aluno['media']:.2f}")
        print(f"Situação: {aluno['situação']}")
        print("-" * 20)


#Estatisticas das Turmas
def analisar_turma(nome_turma, alunos):
    if not alunos:
        print(f"\nA {nome_turma} não tem alunos cadastrados.")
        return

    total_alunos = len(alunos)
    soma_medias = 0
    aprovados = reprovados = recuperacao = 0
    aluno_com_maior_media = alunos[0]

    for aluno in alunos:
        media = aluno["media"]
        soma_medias += media

        if media >= 7:
            aprovados += 1
        elif media >= 5:
            recuperacao += 1
        else:
            reprovados += 1

        if media > aluno_com_maior_media["media"]:
            aluno_com_maior_media = aluno

    media_geral = soma_medias / total_alunos

    print(f"\n Relatório da {nome_turma}:")
    print(f"- Alunos cadastrados: {total_alunos}")
    print(f"- Média geral da turma: {media_geral:.2f}")
    print(f"- Aprovados: {aprovados}")
    print(f"- Recuperação: {recuperacao}")
    print(f"- Reprovados: {reprovados}")
    print(f"- Aluno com maior média: {aluno_com_maior_media['nome']} ({aluno_com_maior_media['media']:.2f})")


#Validação de nome
def validar_nome(nome):
    nome = nome.strip()

    if not nome:
        return False, "O nome não pode estar vazio."

    if len(nome) < 2:
        return False, "O nome deve ter pelo menos 2 letras."

    if not all(parte.isalpha() or parte.isspace() for parte in nome):
        return False, "O nome deve conter apenas letras e espaços."

    if len(nome) > 50:
        return False, "O nome é muito longo."

    return True, nome.title()



while True:

    while True:
        nome = input("Digite o nome do aluno: ")
        valido, resultado = validar_nome(nome)

        if valido:
            nome = resultado
            break
        else:
            print(f"Erro: {resultado}")
    

    notas_aluno = []

    while True:
        quantidade_input = input("Quantas notas adicionar? ")
        if quantidade_input.isdigit() and int(quantidade_input) > 0:
            quantidade = int(quantidade_input)
            break
        else:
            print("Digite um número inteiro positivo válido.")

    for index in range(quantidade):
        while True:
            try:
                nota = int(input(f"Qual a {index + 1}º nota? "))
                if 0 <= nota <= 10:
                    notas_aluno.append(nota)
                    break
                else:
                    print("Digite um número entre 0 e 10.")
            except ValueError:
                print("Digite um valor válido.")
    

    media = sum(notas_aluno) / len(notas_aluno)

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"


    aluno = {
        "nome": nome,
        "notas": notas_aluno,
        "media": media,
        "situação": situacao
    }


    while True:
        try:
            turma = int(input("Qual a turma (1, 2, 3)? "))
            if turma in [1, 2, 3]:
                break
            else:
                print("Digite uma turma entre (1, 2, 3)")
        except ValueError:
            print('Digite um numero valido!')


    if turma == 1:
        alunos_turma_1.append(aluno)
    elif turma == 2:
        alunos_turma_2.append(aluno)
    elif turma == 3:
        alunos_turma_3.append(aluno)
    else:
        print("Digite uma opção valida! Opções validas (1, 2, 3)")


    #Encerrar o programa
    while True:
        finalizar = input("Deseja cadastrar mais algum aluno? [s]im [n]ão ").strip().lower()
        if finalizar.startswith("s"):
            break
        elif finalizar.startswith("n"):
            sair = True
            break
        else:
            print("Digite uma opção válida: [s]im ou [n]ão.")
        
    if 'sair' in locals() and sair:
        break

mostrar_turma("Turma 1", alunos_turma_1)
mostrar_turma("Turma 2", alunos_turma_2)
mostrar_turma("Turma 3", alunos_turma_3)

analisar_turma("Turma 1", alunos_turma_1)
analisar_turma("Turma 2", alunos_turma_2)
analisar_turma("Turma 3", alunos_turma_3)
