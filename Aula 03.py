'''
cm = float(input('Informe o valor em metros a ser convertido para centímetros: '))
mt = cm * 100
print('O valor em centímetros vale', mt,'cm')
'''

'''
raio = float(input('\nInforme o valor do raio do círculo: '))
area = 3.14 * (raio**2)
print('A área do círculo vale',area,'m²')
'''

'''
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
i = 0
while i<= 50:
    print(i)
    i += 1
'''

'''
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
contador = 50

while 0 <= contador:
    print(contador)
    contador-=1
'''

'''
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
cont = 0
num = int(input('Digite o número que você deseja ver a tabuada: '))

while cont <= 10:
    print(f'\n{num} x {cont} = {num*cont}')
    cont +=1
'''




















































