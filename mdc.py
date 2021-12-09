a = int(input('Digite um número inteiro positivo: '))
b = int(input('Digite outro número inteiro positivo: '))
d = 1
divisores = []

while a > d:
    d += 1
    if a % d == 0 and b % d == 0:
        divisores.append(d)
    
print(f'O MDC de {a} e {b} é {max(divisores)}')