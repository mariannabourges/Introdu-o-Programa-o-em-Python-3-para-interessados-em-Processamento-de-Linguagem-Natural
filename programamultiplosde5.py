# Programa que usa o comando continue para imprimir todos os numeros
# entre 0 e 100 (inclusos) que sao multiplos de 5.
cont = -1
while cont <= 100:
    cont += 1
    if cont % 5 != 0:
        continue
    print(cont)