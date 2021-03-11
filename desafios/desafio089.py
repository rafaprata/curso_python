#Variáveis
relacao = []
indice_aluno = 0
pesquisar = 0
soma = 0

#Cadastro
while True:
    #lista ALUNO
    relacao.append(list())
    relacao[indice_aluno].append(str(input('Nome: ')).upper())
    #lista NOTAS
    relacao[indice_aluno].append(list())
    for i in range(2):
        relacao[indice_aluno][1].append(float(input(f'{i+1}ª Nota: ')))
    ans = str(input('Quer continuar? [S/N] '))
    if ans in 'nN':
        break
    indice_aluno += 1

#Média
for aluno in relacao:
    for nota in aluno[1]:
        soma += nota
    aluno.append(soma/2)
    soma = 0

#Boletim
print('-='*30)
print(f'{"Relação de alunos":^60}')
print('-='*30)
for i, aluno in enumerate(relacao):
    print(f'[{i+1}]',f'{aluno[0]:<40}', f'{aluno[2]:>.2f}')

print('-='*30)

#Pesquisar
while pesquisar != 999:
    pesquisar = int(input('Digite o nº do aluno, para ver as notas obtidas: '))
    print(f'O aluno {pesquisar} é {relacao[pesquisar-1][0]}, obteve as seguintes notas:', end='')
    print(f'{relacao[pesquisar-1][1]}')
    print('-='*30)