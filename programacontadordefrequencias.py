# Programa que extrai as frequencias de aparicao das palavras em um texto,
# alocando-as em um dicionario.

texto = '''rosas são vermelhas
violetas são azuis
não são não
violetas são roxas'''

frequencias = {}  # Cria-se um dicionario vazio para poder ir adicionando as palavras e suas
# frequencias enquanto percorre-se o texto.

lista_de_palavras = texto.split()  # O metodo split eh um metodo de strings que retorna
# uma lista em que cada entrada corresponde a uma palavra contida na string.
# As palavras sao segmentadas usando os espacos e as quebras de linha.

# Percorre-se todas as palavras da lista de palavras usando um loop for:
for palavra in lista_de_palavras:
    # Se a palavra nao esta no dicionario eh porque essa eh a primeira vez que a encontramos
    # entao temos que adiciona-la no dicionario com frequencia 1, correspondente a essa vez:
    if palavra not in frequencias:
        frequencias[palavra] = 1
    # Caso contrario, ja vimos essa palava antes, entao basta incrementar sua frequencia:
    else:
        frequencias[palavra] = frequencias[palavra] + 1

print('O DICIONARIO DE FREQUENCIAS PRODUZIDO FOI:\n')
print(frequencias)