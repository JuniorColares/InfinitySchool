# cerquilha indica um comentário

'''
O comentário em mais de uma linha pode ser
feito com três aspas simples ou duplas no
início e no final do comentário
'''


# propriedades sep e end na função print
'''
nome = 'Júnior'
print("Olá, me chamo ", nome,'!', sep='', end=" ")
print("Sou da Infinity.")

print("CPF: 989","499","440", sep=".", end="-")
print("73")
'''


#variáveis e tipos primitivos
'''
string
int
float
bool
'''

#dontpad.com/infinity28aula01  -- arquivos com os documentos da aula

#cálculo do IMC
'''
peso = input('informe o peso do paciente (kg): ')
peso = float(peso)
altura = input('informe a altura do paciente (m): ')
altura = float(altura)
imc = peso/(altura**2)

print("O IMC do paciente é:", round(imc, 2))
'''

#transformação de temperatura
'''
TF = input("Digite a temperatura em Fahrenheit: ")
TF = float(TF)
TC = round((((TF-32)*5)/9),2)
print("A temperatura em Celcius é ", TC)
'''

#calcular a área de um retângulo
'''
base = input("informe o valor da base do retângulo (m): ")
base = float(base)
altura = input("informe o valor da altura do retângulo (m): ")
altura = float(altura)
area = base*altura

print("A área do retângulo vale",area,"m²")
'''

#quantidade de votos
'''
total = input("Digite a quantidade total de votos: ")
total = int(total)
nulos = input("Digite a quantidade de votos nulos: ")
nulos = int(nulos)
pnulos = round(100*nulos/total,2)
brancos = input("Digite a quantidade de votos brancos: ")
brancos = int(brancos)
pbrancos = round(100*brancos/total,2)
validos = (total - nulos - brancos)
pvalidos = round(100*validos/total,2)

print("O total de votos foi de ",total,", sendo ",pnulos,"% nulos, ",pbrancos,"% brancos e ",pvalidos,"% válidos.", sep='')
'''

#mudança de variável
'''
A = 10
B = 20
print("A variável A vale:",A)
print("A variável B vale:",B)
C = A
A = B
B = C
print("Agora A vale:",A)
print("Agora B vale:",B)
'''

#calculo do custo de um carro
'''
custoDeFabrica = input("Qual o valor do custo de fábrica do carro escolhido: ")
custoDeFabrica = float(custoDeFabrica)

valorFinal = custoDeFabrica*(1 + 0.28 + 0.45)

print("O valor final para o consumidor do carro escolhido é de R$",valorFinal)
'''