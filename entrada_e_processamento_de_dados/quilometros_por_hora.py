
num1 = float(input("digite a distancia percorrida: km "))
num2 = float(input("digite o tempo gasto: "))


velocidade = num1/num2
print("velocidade media km/h",velocidade)
if velocidade >=100:
    print("transito livre")


elif velocidade >=60:
    print("transito moderado")

else:
    print("transito lento")