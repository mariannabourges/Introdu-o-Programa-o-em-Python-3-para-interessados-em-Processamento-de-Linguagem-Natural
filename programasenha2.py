# Programa que pede ao usuario um nome de usuario e senha um numero arbitrario
# de vezes ateh que a senha seja diferente do nome de usuario fornecido.
while True:
    usuario = input('INSIRA SEU NOME DE USUARIO:')
    senha = input('INSIRA SUA SENHA:')
    if usuario != senha:
        break
    print('\nSENHA E USUARIO INVALIDOS.\n')