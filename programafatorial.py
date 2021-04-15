# Programa que recebe um numero inteiro do usuario e devolve seu fatorial

# O primeiro loop garante que o usuario forneca um numero inteiro POSITIVO
while True:
    numero = int(input('Insira um numero inteiro positivo:'))
    if numero >= 0:
        break

# O segundo loop calcula o fatorial do numero iterativamente
fatorial = 1
while numero > 0:
    fatorial = fatorial * numero
    numero -= 1

print('O fatorial do numero fornecido eh', fatorial)