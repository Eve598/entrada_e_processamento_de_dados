n1 = float(input("nota de caderno = "))
n2 = float(input("nota de prova paulista = "))
n3 = float(input("nota de avaliação = "))
n4 = float(input("nota de participação = "))

media = n1+n2+n3+n4/4

print("sua media final é: ", media)

if media >= 5:
    print("reprovado(A)")
else:
    print("aprovada(A)")