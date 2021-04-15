# Programa que implementa uma função simples de tokenização, que remove sinais de pontuação
# do fina das palavras

def tokenize(texto):
    indesejados = ['.', ',', ';', ':', '!', '?']
    partes = texto.split()
    cont = 0
    while cont < len(partes):
        if partes[cont][-1] in indesejados:
            partes[cont] = partes[cont][0:len(partes[cont])-1]
        cont += 1
    return partes


# Exemplo da aplicação da função:
print(tokenize('Oi! Tudo be com você? Comigo também.'))
