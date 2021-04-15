#ATIVIDADE 1
#NOMES COMPLETOS:
'''ENUNCIADO:
Nessa atividade, seu objetivo é construir um classificador binário de textos através
da seleção manual de features.
Você deve baixar o arquivo corpus.py do moodle e colocá-lo na mesma pasta que este
arquivo, então você deve preencher a parte indicada do código com a sua solução.
Dentro dessa area você pode usar a variavel corpus, que contem os dados que usaremos.
O corpus é uma lista de tuplas, em que cada tupla possui dois elementos. O primeiro
elemento é um trecho de texto extraído da wikipedia, o segundo é um indicador da classe
daquele texto. Se o indicador for 1, esse é um texto sobre computadores, se for 0, é
um texto sobre aves.
Seu código deve percorrer o córpus, gerando, para cada texto, uma lista de inteiros.
Cada elemento da lista deve indicar a frequencia de aparição de uma palavra pré-definida
naquele texto. Essas palavras são chamadas features de classificação e você deve
escolher quais serão, explicando seu criterio com comentarios, de forma resumida.
O programa deve, então, usar essa lista para definir a qual das duas classes o texto em questão
pertence e deve concatenar um índice correspondente à lista classes_previstas. O índice deve
ser 1 caso a classe prevista seja 'Computadores' e 0 caso seja 'Aves'.
Ao final da execução, o código usará todas as suas previsões para calcular a acurácia do seu
classificador!
Você deve submeter no moodle apenas esse arquivo, com as devidas modificações feita na parte
indicada.
ATENÇÃO: O SEU CÓDIGO DEVE GERAR UMA PREVISÃO PARA CADA TEXTO DO CÓRPUS, NEM MAIS NEM MENOS.
ATENÇÃO2: VOCÊ NÃO DEVE FAZER ATERAÇÕES FORA DA PARTE INDICADA PARA A SOLUÇÃO, A NÃO SER
QUE VOCÊ RECEBA AUTORIZAÇÃO EXPRESSA PARA TAL.

BOA SORTE C:
'''
from corpus import corpus
classes_corretas = [entrada[1] for entrada in corpus]
classes_previstas = []
# Aqui começa sua solução

#Aqui acaba sua solução
assert len(classes_previstas) == len(classes_corretas)
acuracia = sum([int(classes_previstas[i]==classes_corretas[i]) for i in range(len(classes_previstas))])/len(classes_previstas)
print('Acurácia obtida:', acuracia)
print('Ganho obtido:', acuracia - 0.5016181229773463)
