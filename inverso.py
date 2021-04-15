# Program que implementa uma função que gera a contraparte invertida de um numero inteiro:
def inverso(numero):
    # Como strings podem ser invertidas, convertemos o numero de entrada
    # para uma string, invertemos seus caracteres e depois o convertemos de
    # vota, para então, retorná-lo.
    numero_str = str(numero)
    inverso_str = numero_str[::-1]
    inverso = int(inverso_str)
    return inverso


# Exemplo de uso da função:
print(inverso(344)+1)
