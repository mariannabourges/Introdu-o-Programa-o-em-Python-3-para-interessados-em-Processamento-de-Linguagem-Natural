# Programa que implementa a classe TokenList, uma classe que representa uma estrutura de dados
# para armazenar listas de tokens e marcações auxiliares, marcando a posição de sinais de
# pontuação e de palavras com o primeiro caractere capitalizado

class TokenList:
    # Método de construção, que recebe um texto e constrói a TokenList equivalente,
    # povoando as estruturas words, punctuation e upper devidamente.
    def __init__(self, text):
        self.words = []
        self.punctuation = []
        self.upper = []
        punctuation_list = ['.', ',', ':', ';', '!', '?']
        original_list = text.split()
        cont = 0

        while cont < len(original_list):

            if original_list[cont][-1] in punctuation_list:

                if original_list[cont][0].isupper():
                    self.upper.append(True)
                else:
                    self.upper.append(False)

                self.words.append(original_list[cont][:len(original_list[cont])-1].lower())
                self.punctuation.append(original_list[cont][-1])

            else:

                if original_list[cont][0].isupper():
                    self.upper.append(True)
                else:
                    self.upper.append(False)

                self.words.append(original_list[cont])
                self.punctuation.append('None')
            cont += 1

    # Método mágico de representação, que define como a função print deve tratar objetos dessa classe:
    def __repr__(self):
        return 'TokenList:'+str(self.words)+'/'+str(self.punctuation)+'/'+str(self.upper)

    # Método que reconstrói o texto original a partir da lista de palavra e das listas de marcações:
    def rebuild(self):
        text = ''
        cont = 0
        while cont < len(self.words):
            word = self.words[cont]
            if self.upper[cont]:
                word = word[0].upper() + word[1:]
            text = text + word
            if self.punctuation[cont] != 'None':
                text = text + self.punctuation[cont]
            text = text + ' '
            cont += 1
        return text


# Exemplos de uso:
a = TokenList('Oi, tudo bem?')
print(a)
print(a.words)
print(a.punctuation)
print(a.upper)
print(a.rebuild())
