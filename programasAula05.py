
#~~~~Criar uma função que imprima os dois menores números entre os dois fornecidos~~~~
def funcao01():
    def verificaMenor(num1,num2):
        if num1 < num2:
            print(f'{num1} é o menor número dentre os dois digitados!')
        elif num2 < num1:
            print(f'{num2} é o menor número dentre os dois digitados!')
        else:
            print('Os números digitados são iguais!')

    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))

    verificaMenor(num1,num2)


#~~~~Criar função para verificar se é positivo~~~~

def funcao02():
    def verificaPositivo(num):
        if num > 0:
            print('O número digitado é positivo!')
        elif num < 0:
            print('O número digitado é negativo!')
        else:
            print('O número digitado é nulo!')

    num = int(input('Informe o número que deseja verificar: '))
    verificaPositivo(num)


#~~~~função para verificar se um terceiro parâmetro é maior que a soma dos dois primeiros~~~~
def funcao03():
    def verificaSoma(a,b,c):
        if (a+b) > c:
            return True
        else:
            return False

    num1 = int(input('Informe o primeiro numero da soma: '))
    num2 = int(input('Informe o segundo numero da soma: '))
    num3 = int(input('Informe o limite para verificação: '))

    print(verificaSoma(num1,num2,num3))

#~~~~verificar quantosa numeros são maiores que um limite~~~~

def funcao04():
    def verificaMaior(a,b,c):
        if a>c and b>c:
            print('Os dois números são maiores que o limite!')
        elif (a>c and b<c) or (a<c and b>c):
            print('Apenas um dos números é maior que o limite!')
        else:
            print('Nenhum dos números é maior que o limite!')

    num1 = int(input('Informe o primeiro número: '))
    num2 = int(input('Informe o segundo número: '))
    limite = int(input('Informe o limite de verificação: '))

    verificaMaior(num1,num2,limite)
'''
'''
def funcao05():
    def funcaoVerifica(num):
        if num%3 == 0 and num%5 != 0:
            return "fizz"
        elif num%3 != 0 and num%5 == 0:
            return "buzz"
        elif num%3 == 0 and num%5 == 0:
            return "FizzBuzz"
        else:
            return num

    num = int(input('Informe um valor para verificação: '))
    print(funcaoVerifica(num))
'''
'''
def funcao06():
    def percentual(num,perc):
        final = num*(1+(perc/100))
        return final

    num = int(input('Informe o numero inicial: '))
    perc = float(input('Informe o percentual em %: '))

    print(percentual(num,perc))
'''
'''
def funcao07():
    def areaT(base,altura):
        area = base * altura / 2
        return area

    base = int(input('Informe a medida da base do triângulo: '))
    altura = int(input('Informe a medida da altura do triângulo: '))

    print(areaT(base,altura))
'''
'''
import random

def funcao08():
    def sorteio(a,b):
        num = random.randrange(a,b)
        return num

    a = int(input('Informe o início do intervalo: '))
    b = int(input('Informe o fim do intervalo: '))

    num = sorteio(a,b)
    print(num)
'''
'''
def funcao09():
    def funcaoSoma(a):
        cont = 0
        soma = 0
        while cont <=a:
            soma = soma + cont
            cont += 1
        return soma

    num = int(input('Informe um valor inteiro positivo: '))

    print(funcaoSoma(num))
'''
'''
def funcao10():
    def operacao(a,b,c):
        if c == '+':
            oper = a + b
        elif c == '-':
            oper = a - b
        elif c == '*':
            oper = a*b
        elif c == '/':
            oper = a/b
        else:
            oper = 'Operador inválido!'
        return oper

    num1 = int(input('Informe o primeiro numero: '))
    num2 = int(input('Informe o segundo numero: '))
    oper = input('informe a operação desejada: (+)(-)(*)(/) ')

    print(operacao(num1,num2,oper))


















