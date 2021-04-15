# Programa que implementa um classificador Naive Bayes, usando ferramentas do pacote nltk para diferenciar
# trechos textuais sobre aves e computadores.
from corpus import corpus  # importamos o córpus, como no Exercício 1
import nltk
import random
import tqdm

random.shuffle(corpus)  # Embaralhamos o córpus

# Separamos conjuntos de treinamento  e testes:
training_set = corpus[:int(len(corpus) * 0.9)]
test_set = corpus[int(len(corpus) * 0.9):]

token_list = []
stemmer = nltk.stem.RSLPStemmer()
stopwords = nltk.corpus.stopwords.words('portuguese') + ['.', ',', '!', '?', ':', ';', '(', ')', "``", "´´", '''"''', "''"]


# Função auxiliar que recebe um texto e devolve um dicionário de features para representá-lo, em que cada
# feature indica a presença de cada token do texto stemmizado, excluindo-se as stop words:
def feature_extractor(text):
    features_dict = {}
    tokens = nltk.word_tokenize(text, 'portuguese')
    for token in tokens:
        if token not in stopwords:
            features_dict[stemmer.stem(token.lower())] = True
    return features_dict


# Geramos um conjunto de treinamento e de testes, substituindo os textos por seus respectivos
# dicionários de features:
featuresets_train = [(feature_extractor(text), cls) for (text, cls) in training_set]
featuresets_test = [(feature_extractor(text), cls) for (text, cls) in test_set]

classifier = nltk.NaiveBayesClassifier.train(featuresets_train)  # treinamos um classificador.

print('Acurácia obtida sobre o conjunto de testes:')
print(nltk.classify.accuracy(classifier, featuresets_test), '\n')  # calculamos a acurácia do classificador

print('Dez features mais informativas sob o ponto de vista da classificação:')
print(classifier.most_informative_features(10), '\n')

# Exemplo de uso:
print('Exemplo de classificação:', classifier.classify(feature_extractor('A maioria dos pássaros voa.')))
