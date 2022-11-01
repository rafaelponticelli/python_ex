# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
# A pergunta não espesifica condições.
# CRIANDO ESPECIFICAÇOES.
#1 - media 7.0.
#2 - 4 bimestres.
#3 - notas abaixo da media avera reprovação.
#4 - notas iguais ou acima da media avera a aprovaçao.
"""criar condiçao fixa para media e para quantidade de bimestres(4 bimestres).
logo depois pedir a media de cada bimestre. 
soma as medias e comparar com a soma da media 4 *.
e (print)da media (valor total de notas) e se ouve a APROVAÇÃO ou REPROVAÇÃO.
"""
#condiçao fixa
media = 4 * 7.0
#entrada de dados 
bimestre_1 = float(input("Digite a nota do primeiro bimestre :"))
bimestre_2 = float(input("Digite a nota do segundo bimestre :"))
bimestre_3 = float(input("Digite a nota do terceiro bimestre :"))
bimestre_4 = float(input("Digite a nota do quarto bimestre :"))
#calculo formula de soma
formula = bimestre_1 + bimestre_2 + bimestre_3 + bimestre_4
#condiçoes de fucionamento 
if formula  >= media :
    print("para bems VOÇE PASSOU sua media foi",formula)
elif formula <= media:
    print("que pena voçe REPROVOU sua media foi abaixo da media :",formula)  

