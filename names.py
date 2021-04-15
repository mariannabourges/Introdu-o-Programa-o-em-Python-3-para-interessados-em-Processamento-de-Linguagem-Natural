# Programa que implementa um classificador de nomes em inglês, segundo gênero, usando um modelo Naive Bayes
# e as ferramentas fornecidas pelo pacote nltk.
# (Baseado nos exemplos contidos em  https://www.nltk.org/book/
# # e http://www.nltk.org/howto/portuguese_en.html)
from nltk.corpus import names  # córpus de nomes em ingês do nltk
import nltk
import random

# Gera um córpus de classificação constituído por uma lista, em que cada entrada é uma tupla contendo um nome
# e seu respectivo gênero:
labeled_names = []
for name in names.words('male.txt'):  # nomes masculinos.
    labeled_names.append((name, 'male'))
for name in names.words('female.txt'):  # nomes femininos.
    labeled_names.append((name, 'female'))

random.shuffle(labeled_names)  # embaralhamos as entradas do córpus.


# Função auxiliar que recebe uma palavra e retorna um dicionário de features para representá-la.
# No nosso caso, esse dicionário contém uma única feature, a última letra do nome:
def gender_features(word):
    return {'last_letter': word[-1]}


# Geramos uma nova versão do córpus, substituindo os nomes por suas respectivas features:
feature_sets = []
for (name, gender) in labeled_names:
    feature_sets.append((gender_features(name), gender))

train_set, test_set = feature_sets[500:], feature_sets[:500]  # dividimos conjuntos de treinamento e testes.

classifier = nltk.NaiveBayesClassifier.train(train_set)  # treinamos um classificador Naive Bayes com os dados.

# Exemplos de uso:
print('Gênero previsto para Neo:', classifier.classify(gender_features('Neo')), '\n')
print('Gênero previsto para Trinity:', classifier.classify(gender_features('Trinity')), '\n')

# Exemplos de uso probabilístico:
print('Probabilidade do nome Neo ser de cada gênero:')
print('Masculino:', classifier.prob_classify(gender_features('Neo')).prob('male'))
print('Feminino:', classifier.prob_classify(gender_features('Neo')).prob('female'), '\n')

print('Features mais relevantes probabilisticamente para fins de classificação:')
print(classifier.most_informative_features(5), '\n')  # Recuperamos as features mais relevantes probabilisticamente
# para fins de classificação.

print('Acurácia do classificador gerado sobre o conjunto de testes:')
print(nltk.classify.accuracy(classifier, test_set))  # Calculamos a acurácia do classificador sobre o conjunto de testes
