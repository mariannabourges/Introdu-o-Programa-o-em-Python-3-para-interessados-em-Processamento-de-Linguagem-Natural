# Programa que cria uma classe de bichinhos virtuais
class BichinhoVirtual:
    # Com o método mágico de construção, definimos quais os argumentos de construção para
    # cada objeto desta classe:
    def __init__(self, nome, especie, idade, tamanho):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.tamanho = tamanho
        return

    # Com o método mágico de representação, definimos como a função print deve tratar
    # objetos dessa classe:
    def __repr__(self):
        return ':)-' + self.tamanho * '*'

    # Com o método mágico de tamanho, definimos como a função len deve tratar obetos dessa classe:
    def __len__(self):
        return self.tamanho

    # Definimos o método brotar, que cria um novo bichinho virtual (objeto), removendo, para tal,
    # uma unidade de tamanho do objeto atual:
    def brotar(self):
        self.tamanho -= 1
        broto = BichinhoVirtual('', self.especie, 0, 1)
        return broto


# Exemplos de uso:
l = BichinhoVirtual('lucio', 'blob', 5, 10)
j = BichinhoVirtual('jorgina', 'blub', 3, 20)
print('Este é', l.nome, '\nEle é um', l.especie, 'de', l.idade, 'anos de idade:')
print(l)

print('Esta é', j.nome, '\nEla é um', j.especie, 'de', j.idade, 'anos de idade:')
print(j)

l_jr = l.brotar()
l_jr.nome = 'lucio junior'
print('Este é', l_jr.nome, '\nEle é um', l_jr.especie, 'de', l_jr.idade, 'anos de idade:')
print(l_jr)
