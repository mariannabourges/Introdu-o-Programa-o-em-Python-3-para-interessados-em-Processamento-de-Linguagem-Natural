# Programa que implementa uma função que calcula o fatorial de um numero inteiro
# de forma recursiva, ou seja, chamando a si mesma.
def fatorial(numero):
    # Condição de parada: fatorial(0) -> 1
    if numero == 0:
        return 1
    # Regra de recursão:
    else:
        return numero * fatorial(numero - 1)  # A função chama a si mesma


# Exemplo de uso:
print(fatorial(5))
