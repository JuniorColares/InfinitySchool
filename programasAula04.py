#www.dontpad.com/219aula04

#IMPRIMIR DE ZERO A UM NÚMERO INFORMADO
'''
num = int(input('Escolha um número limite: '))
cont = 0

while cont <= num:
    print(cont)
    cont += 1
'''

'''
Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados os dados de idade, sexo (M/F) e salário. Faça um programa que calcule e mostre:

a. A média dos salários do grupo
b. A maior e a menor idade do grupo
c. A quantidade de mulheres na região
d. A idade e o sexo da pessoa que possui o menor salário

Finalize a entrada de dados ao ser digitada uma idade negativa
'''

'''
qm = 0
salarioTotal = 0
cont_pessoas = 0
idade = 0
menor_salario = 100000000
maior_idade = 0
menor_idade = 200

while True:
    idade = int(input('Informe a idade: '))
    if idade < 0:
        break
    elif idade < menor_idade:
        menor_idade = idade
    elif idade > maior_idade:
        maior_idade = idade
    salario = float(input('Digite o salário: '))
    salarioTotal = salarioTotal + salario
    sexo = input('Informe o sexo (m/f): ')
    if sexo == 'f':
        qm += 1
    if salario < menor_salario:
        menor_salario = salario
        sexo_menor = sexo
        idade_menor = idade
    cont_pessoas += 1
print(f'A média dos salários do grupo vale R${salarioTotal/cont_pessoas:.2f}')
print(f'A maior idade é {maior_idade} e a menor é {menor_idade}')
print(f'O número de mulheres na região é {qm}')
print(f'A pessoa que possui o menor salário é do sexo {sexo_menor} e tem {idade_menor} anos')
'''

'''
TENTATIVA FORCA

palavra_secreta = input('Digite a palavra a ser adivinhada: ')
palavra = ""
palavra_jogo = ""
cont = 0
for i in palavra_secreta:
    palavra = palavra + "_ "

print(palavra)

while cont <= 10:
    letra = input('Escolha uma letra: ')
    for i in palavra_secreta:
        if i == letra:
            palavra = palavra + letra

    print(palavra)
'''

'''
qnt = int(input("Quantas notas deseja digitar? "))
soma = 0

for i in range(1,(qnt+1)):
    nota = float(input(f'Digite a {i}ª nota: '))
    soma = soma + nota

print(f'A média final é {soma/qnt:.2f}')
'''

#PORCENTAGEM DE SINTOMAS

totalL = 0
totalG = 0
totalA = 0

for i in range(10):
    sintoma = input(f'O paciente {i+1} se encontra com sintomas leves (l), graves (g) ou é assintomático (a)? ')
    if sintoma == 'l':
        totalL += 1
    elif sintoma == 'g':
        totalG += 1
    elif sintoma == 'a':
        totalA += 1
    else:
        print('Informação inválida!')

print(f"\nPacientes com sintomas\nGraves: {100*totalG/10:.2f}%\nLeves: {100*totalL/10:.2f}%\nAssintomáticos: {100*totalA/10:.2f}%.")


#QUANTIDADE DE VOGAIS

palavra = input("Escolha uma palavra para contar as vogais: ")
contador = 0

for i in palavra:
    if i == "a" or i == "e" or i == "i" or i == "o" or i =="u":
        contador += 1

print(f'A palavra escolhida possui {contador} vogais.')












