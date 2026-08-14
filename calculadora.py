############################################
#..............Calculadora.................#
############################################


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        print("Erro: impossível dividir por zero!")
        return None
    return a / b


def pegar_numero(mensagem):
    while True:
        valor = input(mensagem)
        try:
            return float(valor)
        except ValueError:
            print("Digite um número válido!")


while True:
    print("\n--- CALCULADORA ---")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Até mais!")
        break

    if opcao not in ("1", "2", "3", "4"):
        print("Opção inválida!")
        continue

    a = pegar_numero("Primeiro valor: ")
    b = pegar_numero("Segundo valor: ")

    if opcao == "1":
        resultado = somar(a, b)
    elif opcao == "2":
        resultado = subtrair(a, b)
    elif opcao == "3":
        resultado = multiplicar(a, b)
    elif opcao == "4":
        resultado = dividir(a, b)

    if resultado is not None:
        print("Resultado:", resultado)