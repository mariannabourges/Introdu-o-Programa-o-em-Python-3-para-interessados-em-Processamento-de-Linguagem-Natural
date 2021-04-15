# Programa que produz um córpus como o da atividade prática, a partir de arquivos
# de texto separados que contenham as sentenças de cada classe, salvando
# o córpus resultante num arquivo serializado, usando o módulo pickle.
import pickle  # importa-se a referência ao módulo


# Define-se uma função auxiliarq que faz aasição da frase ao córpus com as devidas
# correções:
def add_corpus(frase, corpus, classe):
    if frase != '':
        if frase[0] == ' ':
            corpus.append((frase[1:], classe))
        else:
            corpus.append((frase, classe))
    return corpus


# Abre-se e extrai o conteúdo bruto dos dois arquivos:
with open('aves.txt', 'r') as leitor_aves:
    texto_aves = leitor_aves.read()
with open('computadores.txt', 'r') as leitor_computadores:
    texto_computadores = leitor_computadores.read()

# Separa-se o conteúdo em frases:
frases_aves = texto_aves.split('.')
frases_computadores = texto_computadores.split('.')
corpus = []

# Usando a função auxiliar, adiciona-se as frases a córpus:
for frase in frases_aves:
    corpus = add_corpus(frase, corpus, 0)

for frase in frases_computadores:
    corpus = add_corpus(frase, corpus, 1)

# Salva-se o córpus em disco, usando o módulo pickle:
with open('corpus.pkl', 'wb') as f:
    pickle.dump(corpus, f)
