# Programa que pede as notas do aluno nas atividades do curso, sua frequencia e
# retorna se ele foi aprovado ou reprovado, alem do motivo da reprovacao.
print('Obterei seu resultado final no curso.\n')
nota1 = float(input('Insira sua nota na primeira atividade:'))
nota2 = float(input('Insira sua nota na segunda atividade:'))
nota3 = float(input('Insira sua nota na terceira atividade:'))
frequencia = float(input('Insira sua frequencia no curso (em porcentagem):'))

media = (nota1 + nota2 + nota3)/3
print('\nSua nota final eh: ' + str(media))

if media >= 5.0 and frequencia >= 80:
    print('Você foi aprovado!')
elif media < 5 and frequencia < 80:
    print('Você foi reprovado por nota e frequencia.')
elif media < 5:
    print('Você foi reprovado por nota.')
else:
    print('Você foi reprovado por frequencia.')