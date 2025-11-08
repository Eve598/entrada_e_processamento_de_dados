from os import system
system('cls')

celsius = float(input("Temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f'Celsius: {celsius}°C\nFahrenheit: {fahrenheit} °F')