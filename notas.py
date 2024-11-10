# Função para calcular a média das notas, com base na operação escolhida (somar ou dividir)
def calcular_media(notas, operacao):
    if operacao == 'soma':
        # Se o aluno escolher somar as notas, a função retorna a soma total das notas
        return sum(notas)
    elif operacao == 'dividir':
        # Se o aluno escolher dividir as notas, a função calcula a média dividindo a soma pelo número de notas
        return sum(notas) / len(notas)
    else:
        # Caso a operação seja inválida, o código avisa e retorna None
        print("Operação inválida!")
        return None

# Função principal que executa o programa
def calcular_resultado():
    print("Bem-vindo ao sistema de cálculo de notas!")
    
    # Pergunta ao aluno qual é a nota mínima para aprovação, reprovação e recuperação
    nota_aprovacao = float(input("Digite a nota mínima para aprovação: "))
    nota_reprovacao = float(input("Digite a nota mínima para reprovação: "))
    nota_recuperacao = float(input("Digite a nota mínima para recuperação: "))
    
    # Pergunta ao aluno se ele deseja somar ou dividir as notas para calcular a média
    operacao = input("Você deseja somar ou dividir as notas para calcular a média? (soma/dividir): ").strip().lower()
    
    # Pergunta ao aluno quantas notas ele tem
    num_notas = int(input("Quantas notas você tem? "))
    notas = []

    # Coleta todas as notas inseridas pelo aluno
    for i in range(num_notas):
        nota = float(input(f"Digite a {i+1}ª nota: "))
        notas.append(nota)
    
    # Chama a função para calcular a média das notas, passando a operação escolhida
    media = calcular_media(notas, operacao)
    
    if media is None:
        # Se a operação for inválida, encerra o programa
        return

    print(f"Sua média é: {media:.2f}")
    
    # Verifica a situação do aluno com base na média calculada
    if media >= nota_aprovacao:
        # Se a média for maior ou igual à nota de aprovação, o aluno foi aprovado
        print("Você foi aprovado!")
    elif media >= nota_recuperacao:
        # Se a média for maior ou igual à nota de recuperação, o aluno pode ser aprovado com a recuperação
        print("Você está de recuperação.")
        # Pergunta a nota de recuperação do aluno
        nota_recuperacao_aluno = float(input("Digite sua nota de recuperação: "))
        # Calcula a nova média após a recuperação
        media_recuperacao = (media + nota_recuperacao_aluno) / 2
        if media_recuperacao >= nota_aprovacao:
            # Se a média da recuperação for suficiente, o aluno foi aprovado
            print("Você foi aprovado após a recuperação!")
        else:
            # Se a média da recuperação não for suficiente, o aluno foi reprovado
            print("Você não passou nem na recuperação.")
    elif media < nota_reprovacao:
        # Se a média for menor que a nota de reprovação, o aluno foi reprovado
        print("Você foi reprovado.")
    else:
        # Caso o aluno não se encaixe em nenhuma das condições, algo deu errado
        print("Sua situação não foi definida corretamente.")

# Chama a função para executar o programa
calcular_resultado()