
 
n = int(input('Digite um número: '))
total = 0 # Número de divisores
for c in range(1, n+1):
    if n % c == 0:
        print('', end='')
        total += 1
    else:
        print('', end='')
if total == 2: 
    print('É primo!')
else:
    print('Não é primo')