# Questão (5)  Sistema de notas 

nota = float( input("Digite a nota: "))

if 9 <= nota <= 10:
    print("Excelente")
elif 7 <= nota < 9:
    print("Aprovado")
elif 5 <= nota < 7:
    print("Recuperação")
else:
    print("Reprovado")