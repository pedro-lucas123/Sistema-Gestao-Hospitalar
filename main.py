
from collections import deque
import os

# ==================================================
# ESTRUTURAS DE DADOS
# ==================================================

# Lista: pacientes atualmente internados
pacientes = []

# Fila: pacientes aguardando atendimento (FIFO)
fila_triagem = deque()

# Pilha: historico de prontuarios acessados (LIFO)
historico_prontuarios = []

# Arvore: especialidades e diagnosticos
arvore_especialidades = {}


# ==================================================
# FUNCOES AUXILIARES
# ==================================================

ARQUIVO = "dados_sistema.txt"


def ler_texto(mensagem):
    """Solicita um texto obrigatorio ao usuario."""
    while True:
        valor = input(mensagem).strip()

        if valor and "|" not in valor and "\n" not in valor:
            return valor

        print("Digite um valor valido. O caractere | nao e permitido.")


def encontrar_por_id(lista, identificador):
    """Procura um registro pelo identificador."""
    for indice, registro in enumerate(lista):
        if registro["id"] == identificador:
            return indice, registro

    return None, None


# ==================================================
# LISTA - PACIENTES INTERNADOS
# ==================================================

def cadastrar_paciente():
    print("\n--- CADASTRAR PACIENTE ---")

    identificador = ler_texto("ID do paciente: ")

    if encontrar_por_id(pacientes, identificador)[1] is not None:
        print("Ja existe um paciente com esse ID.")
        return

    nome = ler_texto("Nome do paciente: ")
    leito = ler_texto("Leito: ")
    estado = ler_texto("Estado clinico: ")

    paciente = {
        "id": identificador,
        "nome": nome,
        "leito": leito,
        "estado": estado
    }

    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!")


def listar_pacientes():
    print("\n--- PACIENTES INTERNADOS ---")

    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    for indice, paciente in enumerate(pacientes):
        print(f"\nPosicao: {indice}")
        print(f"ID: {paciente['id']}")
        print(f"Nome: {paciente['nome']}")
        print(f"Leito: {paciente['leito']}")
        print(f"Estado: {paciente['estado']}")


def atualizar_paciente():
    print("\n--- ATUALIZAR PACIENTE ---")

    identificador = input("ID do paciente: ").strip()
    indice, paciente = encontrar_por_id(pacientes, identificador)

    if paciente is None:
        print("Paciente nao encontrado.")
        return

    print("Deixe vazio para manter o valor atual.")

    nome = input(f"Nome ({paciente['nome']}): ").strip()
    leito = input(f"Leito ({paciente['leito']}): ").strip()
    estado = input(f"Estado ({paciente['estado']}): ").strip()

    if nome and "|" not in nome:
        paciente["nome"] = nome

    if leito and "|" not in leito:
        paciente["leito"] = leito

    if estado and "|" not in estado:
        paciente["estado"] = estado

    print("Paciente atualizado com sucesso!")


def excluir_paciente():
    print("\n--- EXCLUIR PACIENTE ---")

    identificador = input("ID do paciente: ").strip()
    indice, paciente = encontrar_por_id(pacientes, identificador)

    if paciente is None:
        print("Paciente nao encontrado.")
        return

    pacientes.pop(indice)
    print("Paciente removido com sucesso!")


def menu_pacientes():
    while True:
        print("\n===== GERENCIAR PACIENTES =====")
        print("1 - Cadastrar paciente")
        print("2 - Listar pacientes")
        print("3 - Atualizar paciente")
        print("4 - Excluir paciente")
        print("0 - Voltar")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            cadastrar_paciente()
        elif opcao == "2":
            listar_pacientes()
        elif opcao == "3":
            atualizar_paciente()
        elif opcao == "4":
            excluir_paciente()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida.")


# ==================================================
# FILA - TRIAGEM (FIFO)
# ==================================================

def adicionar_fila():
    print("\n--- ADICIONAR A FILA DE TRIAGEM ---")

    identificador = ler_texto("ID do paciente: ")

    for registro in fila_triagem:
        if registro["id"] == identificador:
            print("Esse paciente ja esta na fila.")
            return

    nome = ler_texto("Nome do paciente: ")
    prioridade = ler_texto("Prioridade: ")

    registro = {
        "id": identificador,
        "nome": nome,
        "prioridade": prioridade
    }

    # Entra no final da fila
    fila_triagem.append(registro)

    print("Paciente adicionado ao final da fila!")


def listar_fila():
    print("\n--- FILA DE TRIAGEM ---")

    if not fila_triagem:
        print("Fila vazia.")
        return

    for posicao, registro in enumerate(fila_triagem, start=1):
        print(
            f"{posicao} - ID: {registro['id']} | "
            f"Nome: {registro['nome']} | "
            f"Prioridade: {registro['prioridade']}"
        )


def atender_fila():
    print("\n--- ATENDER PACIENTE ---")

    if not fila_triagem:
        print("Nao existem pacientes aguardando.")
        return

    # Remove o primeiro paciente da fila
    atendido = fila_triagem.popleft()

    print(f"Paciente atendido: {atendido['nome']}")
    print(f"ID: {atendido['id']}")


def atualizar_fila():
    print("\n--- ATUALIZAR PACIENTE DA FILA ---")

    identificador = input("ID do paciente: ").strip()

    for registro in fila_triagem:
        if registro["id"] == identificador:
            print("Deixe vazio para manter o valor atual.")

            nome = input(f"Nome ({registro['nome']}): ").strip()
            prioridade = input(
                f"Prioridade ({registro['prioridade']}): "
            ).strip()

            if nome and "|" not in nome:
                registro["nome"] = nome

            if prioridade and "|" not in prioridade:
                registro["prioridade"] = prioridade

            print("Registro atualizado!")
            return

    print("Paciente nao encontrado na fila.")


def menu_fila():
    while True:
        print("\n===== GERENCIAR FILA DE TRIAGEM =====")
        print("1 - Adicionar paciente")
        print("2 - Listar fila")
        print("3 - Atender proximo paciente")
        print("4 - Atualizar paciente na fila")
        print("0 - Voltar")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            adicionar_fila()
        elif opcao == "2":
            listar_fila()
        elif opcao == "3":
            atender_fila()
        elif opcao == "4":
            atualizar_fila()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida.")


# ==================================================
# PILHA - HISTORICO DE PRONTUARIOS (LIFO)
# ==================================================

def adicionar_prontuario():
    print("\n--- ADICIONAR PRONTUARIO AO HISTORICO ---")

    identificador = ler_texto("Codigo do prontuario: ")

    if encontrar_por_id(
        historico_prontuarios, identificador
    )[1] is not None:
        print("Esse prontuario ja esta no historico.")
        return

    paciente = ler_texto("Identificacao do paciente: ")
    descricao = ler_texto("Descricao do acesso: ")

    prontuario = {
        "id": identificador,
        "paciente": paciente,
        "descricao": descricao
    }

    # O novo registro entra no topo da pilha
    historico_prontuarios.append(prontuario)

    print("Prontuario adicionado ao historico!")


def listar_prontuarios():
    print("\n--- HISTORICO DE PRONTUARIOS ---")

    if not historico_prontuarios:
        print("Historico vazio.")
        return

    # Mostra primeiro o registro mais recente
    for registro in reversed(historico_prontuarios):
        print(
            f"Codigo: {registro['id']} | "
            f"Paciente: {registro['paciente']} | "
            f"Descricao: {registro['descricao']}"
        )


def remover_prontuario():
    print("\n--- REMOVER PRONTUARIO DO HISTORICO ---")

    if not historico_prontuarios:
        print("A pilha esta vazia.")
        return

    # Remove somente o elemento do topo
    removido = historico_prontuarios.pop()

    print(f"Prontuario removido: {removido['id']}")


def atualizar_prontuario():
    print("\n--- ATUALIZAR PRONTUARIO DO TOPO ---")

    if not historico_prontuarios:
        print("A pilha esta vazia.")
        return

    prontuario = historico_prontuarios[-1]

    print(f"Prontuario no topo: {prontuario['id']}")
    print("Deixe vazio para manter o valor atual.")

    paciente = input(
        f"Paciente ({prontuario['paciente']}): "
    ).strip()

    descricao = input(
        f"Descricao ({prontuario['descricao']}): "
    ).strip()

    if paciente and "|" not in paciente:
        prontuario["paciente"] = paciente

    if descricao and "|" not in descricao:
        prontuario["descricao"] = descricao

    print("Prontuario atualizado!")


def menu_pilha():
    while True:
        print("\n===== HISTORICO DE PRONTUARIOS =====")
        print("1 - Adicionar prontuario")
        print("2 - Listar historico")
        print("3 - Remover prontuario do topo")
        print("4 - Atualizar prontuario do topo")
        print("0 - Voltar")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            adicionar_prontuario()
        elif opcao == "2":
            listar_prontuarios()
        elif opcao == "3":
            remover_prontuario()
        elif opcao == "4":
            atualizar_prontuario()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida.")


# ==================================================
# ARVORE - ESPECIALIDADES E DIAGNOSTICOS
# ==================================================

def inserir_caminho(arvore, caminho):
    """Insere um caminho na arvore usando dicionarios aninhados."""
    atual = arvore

    for parte in caminho:
        if parte not in atual:
            atual[parte] = {}

        atual = atual[parte]


def adicionar_especialidade():
    print("\n--- ADICIONAR NA ARVORE ---")
    print("Digite os niveis separados por /")
    print("Exemplo: Clinica Geral/Cardiologia/Arritmia")

    entrada = ler_texto("Caminho: ")
    caminho = [parte.strip() for parte in entrada.split("/")]

    if any(not parte or "|" in parte for parte in caminho):
        print("Caminho invalido.")
        return

    inserir_caminho(arvore_especialidades, caminho)
    print("Caminho inserido na arvore!")


def exibir_arvore(no, nivel=0):
    """Percorre a arvore recursivamente."""
    for nome, filhos in no.items():
        print("  " * nivel + "- " + nome)
        exibir_arvore(filhos, nivel + 1)


def listar_arvore():
    print("\n--- ARVORE DE ESPECIALIDADES ---")

    if not arvore_especialidades:
        print("Arvore vazia.")
        return

    exibir_arvore(arvore_especialidades)


def buscar_caminho(arvore, caminho):
    atual = arvore

    for parte in caminho:
        if parte not in atual:
            return None

        atual = atual[parte]

    return atual


def consultar_arvore():
    print("\n--- CONSULTAR CAMINHO NA ARVORE ---")

    entrada = ler_texto("Caminho separado por /: ")
    caminho = [parte.strip() for parte in entrada.split("/")]

    resultado = buscar_caminho(arvore_especialidades, caminho)

    if resultado is None:
        print("Caminho nao encontrado.")
    else:
        print("Caminho encontrado!")
        if resultado:
            print("Elementos abaixo desse nivel:")
            exibir_arvore(resultado, len(caminho))
        else:
            print("Esse item nao possui subcategorias.")


def atualizar_arvore():
    print("\n--- RENOMEAR ITEM DA ARVORE ---")

    entrada = ler_texto("Caminho atual separado por /: ")
    caminho = [parte.strip() for parte in entrada.split("/")]

    if not caminho or any(not parte for parte in caminho):
        print("Caminho invalido.")
        return

    if len(caminho) == 1:
        pai = arvore_especialidades
    else:
        pai = buscar_caminho(
            arvore_especialidades, caminho[:-1]
        )

    if pai is None or caminho[-1] not in pai:
        print("Item nao encontrado.")
        return

    novo_nome = ler_texto("Novo nome: ")

    if novo_nome in pai:
        print("Ja existe um item com esse nome nesse nivel.")
        return

    # Mantem os filhos do item ao alterar seu nome
    pai[novo_nome] = pai.pop(caminho[-1])

    print("Item renomeado com sucesso!")


def excluir_arvore():
    print("\n--- EXCLUIR ITEM DA ARVORE ---")

    entrada = ler_texto("Caminho a excluir separado por /: ")
    caminho = [parte.strip() for parte in entrada.split("/")]

    if not caminho or any(not parte for parte in caminho):
        print("Caminho invalido.")
        return

    if len(caminho) == 1:
        pai = arvore_especialidades
    else:
        pai = buscar_caminho(
            arvore_especialidades, caminho[:-1]
        )

    if pai is None or caminho[-1] not in pai:
        print("Item nao encontrado.")
        return

    confirmacao = input(
        "Deseja excluir esse item e seus descendentes? (s/n): "
    ).strip().lower()

    if confirmacao == "s":
        del pai[caminho[-1]]
        print("Item excluido com sucesso.")
    else:
        print("Exclusao cancelada.")


def menu_arvore():
    while True:
        print("\n===== ARVORE DE ESPECIALIDADES =====")
        print("1 - Inserir especialidade ou diagnostico")
        print("2 - Listar arvore")
        print("3 - Consultar caminho")
        print("4 - Renomear item")
        print("5 - Excluir item e seus descendentes")
        print("0 - Voltar")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            adicionar_especialidade()
        elif opcao == "2":
            listar_arvore()
        elif opcao == "3":
            consultar_arvore()
        elif opcao == "4":
            atualizar_arvore()
        elif opcao == "5":
            excluir_arvore()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida.")


# ==================================================
# PERSISTENCIA - ARQUIVO TXT
# ==================================================

def salvar_dados():
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as arquivo:

            # Salva os pacientes
            for paciente in pacientes:
                arquivo.write(
                    f"LISTA|{paciente['id']}|{paciente['nome']}|"
                    f"{paciente['leito']}|{paciente['estado']}\n"
                )

            # Salva a fila na ordem de atendimento
            for registro in fila_triagem:
                arquivo.write(
                    f"FILA|{registro['id']}|{registro['nome']}|"
                    f"{registro['prioridade']}\n"
                )

            # Salva a pilha da base para o topo
            for registro in historico_prontuarios:
                arquivo.write(
                    f"PILHA|{registro['id']}|"
                    f"{registro['paciente']}|"
                    f"{registro['descricao']}\n"
                )

            # Salva todos os caminhos da arvore
            def salvar_nos(no, caminho_atual):
                for nome, filhos in no.items():
                    novo_caminho = caminho_atual + [nome]

                    arquivo.write(
                        "ARVORE|" + "|".join(novo_caminho) + "\n"
                    )

                    salvar_nos(filhos, novo_caminho)

            salvar_nos(arvore_especialidades, [])

        print("Dados salvos com sucesso!")

    except OSError as erro:
        print(f"Erro ao salvar os dados: {erro}")


def carregar_dados():
    global pacientes
    global fila_triagem
    global historico_prontuarios
    global arvore_especialidades

    if not os.path.exists(ARQUIVO):
        print("Arquivo de dados ainda nao existe.")
        return

    # Estruturas temporarias evitam perder os dados atuais
    # caso o arquivo apresente algum problema.
    novos_pacientes = []
    nova_fila = deque()
    nova_pilha = []
    nova_arvore = {}

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            for numero_linha, linha in enumerate(arquivo, start=1):
                linha = linha.rstrip("\n")

                if not linha:
                    continue

                partes = linha.split("|")
                tipo = partes[0]

                if tipo == "LISTA" and len(partes) == 5:
                    novos_pacientes.append({
                        "id": partes[1],
                        "nome": partes[2],
                        "leito": partes[3],
                        "estado": partes[4]
                    })

                elif tipo == "FILA" and len(partes) == 4:
                    nova_fila.append({
                        "id": partes[1],
                        "nome": partes[2],
                        "prioridade": partes[3]
                    })

                elif tipo == "PILHA" and len(partes) == 4:
                    nova_pilha.append({
                        "id": partes[1],
                        "paciente": partes[2],
                        "descricao": partes[3]
                    })

                elif tipo == "ARVORE" and len(partes) >= 2:
                    inserir_caminho(nova_arvore, partes[1:])

                else:
                    raise ValueError(
                        f"Formato invalido na linha {numero_linha}."
                    )

        # Substitui as estruturas somente depois da leitura completa
        pacientes = novos_pacientes
        fila_triagem = nova_fila
        historico_prontuarios = nova_pilha
        arvore_especialidades = nova_arvore

        print("Dados carregados com sucesso!")

    except (OSError, ValueError) as erro:
        print(f"Erro ao carregar os dados: {erro}")
        print("Os dados que estavam na memoria foram preservados.")


# ==================================================
# MENU PRINCIPAL
# ==================================================

def menu_principal():
    while True:
        print("\n========================================")
        print("       SISTEMA DE GESTAO HOSPITALAR")
        print("========================================")
        print("1 - Gerenciar pacientes internados")
        print("2 - Gerenciar fila de triagem")
        print("3 - Gerenciar historico de prontuarios")
        print("4 - Gerenciar arvore de especialidades")
        print("5 - Salvar dados")
        print("6 - Carregar dados")
        print("0 - Sair")
        print("========================================")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            menu_pacientes()
        elif opcao == "2":
            menu_fila()
        elif opcao == "3":
            menu_pilha()
        elif opcao == "4":
            menu_arvore()
        elif opcao == "5":
            salvar_dados()
        elif opcao == "6":
            carregar_dados()
        elif opcao == "0":
            print("Encerrando o sistema. Ate logo!")
            break
        else:
            print("Opcao invalida. Tente novamente.")


# ==================================================
# INICIO DO PROGRAMA
# ==================================================

if __name__ == "__main__":
    menu_principal()
