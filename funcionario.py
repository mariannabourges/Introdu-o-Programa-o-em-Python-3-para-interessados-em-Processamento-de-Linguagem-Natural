# Programa exemplo de como criar uma classe filha de outra classe.
# Cria a classe  Funcionario e a classe-filha Voluntario, para modelar
# o pagamento de funcionarios de uma empresa
class Funcionario:
    # modela um Funcionario da empresa, permitindo criar, posteriormente, um objeto
    # para cada funcionario.
    assalariado = True  # o funionario generico eh tido como assalariado or padrao.
    empresa = 'Empresa: Serviços e Serviços.ltda'

    def __init__(self, nome, filial, departamento):
        self.nome = nome
        self.filial = filial
        self.departamento = departamento

    def pagamento(self):
        print('Pagamento realizado.')


class Voluntario(Funcionario):
    # Modela o funcionario voluntario. Eh uma classe filha da classe Funcionario
    # e, portanto, herda seus atributos e metodos, por padrao.
    assalariado = False  # sobrescreve o atributo assalariado, para que o voluntario seja tido como nao assalariado.

    def pagamento(self):
        # sobrescreve o metodo de pagamento da classe mae. Informa que pagamento nao eh aplicavel
        # a voluntario, caso ele realmente nao seja assalariado. Caso contrario, chama a versao
        # do metodo da classe mae.
        if not self.assalariado:
            print('Funcionário Voluntário. Não há pagamento a ser realizado.')
        else:
            super().pagamento()  # o comando super() serve para referir-se a classe mae de dentro da classe filha.


# Exemplos de uso:
f1 = Funcionario('Jorge da Silva', 25, 'Pesquisa e Desenvolvimento')
print(f1.nome)
print(f1.assalariado)
f1.pagamento()

f2 = Voluntario('Lúcia Silveira', 3, 'Contabilidade')
print(f2.nome)
print(f2.assalariado)
f2.pagamento()
f2.assalariado = True
print(f2.assalariado)
f2.pagamento()
f3 = Voluntario('Arnaldo Pinheiro', 10, 'Marketing')
print(f3.assalariado)
