# Programa que calcula quantos anos demora para que a populacao de um pais
# ultrapasse a de outro.
# CUIDADO! ESSE PROGRAMA PODE ENTRAR EM LOOP INFINITO DEPENDENDO DOS PARAMETROS
pop0_narnia = float(input('Insira a população de Narnia hoje:'))
pop0_usp = float(input('Insira a população de Usplândia hoje:'))
taxa_narnia = float(input('Insira a taxa de crescimento população de Narnia:'))/100
taxa_usp = float(input('Insira a taxa de crescimento população de Usplandia:'))/100

# O loop simula o crescimento da populacao dos dois paises ao longo do ano e
# quando a populacao do primeiro ultrapassa a do segundo, o loop e interrompido
# e o ano eh retornado.
ano = 0
while pop0_usp < pop0_narnia:
    pop0_usp = pop0_usp + pop0_usp * taxa_usp
    pop0_narnia = pop0_narnia + pop0_narnia * taxa_narnia
    ano += 1

print('Foram necessarios', ano, 'anos.')