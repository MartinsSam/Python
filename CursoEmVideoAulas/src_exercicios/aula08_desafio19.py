import random
alunos = {}
alunoTemp = input('Primeiro aluno:')
alunos = alunoTemp

alunoTemp = input('Segundo aluno:')
alunos = [alunos, alunoTemp]

alunoTemp = input('Terceiro aluno:')
alunos.append(alunoTemp)

alunoTemp = input('Quarto aluno:')
alunos.append(alunoTemp)

alunoTemp = random.choice(alunos)
print('O aluno escolhido foi: {}'.format(alunoTemp))
