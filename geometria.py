# Exemplo de orientacao a objetos e relacao de paternidade entre classes.
# Implementa: uma classe Ponto, que modela um ponto num espaco 2d;
# uma classe Quadrilatero, que modela um quadrilatero, num espaco 2d;
# uma classe Retangulo, filha de Quadrilatero, que modela um quadrilatero que tem dois pares
# de lados iguais entre si.

class Ponto:
    def __init__(self, x, y):
        # num espaco 2d, um ponto eh caracterizado por duas coordenadas:
        self.x = x
        self.y = y

    def __repr__(self):
        # metodo magico de representacao, define como um objeto da classe Ponto
        # sera interpretado pelo comando print().
        return '<' + str(self.x) + ', ' + str(self.y) + '>'


class Quadrilatero:
    # classe que implementa um quadrilatero no espaco 2d, caracterizado por 4 Pontos.
    num_lados = 4
    degenerado = False

    def __init__(self, p1, p2, p3, p4):
        # verifica se os argumentos de construcao sao do tipo correto. Senao, marca o quadrilatero como degenerado:
        if not (isinstance(p1, Ponto) and isinstance(p2, Ponto) and isinstance(p3, Ponto) and isinstance(p4, Ponto)):
            self.degenerado = True
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def __repr__(self):
        return '[' + self.p1.__repr__() + '|' + self.p2.__repr__() + '|' + self.p3.__repr__() + '|' + self.p4.__repr__() + ']'


class Retangulo(Quadrilatero):
    # classe retangulo, filha da classe Quadrilatero.
    def __init__(self, p1, p2):
        # sobrescreve o metodo de construcao, porque no caso do retangulo, apenas dois pontos sao necessarios.
        self.p1 = p1
        self.p2 = p2
        if isinstance(p1, Ponto) and isinstance(p2, Ponto):
            # cria os outros dois ponntos, em funcao dos fornecidos:
            self.p3 = Ponto(p1.x, p2.y)
            self.p4 = Ponto(p2.x, p1.y)
        else:
            self.degenerado = True

    def __repr__(self):
        # sobrescreve o metodo de representacao da classe-mae, para incluir retangulos degenerados:
        if self.degenerado:
            return 'DEGENERADO[' + str(self.p1) + '|' + str(self.p2) + ']'
        else:
            return super().__repr__()


# Exemplos de uso:

p1 = Ponto(1, 2)
p2 = Ponto(3, 4)
p3 = Ponto(5, 7)
p4 = Ponto(9, 3)
q = Quadrilatero(p1, p2, p3, p4)
print(q.degenerado)
r = Retangulo(p1, p2)
print(q)
print(r)
print(r.num_lados)
print(r.degenerado)
