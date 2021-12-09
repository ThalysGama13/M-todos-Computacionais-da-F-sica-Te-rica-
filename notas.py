import numpy as np

notas_turma = np.loadtxt('notas.dat')
notas = np.array(notas_turma)
passaram = []
reprovaram = []
#número de alunos na turma
print(len(notas))

#média da turma
media = sum(notas/len(notas))

print(f'A média da turma é {round(media,1)}')

#alunos que passaram e reprovaram direto
for i in notas:
    if i >= 7:
        passaram.append(i)
    if i < 3:
        reprovaram.append(i)
        
passou = len(passaram)/len(notas) * 100

reprovou = len(reprovaram)/len(notas) * 100

print(f'{round(passou,2)}% da turma foi aprovada e {round(reprovou,2)}% foi reprovada')

'''
output:
A quantidade de aluno é: 78
A média da turma é 5.1
17.95% da turma foi aprovada e 16.67% foi reprovada'''