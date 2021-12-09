'''
programa que calcula a média ponderada lendo os números n1 e n2 pelo teclado
assim como seus pesos p1 e p2 respectivamente'''

def mediaPonderada(n1,n2,p1,p2):
    n1 = float(n1)
    n2 = float(n2)
    p1 = float(p1)
    p2 = float(p2)
    media = (p1*n1 + p2*n2)/(p1+p2)
    return media


n1 = float(input('Digite o 1° valor: '))
n2 = float(input('Digite o 2° valor: '))
p1 = float(input('Digite o 1° peso: '))
p2 = float(input('Digite o 2° peso: '))

print(f'A média ponderada é {round(mediaPonderada(n1,n2,p1,p2),2)}')

'''
output:
Digite o 1° valor: 6.5
Digite o 2° valor: 7.7
Digite o 1° peso: 0.4
Digite o 2° peso: 0.6
A média ponderada é 7.22
'''