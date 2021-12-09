'''
programa que mostra os 100 primeiros termos da sequẽncia de Fibonacci'''

n = 100
c = 0

t1 = 0
t2 = 1
print(f'{t1}, {t2}, ', end='')
while c <= n:
    t3 = t1 + t2 #
    t1 = t2
    t2 = t3
    c += 1
    print(f'{t3}, ', end='')

