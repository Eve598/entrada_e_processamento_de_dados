#ENTRADA
a = float(input("digite o valor de a: "))
b = float(input("digite o valor de b: "))
c = float(input("digite o valor de c: "))

delta = b**2 - 4*a*c

#saida
print("o valor de delta é: ",delta)

if delta > 0:
    print("então a equação tem duas raizes reais")
elif delta == 0:
    print("então a equação tem uma raiz real")
else:
    print("então equação não possui raizes reais")