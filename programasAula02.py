#CÁLCULO DA MÉDIA

def media():
    av1 = float(input('Digite o valor da nota da primeira prova: '))
    av2 = float(input('Digite o valor da nota da segunda prova: '))
    av3 = float(input('Digite o valor da nota da terceira prova: '))

    media = (av1 + av2 + av3)/3

    print(f'A média do aluno foi {media:.2f}')


'''
CÁLCULO DO IMC

peso = float(input('Informe o peso do paciente (kg): '))
altura = float(input('Informe a altura do paciente (m): '))
imc = peso/(altura**2)

print("O IMC do paciente é:", round(imc, 2))
'''

#CÁLCULO DA ÁREA DE UM QUADRADO

def areaq():
    lado = float(input("Informe o valor do lado do quadrado (m): "))
    area = lado**2

    print("A área do quadrado vale",area,"m²")


#USUÁRIO E SENHA

def usuario():
    import os

    os.system('cls')

    usuario = input('Informe seu usuário: ')

    os.system('cls')

    senha = input('Informe sua senha: ')

    os.system('cls')

    if usuario == "ADM" and senha == "123":
        print('Login realizado com sucesso')
    else:
        print('Usuário ou senha inválidos')



#VERIFICAÇÃO DE TEMPERATURA

def cancela():
    temp = float(input('Informe a temperatura medida: '))

    if temp <= 37:
        print('CANCELA LIBERADA!')
    else:
        print('CANCELA NÃO LIBERADA!')


#MAIOR NÚMERO

def maior():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    if num1 > num2:
        print("O maior valor escolhido foi:",num1)
    else:
        print("O maior valor escolhido foi:", num2)


#NÚMERO POSITIVO/NEGATIVO

def positivo():
    num = float(input('Digite um número para verificação: '))

    if num < 0:
        print('O número escolhido é negativo!')
    elif num == 0:
        print('O número escolhido é igual a ZERO!')
    else:
        print('O número escolhido é positivo!')


#APROVAÇÃO MÉDIA

def aprovado():
    n1 = float(input('Valor da primeira nota: '))
    n2 = float(input('Valor da segunda nota: '))
    n3 = float(input('Valor da terceira nota: '))

    media = (n1 + n2 + n3)/3

    if media >=8:
        print('Aprovado com louvor!')
    elif media >= 6:
        print('Aprovado!')
    elif media >= 4:
        print('Recuperação!')
    else:
        print('Reprovado!')



#VERIFICAÇÃO PAR/ÍMPAR

def par():
    num = int(input("Digite o número escolhido: "))

    resto = num%2

    if resto == 0:
        print('O número escolhido é par')
    else:
        print('O número escolhido é ímpar')



#VERIFICAÇÃO IMC

def imcv():
    altura = float(input('Informe a altura do paciente: '))
    peso = float(input('Informe o peso do paciente: '))

    imc = peso/altura**2

    if imc < 18.5:
        print('Subnutrido')
    elif imc < 24.9:
        print('Normal')
    elif imc < 29.9:
        print('Sobrepeso')
    elif imc < 39.9:
        print('Obesidade')
    else:
        print('Alerta')



#TRIÂNGULO

def triangulo():
    l1 = float(input('Informe a medidade do lado 1 do triângulo: '))
    l2 = float(input('Informe a medidade do lado 2 do triângulo: '))
    l3 = float(input('Informe a medidade do lado 3 do triângulo: '))

    if ((l1 < l2 - l3) or (l1 < l3 - l2)) or ((l2 < l1 - l3) or (l2 < l3 - l1)) or ((l3 < l2 - l1) or (l3 < l1 - l2)):
        print('O triângulo não existe')
    elif l1 == l2 == l3:
        print('O triângulo é equilátero')
    elif l1 != l2 and l1 != l2 and l2 != l3:
        print('O triângulo é escaleno')
    else:
        print('O triângulo é isóceles')



#HOSPITAIS

def hospitais():
    q1 = int(input('Informe a quantidade de respiradores do hospital 01: '))
    p1 = float(input('Informe a ocupação do hospital 01: '))
    q2 = int(input('\nInforme a quantidade de respiradores do hospital 02: '))
    p2 = float(input('Informe a ocupação do hospital 02: '))
    q3 = int(input('\nInforme a quantidade de respiradores do hospital 03: '))
    p3 = float(input('Informe a ocupação do hospital 03: '))
    q4 = int(input('\nInforme a quantidade de respiradores do hospital 04: '))
    p4 = float(input('Informe a ocupação do hospital 04: '))
    q5 = int(input('\nInforme a quantidade de respiradores do hospital 05: '))
    p5 = float(input('Informe a ocupação do hospital 05: '))

    if (q1 < 50 or q2 < 50 or q3 < 50 or q4 < 50 or q5 < 50) or (p1 > 60 or p2 > 60 or p3 > 60 or p4 > 60 or p5 > 60):
        print('\nSerão adicionados mais 5 hospitais!')
    else:
        print('\nNão há necessidade de mais hospitais!')



#ÍNDICE DE POLUIÇÃO

def poluicao():
    i = float(input('Informe o índice de poluição medido: '))

    if i < 0:
        print('Informe um índice válido.')
    elif i < 0.3:
        print('Todas as indústrias podem operar normalmente.')
    elif i < 0.4:
        print('As indústrias do 1º grupo devem suspender suas atividades.')
    elif i < 0.5:
        print('As indústrias dos grupos 1 e 2 devem suspender suas atividades')
    else:
        print('Todos os grupos devem suspender suas atividades.')



#RESULTADO JOGO FUTEBOL

def futebol():
    time1 = input('Informe o primeiro time: ')
    gol1 = int(input('Quantos gols ele marcou: '))

    time2 = input('\nInforme o segundo time: ')
    gol2 = int(input('Quantos gols ele marcou: '))

    if gol1 > gol2:
        print('\nO time vencedor foi o', time1)
    elif gol2 > gol1:
        print('\nO time vencedor foi o',time2)
    else:
        print('\nEMPATE!')



#APOSENTADORIA

def aposentadoria():
    import datetime

    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()

    cod = int(input('Código do funcionário: '))
    nasc = int(input('Ano de nascimento do funcionário: '))
    ent = int(input('Ano de admissão do funcionário: '))
    idade = date.year - nasc
    tempo = date.year - ent

    if idade >= 65 or tempo > 30 or (idade > 60 and tempo > 25):
        print(f'O funcionário de código {cod}, idade de {idade} anos, tem {tempo} anos de empresa: REQUERER APOSENTADORIA')
    else:
        print(f'O funcionário de código {cod}, idade de {idade} anos, tem {tempo} anos de empresa: NÃO QUERER APOSENTADORIA')


#PRODUTO MAIS BARATO

def barato():
    p1 = float(input('Informe o preço do primeiro produto: '))
    p2 = float(input('Informe o preço do segundo produto: '))
    p3 = float(input('Informe o preço do terceiro produto: '))

    if p1<p2 and p1<p3:
        print('Comprar o primeiro produto.')
    elif p2<p1 and p2<p3:
        print('Comprar o segundo produto')
    elif p3<p1 and p3<p2:
        print('Comprar o terceiro produto')
    elif p1<p2 and p1==p3:
        print('Você pode escolher entre o primeiro e terceiro produtos')
    elif p1<p3 and p1==p2:
        print('Você pode escolher entre o primeiro e segundo produtos')
    elif p2<p1 and p2==p3:
        print('Você pode escolher entre o segundo e terceiro produtos')
    else:
        print('Todos os produtos possuem o mesmo valor!')


#SIGNOS

def signos():
    dia = int(input('Informe seu dia de nascimento: '))
    mes = int(input('Informe seu mês de nascimento: '))

    if (mes == 3 and (21 <= dia <= 31)) or (mes == 4 and (0 < dia <= 20)):
        print('Você é do signo de áries!')
    elif (mes == 4 and (21 <= dia <= 30)) or (mes == 5 and (0 < dia <= 20)):
        print('Você é do signo de touro!')
    elif (mes == 5 and (21 <= dia <= 31)) or (mes == 6 and (0 < dia <= 20)):
        print('Você é do signo de gêmeos!')
    elif (mes == 6 and (21 <= dia <= 30)) or (mes == 7 and (0 < dia <= 22)):
        print('Você é do signo de câncer!')
    elif (mes == 7 and (23 <= dia <= 31)) or (mes == 8 and (0 < dia <= 22)):
        print('Você é do signo de leão!')
    elif (mes == 8 and (23 <= dia <= 30)) or (mes == 9 and (0 < dia <= 22)):
        print('Você é do signo de virgem!')
    elif (mes == 9 and (23 <= dia <= 31)) or (mes == 10 and (0 < dia <= 22)):
        print('Você é do signo de libra!')
    elif (mes == 10 and (23 <= dia <= 31)) or (mes == 11 and (0 < dia <= 21)):
        print('Você é do signo de escorpião!')
    elif (mes == 11 and (22 <= dia <= 30)) or (mes == 12 and (0 < dia <= 21)):
        print('Você é do signo de sagitário!')
    elif (mes == 12 and (22 <= dia <= 31)) or (mes == 1 and (0 < dia <= 20)):
        print('Você é do signo de capricórnio!')
    elif (mes == 1 and (21 <= dia <= 31)) or (mes == 2 and (0 < dia <= 18)):
        print('Você é do signo de aquário!')
    elif (mes == 2 and (19 <= dia <= 29)) or (mes == 3 and (0 < dia <= 20)):
        print('Você é do signo de peixes!')
    else:
        print('Você não digitou uma data válida!')
