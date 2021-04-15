# Programa que pede as notas do aluno para as atividades do curso e calcula a media final
print('Calcularei sua nota final no curso.\n')
nota1 = float(input('Insira sua nota na primeira atividade:'))
nota2 = float(input('Insira sua nota na segunda atividade:'))
nota3 = float(input('Insira sua nota na terceira atividade:'))

media = (nota1 + nota2 + nota3)/3
print('\nSua nota final eh: ' + str(media))