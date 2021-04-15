# Programa que pede que o usuario insira uma senha e informa sobre a validade
# da senha, dadas as normas sintaticas pre-estabelecidas.

# Strings com tres aspas simples podem conter quebras de linha com o enter ao inves do \n
mensagem = '''Para ser considerada válida, sua senha deve seguir todas as seguintes diretrizes:
\t1. Deve conter ao menos um digito numerico;
\t2. Deve conter ao menos um caractere maiusculo;
\t3. Deve ter, no total, mais de oito caracteres.'''
print(mensagem)

senha = input('\nINSIRA SUA SENHA AQUI:')

# O valor-verdade de cada condicao eh computado separadamente:
cond1 = ('1' in senha or '2' in senha or '3' in senha or '4' in senha or '5' in senha or
         '6' in senha or '7' in senha or '8' in senha or '9' in senha or '0' in senha)
# Colocando a expressao logica entre parenteses voce pode fazer ela ocupar mais de uma linha
# sem que o python a interprete como comandos diferentes

cond2 = ('A' in senha or 'B' in senha or 'C' in senha or 'D' in senha or 'E' in senha or
         'F' in senha or 'G' in senha or 'H' in senha or 'I' in senha or 'J' in senha or
         'K' in senha or 'L' in senha or 'M' in senha or 'N' in senha or 'O' in senha or
         'P' in senha or 'Q' in senha or 'R' in senha or 'S' in senha or 'T' in senha or
         'U' in senha or 'V' in senha or 'X' in senha or 'W' in senha or 'Y' in senha or
         'Z' in senha)

cond3 = len(senha) >= 8

# Com as condicoes computadas e possivel verificar se a senha eh valida, verificando se todas as
# condicoes sao satisfeitas simultaneamente:
if cond1 and cond2 and cond3:
    print('\nSua senha é válida.')
else:
    print('\nSua senha não é válida.')