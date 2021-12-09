'''
Programa que converte graus  Celsius em Fahrenheit através da fórmula:

C/5 = (F - 32)/9'''

C = -20
F = 9*C/5 + 32
print(f'{C}°C ---> {F}°F')
cont = 0
while cont <= 59:
    C += 1
    F = 9*C/5 + 32
    cont += 1
    
    print(f'{C}°C ---> {round(F,2)}°F')
