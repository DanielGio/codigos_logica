# Questão (6) Produto em estoque

estoque = 15 
quantidade_solicitada = 10 

if quantidade_solicitada <= estoque:
    print("Pedido aprovado!")
else: print("Pedido Excede estoque!")

print("")

quantidade_solicitada = int(input("Digite a quantidade solicitada: "))

if quantidade_solicitada <= estoque:
    print("Pedido aprovado.")
else:
    print("Estoque insuficiente!")