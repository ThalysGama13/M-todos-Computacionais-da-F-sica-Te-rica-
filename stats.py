'''
Função que recebe uma lista e retorna os dados estatisticos:
- número de elementos
- maior valor
- menor valor
- soma dos valores
- média dos valores
- desvio padrão'''

def stats(valores = []):
    import numpy as np
    val = np.array(valores)
    num_elementos = len(val)
    maior = max(val)
    menor = min(val)
    soma = sum(val)
    media = soma/num_elementos
    desv_pad = np.std(val)

    print(f'''
    A quantidade de elementos é: {num_elementos}
    O maior valor da lista é: {maior}
    O menor valor da lista é: {menor}
    A soma dos valores da lista é: {soma}
    A média dos valores da lista é: {media}
    O desvio padrão dos valroes da lista é: {round(desv_pad,1)}''')


import numpy as np

valores = np.array([1,2,3,4,5,6])
stats(valores)
'''
output:
    A quantidade de elementos é: 6
    O maior valor da lista é: 6
    O menor valor da lista é: 1
    A soma dos valores da lista é: 21
    A média dos valores da lista é: 3.5
    O desvio padrão dos valroes da lista é: 1.7'''