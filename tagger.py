# Programa que implementa e compara diferentes analisadores sintáticos automáticos (taggers) para a
# língua portuguesa, usando as ferramentas disponibilizadas pelo pacote NLTK e os dados do córpus
# Floresta Sintactica, para treinamento.
# (Baseado nos exemplos contidos em  https://www.nltk.org/book/
# # e http://www.nltk.org/howto/portuguese_en.html)
import nltk
from nltk.corpus import floresta
from tqdm import tqdm  # importamos o tqdm para gerar barras de progresso facilmente.


# Função auxiliar que realiza a extração da classe sintática de uma palavra da tag (ou anotação) para aquela
# palavra no córpus, removendo as partes da tag que não são relevantes neste contexto:
def extract_pos(tag):
    if '+' in tag:
        return tag.split('+')[1]
    else:
        return tag


sentences = floresta.tagged_sents()  # lista de sentenças taggeadas originais do córpus.

# Preenchemos a lista tagged_sentences com os dados do córpus com as tags já filtradas, correspondentes às
# classes gramaticais:
tagged_sentences = []
print('Extraindo classes gramaticais das tags do córpus:')
for sent in tqdm(sentences):
    tagged_sent = []
    for (word, tag) in sent:
        tagged_sent.append((word.lower(), extract_pos(tag)))
    tagged_sentences.append(tagged_sent)

# Dividimos o córpus em um conjunto de treinamento e umm conjunto de testes:
train = tagged_sentences[100:]
test = tagged_sentences[:100]

# Escolhemos como Baseline um tagger que chuta sempre a mesma classe para toda palavra, a classe gramatical mais
# frequente no córpus: 'n', correspondente à NOME:
baseline = nltk.DefaultTagger('n')
print('Baseline accuracy:', baseline.evaluate(test))

# Treinamos um tagger de Unigramas usando o baseline como backoff:
tagger1 = nltk.UnigramTagger(train, backoff=baseline)
print('Unigram Tagger accuracy:', tagger1.evaluate(test))

# Em seguida, treinamos um tagger de Bigramas, usando o tagger de unigramas como backoff:
tagger2 = nltk.BigramTagger(train, backoff=tagger1)
print('Bigram Tagger accuracy', tagger2.evaluate(test))

# Exemplo de classificação sintática de uma sentença tokenizada, usando nosso melhor tagger:
print(tagger2.tag(['o', 'pássaro', 'segue', 'feliz', '.']))
