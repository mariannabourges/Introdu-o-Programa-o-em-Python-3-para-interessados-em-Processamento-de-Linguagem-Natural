# Programa que recebe do usuario cinco numeros interios e retorna o maior entre eles.
cont = 0
maximo = float('-inf')  # comecamos o maximo com o valor -infinito, um valor especial
# que, quando comparado com qualquer outro numero, eh tido como menor.
while cont < 5:
    numero = int(input('Insira um número inteiro:'))
    # se o numero fornecido eh maior que o maximo atual, ele eh tido como novo maximo:
    if numero > maximo:
        maximo = numero
    cont += 1
print('O maior numero fornecido foi: ', str(maximo))