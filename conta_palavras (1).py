# Esse programa implementa uma função principal de contagem de palavras, que recebe um
# texto e retorna um dicionário cujas chaves são as palavras do texto e os valores
# são suas frequências de aparição, mas só para as palavras cuja frequência de apariç~ao
# está acima de um determinado limiar. Para ta, define-se duas funções auxiliares:
# uma para tokenizar o texto e uma para filtrar do dicionário  as palavras com
# frequencia abaixo do limiar.

# FUNÇÕES AUXILIARES:

# Função que tokeniza o texto, removendo sinais de pontuação:
def tokenize(texto):
    indesejados = ['.', ',', ';', ':', '!', '?']
    partes = texto.split()
    cont = 0
    while cont < len(partes):
        if partes[cont][-1] in indesejados:
            partes[cont] = partes[cont][0:len(partes[cont])-1]
        cont += 1
    return partes


# Função que recebe um dicionario com contagens de frequencias e uma frequencia minima
# e retorna uma nova versão do dicioário com todas as entradas com frequencia
# menor ou igual à mínima removidas:
def filtra_dicionario(freq, freq_min):
    freq_filtrado = {}  # Temos que criar um novo dicionario
    for key in freq:
        if freq[key] > freq_min:
            freq_filtrado[key] = freq[key]
    return freq_filtrado


# FUNÇÃO PRINCIPAL:
def conta_palavras(texto, freq_min):
    tokens = tokenize(texto)
    freq = {}
    for token in tokens:
        if token not in freq:
            freq[token] = 1
        else:
            freq[token] += 1
    return filtra_dicionario(freq, freq_min)


# EXEMPLO DE UTILIZAÇÃ DA FUNÇÃO PRINCIPAL:
print(conta_palavras('Os pássaros, pássaros no céu, não se se lembram do chão.', 1))
