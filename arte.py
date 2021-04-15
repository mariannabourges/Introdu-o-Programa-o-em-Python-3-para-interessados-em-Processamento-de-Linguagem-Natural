# Esse programa usa funções das bibliotecas random e matplotlib para produzir
# uma obra de arte aleatória. É um exemplo de como importar e utilizar funções
# de módulos externos.
# Importações:
from random import random as rand  # importação de função com apelido
import matplotlib.pyplot as plt  # importação de referência a um sub-módulo com apelido

# Instancia-se as listas x e y, inicialmente vazias, que comportarão as coordenadas
# vertical e horizontal dos pontos aleatorios gerados
x = []
y = []

# No loop, gera-se cinquanta pontos aleatórios, com coordenadas entre 0 e 1
cont = 0
while cont < 50:
    x.append(rand())
    y.append(rand())
    cont += 1

# plota-se os pontos e salva o resultado em disco:
plt.plot(x, y)
plt.savefig('arte.png')
