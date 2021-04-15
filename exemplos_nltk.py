# Programa que fornece uma série de exemplos básicos de como usar ferramentas do pacote nltk
# para realizar processamento de linguagem natural, com foco especial para tarefas de pré-processamento
# e ferramentas de visualização.
# (Muitos desses exemplos foram baseados naqueles contidos em https://www.nltk.org/book/
# e http://www.nltk.org/howto/portuguese_en.html)
import nltk
from nltk.corpus import floresta  # importamos o corpus em portugues Flotesta Sintactica, que usaremos
# em alguns exemplos.

# EXEMPLOS DE TOKENIZAÇÃO SIMPLES COM O NLTK:
# Exemplo em português
texto_pt = 'Um pássaro, enquanto voa, não se lembra do chão, me disse Dr. Arnaldo'
tokens_pt = nltk.word_tokenize(texto_pt, 'portuguese')
print('Tokenização em potuguês:', tokens_pt, '\n')

texto_en = "It's ok Luke. We will be all right"
tokens_en = nltk.word_tokenize(texto_en, 'english')
print('Tokenização em inglês:', tokens_en, '\n')

# COMO USAR AS LISTAS DE STOP WORDS NO NLTK:
# Exemplo em português:
stopwords_pt = nltk.corpus.stopwords.words('portuguese')
print('Stop words em português:', stopwords_pt, '\n')

# Exemplo em Norueguês:
stopwords_no = nltk.corpus.stopwords.words('norwegian')
print('Stop words em norueguês:', stopwords_no, '\n')

# Exemplo de remoção de Stop words em Português com um loop simples:
texto_tok = nltk.word_tokenize('De lá até aqui encontrei muita gente'.lower(), 'portuguese')  # ajustamos a
# capitalização do texto, porque a lista de stop words fornecida está sempre em letras minuúsculas.
texto_tok_nosw = []
for token in texto_tok:
    if token not in stopwords_pt:
        texto_tok_nosw.append(token)

print('Lista de tokens com stop words removidas:', texto_tok_nosw)
#
# COMO REALIZAR STEMIZAÇAO USANDO O NLTK:
stemmer = nltk.stem.RSLPStemmer()  # importamos um stemmer para lingua portuguesa.
print(stemmer.stem('amor'))
print(stemmer.stem('amar'))
print(stemmer.stem('amaria'), '\n')

# REALIZANDO CONTAGEM DE FREQUENCIAS COM O NLTK:
fd = nltk.FreqDist(floresta.words())  # floresta.words() retorna a lista de palavras que compõe o córpus.
print('Objeto FrequencyDist construído:', fd, '\n')
print('Dez palavras mais comuns no córpus:', fd.most_common(10), '\n')
print('Número total de palavras no córpus:', fd.N(), '\n')
print('Número de tipos do córpus, ou número total de palavras no seu vocabulário:', len(fd), '\n')
fd.plot(50)  # gera um plot da distribuiçãonde frequência das 50 palavras mais comuns no córpus.
#
# EXEMPLO DE USO DA CLASSE TEXT, DISPONIBILIZADA NO NLTK:
text = nltk.Text(floresta.words())
print('Objeto Text criado:', text, '\n')

print("Busca de ocorrências pala palavra 'lugar' no córpus:")
text.concordance('lugar')
print()

print("Contextos mais comuns para a palavra 'lugar' no córpus:")
text.common_contexts(['lugar'])
print()

# Faz um plot de dispersão, que permite visualizar os pontos de aparição da lista de palavras dadas como argumento
# ao longo do córpus de forma comparativa:
text.dispersion_plot(['Portugal', 'Brasil', 'Amazônia', 'Lisboa', 'correto', 'correcto'])
