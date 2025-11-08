num1 = float(input("digite a base do triangulo: "))
num2 = float(input("digite a altura do triangulo: "))

area = (num1*num2)/2

if area >100:
    print("triangulo grande")

elif area >=100:
    print("triangulo medio")

else:
    print("triangulo pequeno")