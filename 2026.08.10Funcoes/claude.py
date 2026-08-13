############################################
# 2026.08.10.Funcoes\agenda_furreca.py     #
# AGENDA FURRECA.PY                        #
# Versão 2026.08.12 - Interface melhorada  #
# By Luferat - https://github.xonm/Luferat #
############################################

# Importa "subprocess" e "os" que permitem executar comandos do sistema
import subprocess
import os

# Importa "random" para gerar números aleatórios
import random

# Banco de dados em memória (dict) (Mock)
database = {
    "1": {"name": "Joca da Silva", "contact": "(21) 998877665", "status": "ON"},
    "120": {"name": "Mariana Sirilampo", "contact": "mariana@sirilampo.com.br", "status": "ON"}
}


# ------------------------------------------------------------------
# NOVO: cores ANSI para deixar a interface mais clara
# ------------------------------------------------------------------
class Cor:
    VERDE = "\033[92m"
    VERMELHO = "\033[91m"
    AMARELO = "\033[93m"
    AZUL = "\033[94m"
    CIANO = "\033[96m"
    RESET = "\033[0m"
    NEGRITO = "\033[1m"


def cls():
    # Limpa a tela
    if os.name == "nt":
        # Se o sistema é Windows
        subprocess.run("cls", shell=True)
    else:
        # Outros sistemas como Linux e MacOS
        subprocess.run("clear", shell=True)


# ------------------------------------------------------------------
# NOVO: cabeçalho padronizado com borda, usado em todas as telas
# ------------------------------------------------------------------
def header(titulo, largura=50):
    print(Cor.CIANO + "╔" + "═" * (largura - 2) + "╗")
    print("║" + titulo.center(largura - 2) + "║")
    print("╚" + "═" * (largura - 2) + "╝" + Cor.RESET)


# ------------------------------------------------------------------
# NOVO: helpers de mensagem coloridos (erro/sucesso), sem mudar
# nenhuma regra de validação já existente
# ------------------------------------------------------------------
def msg_erro(texto):
    print(f"{Cor.VERMELHO}----- {texto} -----{Cor.RESET}")


def msg_sucesso(texto):
    print(f"{Cor.VERDE}{texto}{Cor.RESET}")


def prompt(texto):
    return input(f"{Cor.AMARELO}» {Cor.RESET}{texto}")


def new_contact():
    # Cadastra novo contato
    cls()
    header("AGENDA FURRECA - NOVO CONTATO")
    print("\nDigite os dados do contato:\n")

    # Recebe e valida o "name"
    while True:
        name = prompt(" • Nome: ")
        if name.strip() != "":
            break
        msg_erro("Digite um nome válido!")

    # Recebe e valida o "contact"
    while True:
        contact = prompt(" • Contato: ")
        if contact.strip() != "":
            break
        msg_erro("Digite um contato válido!")

    # Gera o ID aleatório e não repetido
    while True:
        key = str(random.randint(1, 1000))
        if key not in database:
            break

    # Salva o novo cadastro (mantendo o campo "status", que existia
    # no banco original mas não estava sendo salvo aqui)
    database[key] = dict(name=name, contact=contact, status="ON")

    print()
    msg_sucesso(f"Usuário com ID {key} adicionado!")
    input("Tecle [Enter] para continuar")

    main()


def list_contacts():
    # Lista todos os registros em formato de tabela
    cls()
    header("AGENDA FURRECA - LISTA DE CONTATOS")
    print()
    print(f"{Cor.NEGRITO}{len(database)} usuário(s) encontrado(s){Cor.RESET}")
    print()

    # Cabeçalho da tabela
    print(f"{Cor.NEGRITO}{'ID':<6}{'Nome':<25}{'Contato':<25}{'Status':<8}{Cor.RESET}")
    print("-" * 64)

    # Loop para iterar os registros usando o método `dict.items()`
    for key, value in database.items():
        status = value.get("status", "-")
        cor_status = Cor.VERDE if status == "ON" else Cor.VERMELHO
        print(f"{key:<6}{value['name']:<25}{value['contact']:<25}{cor_status}{status:<8}{Cor.RESET}")

    print()
    input("Tecle [Enter] para continuar")
    main()


def edit_contact():
    cls()
    header("AGENDA FURRECA - EDITA CONTATO")

    print()
    while True:
        key = prompt("Digite o ID do usuário: ")
        if key in database:
            break
        msg_erro("ID não encontrado!")

    print()
    print("ID:", key)
    print(" • Nome:", database[key]['name'])
    print(" • Contato:", database[key]['contact'])
    print(" • Status:", database[key].get('status', '-'))
    print()

    print("Digite os novos dados:")

    # Recebe e valida o "name"
    while True:
        name = prompt(" • Nome: ")
        if name.strip() != "":
            break
        msg_erro("Digite um nome válido!")

    # Recebe e valida o "contact"
    while True:
        contact = prompt(" • Contato: ")
        if contact.strip() != "":
            break
        msg_erro("Digite um contato válido!")

    # Atualiza mantendo o "status" que o contato já tinha
    status_atual = database[key].get("status", "ON")
    database[key] = dict(name=name, contact=contact, status=status_atual)

    print()
    msg_sucesso("Contato atualizado!")
    input("Tecle [Enter] para continuar")
    main()


def delete_contact():
    cls()
    header("AGENDA FURRECA - APAGA CONTATO")

    print()
    while True:
        key = prompt("Digite o ID do usuário: ")
        if key in database:
            break
        msg_erro("ID não encontrado!")

    print()
    print("ID:", key)
    print(" • Nome:", database[key]['name'])
    print(" • Contato:", database[key]['contact'])
    print()

    option = prompt(f"{Cor.VERMELHO}Tem certeza que deseja apagar [S/N]? {Cor.RESET}")
    if option.upper() == "S":
        del database[key]
        msg_sucesso("Contato apagado!")
    else:
        print()
        print("Não aconteceu nada!")

    input("Tecle [Enter] para continuar")
    main()


def main(error=str()):
    # Programa principal e "main loop"
    while True:
        # Limpa a tela
        cls()

        # Cabeçalho
        header("AGENDA FURRECA - MENU PRINCIPAL")

        # Exibe menu principal
        print(f'''
{Cor.NEGRITO}Opções:{Cor.RESET}

1 - Novo contato
2 - Listar contatos
3 - Editar contato
4 - Apagar contato
0 - Sair do programa
    ''')

        # Exibe mensagem de erro se existir
        if error:
            msg_erro(error)

        # Recebe opção do usuário
        opcao = prompt("Escolha uma opção: ")

        # Executa a opção selecionada
        match opcao:
            case "1":
                new_contact()
            case "2":
                list_contacts()
            case "3":
                edit_contact()
            case "4":
                delete_contact()
            case "0":
                # Limpa a tela, exibe confirmação e termina o programa
                cls()
                print(f"\n{Cor.CIANO}Acabou!{Cor.RESET}")
                exit()
            case _:
                # Se escolheu uma opção inválida, chama o menu novamente, mas, com a mensagem de erro.
                error = "Digite uma opção válida!"
                main(error)


# "Roda" o programa
main()