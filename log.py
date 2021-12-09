'''
Programa que calcula o log de um número'''

def logaritmo(x):
    n = 5
    lg = 0
    for c in range (1,n+1):
        lg += 2*(1/(2*c - 1))*((x-1)/(x+1))**(2*c - 1)

    return lg

from math import log

x = 1.2

print(f'log: {logaritmo(x)}')

print(' ')
print(f'ln:  {log(x)}')

'''
output:
log: 0.18232155679331283
 
ln:  0.1823215567939546'''