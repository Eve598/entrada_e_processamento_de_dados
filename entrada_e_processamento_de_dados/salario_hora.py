def calcular_salario(valor_hora, horas_trabalhadas):
    limite_horas = 40
    if horas_trabalhadas > limite_horas:
        horas_extras = horas_trabalhadas - limite_horas
        salario_base = limite_horas * valor_hora
        adicional = horas_extras * valor_hora * 1.5
        salario_total = salario_base + adicional
    else:
        salario_total = horas_trabalhadas * valor_hora
    return salario_total

valor_hora = float(input("Digite o valor da sua hora de trabalho: R$ "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario = calcular_salario(valor_hora, horas_trabalhadas)

print(f"\nSeu salário total é: R$ {salario:.2f}")

