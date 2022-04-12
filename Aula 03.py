'''
CONVERTER M PARA CM

cm = float(input('Informe o valor em metros a ser convertido para centímetros: '))
mt = cm * 100
print('O valor em centímetros vale', mt,'cm')
'''
import random
from os import write

'''
CALCULAR AREA A PARTIR DO RAIO

raio = float(input('\nInforme o valor do raio do círculo: '))
area = 3.14 * (raio**2)
print('A área do círculo vale',area,'m²')
'''

'''
TRANSFORMAR TF PARA TC E APRESENTAR FAIXA DE CALOR

#print(f"A temperatura em Celcius é {TC}")
TF = float(input("Digite a temperatura em Fahrenheit: "))
TC = round((((TF-32)*5)/9),2)

if TC > 38:
    print(f'PEGANDO FOGO: {TC}ºC')
elif 38 >= TC >= 30:
    print(f'Quente: {TC}ºC')
elif 30 > TC > 20:
    print(f'Temperatura normal: {TC}ºC')
elif TC <= 20:
    print(f'Muito frio: {TC}ºC')
'''

'''
PRINTAR DE 0 A 50

i = 0
while i<= 50:
    print(i)
    i += 1
'''

'''
IMPRIMIR TODOS OS NÚMEROS ATÉ 100 A PARTIR DE UMA ENTRADA

i = int(input('Digite um número menor que 100: '))

if i > 100:
    i = int(input('Digite um valor válido: '))
    while i <= 100:
        print(i)
        i += 1
else:
    while i <= 100:
        print(i)
        i += 1
'''

'''
IMPRIMIR TODOS OS PARES A PARTIR DE UMA ENTRADA E ATÉ 100

i = int(input('Digite um número menor que 100: '))

while i <= 100:
    if i%2 == 0:
        print(i)
        i += 1
    else:
        i = i + 1
        print(i)
        i += 2
'''

'''
IMPRIMIR DE 50 A 0

contador = 50

while 0 <= contador:
    print(contador)
    contador-=1
'''

'''
ENTRAR COM 10 NUMEROS E IMPRIMIR A QUANTIDADE DE ÍMPARES E PARES

p = 0
i = 0
contador = 1

while contador <= 10:
    num = int(input(f"Digite o {contador}º numero: "))
    if num%2 == 0:
        p += 1
    else:
        i += 1
    contador += 1

print("Quantidade de números ímpares:",i)
print("Quantidade de números pares:",p)
'''

'''
ESCREVER A MÚSICA DOS PATINHOS USANDO WHILE

import time

contador = 5
while contador >= 0:
    if contador != 0:
        print(f"\n{contador} patinhos foram passear\nAlém das montanhas para brincar\nA mamãe gritou: Quá, quá, quá, quá\nMas só {contador-1} patinhos voltaram de lá.")
        time.sleep(14)
    else:
        print('\nA mamãe patinha foi procurar\nAlém das montanhas, na beira do mar\nA mamãe gritou: Quá, quá, quá, quá\nE os 5 patinhos voltaram de lá.')
    contador -= 1
'''

'''
CÁLCULO DE ANOS E AUMENTO DA POPULAÇÃO

anos = 0
popA = 80000
popB = 200000


while popB > popA:
    popA *= 1.03
    popB *= 1.015
    anos += 1

print(f"Serão necessários {anos} anos para a população de A ser maior que a de B")
'''

'''
IMPRIMIR A TABUADA DE UMA ENTRADA

cont = 0
num = int(input('Digite o número que você deseja ver a tabuada: '))

while cont <= 10:
    print(f'{num} x {cont} = {num*cont}')
    cont +=1
'''
'''
PRINTAR NÚMEROS DE 1 A 20 NA VERTICAL E DEPOIS NA HORIZONTAL

cont = 1

while cont <=20:
    print(f'{cont}')
    cont += 1

cont = 1

while cont <=20:
    print(f'{cont}', end='\t')
    cont += 1
'''

'''
PRINTAR A SEQUÊNCIA DE FIBONACCI

import time
num = 1
nump = 0
numa = 0
while True:
    print(f'{num}')
    time.sleep(1)
    nump = num + numa
    numa = num
    num = nump
'''
'''
ADIVINHAR NUMERO SORTEADO

sort = random.randrange(1,10)
num = 0

while num != sort:
    num = int(input('\nEscolha um número: '))
    if num == sort:
        print('Parabéns, você acertou!')
    elif num > sort:
        print('O número que você escolheu é maior que o sorteado!')
    else:
        print('O número que você escolheu é menor que o sorteado!')
'''

'''
CÁLCULO DO FATURAMENTO TOTAL

totalToneladas = 0
controle = 's'

valor = float(input('Informe o valor em reais por tonelada: '))
while controle == 's':
    controle = input('Você gostaria de informar mais uma saída? (s/n): ')
    if controle == 's':
        saida = int(input('Informe a quantidade de toneladas que saiu: '))
        totalToneladas = totalToneladas + saida
    else:
        break

total = valor * totalToneladas

print(f'\nO valor em reais de faturamento no final do mês foi de R${total:.2f}.')
'''
'''
CÁLCULO DA MÉDIA

cont = 0
controle = 's'
total = 0

while controle == 's':
    controle = input('\nVocê gostaria de informar mais alguma nota: (s/n) ')
    if controle == 's':
        notas = float(input('Informe a nota da prova: '))
        total = total + notas
        cont += 1
    else:
        break

print(f'A média final do aluno foi {total/cont:.2f}')
'''
'''
CONTROLE DE PACIENTES

controle = 's'
totalL = 0
totalG = 0
totalA = 0
total = 0

while controle == 's':
    controle = input('Deseja informar mais algum paciente? (s/n): ')
    if controle == 's':
        sintoma = input('O paciente se encontra com sintomas leves (l), graves (g) ou é assintomático (a)? ')
        if sintoma == 'l':
            total += 1
            totalL += 1
        elif sintoma == 'g':
            totalG += 1
            total += 1
        elif sintoma == 'a':
            totalA += 1
            total += 1
        else:
            print('Informação inválida!')
    else:
        break

if total >= 1:
    print(f"\nPacientes com sintomas\nGraves: {100*totalG/total:.2f}%\nLeves: {100*totalL/total:.2f}%\nAssintomáticos: {100*totalA/total:.2f}%\nde um total de {total} pacientes.")
else:
    print('Não foi informado nenhum paciente!')
'''

'''
CONTAR AS VOGAIS

palavra = input("Escolha uma palavra para contar as vogais: ")
contador = 0


for i in palavra:
    if i == "a" or i == "e" or i == "i" or i == "o" or i =="u":
        contador += 1

print(f'A palavra escolhida possui {contador} vogais.')
'''




































