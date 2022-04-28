import programasAula05
import random

print('***********************************')
print('Escolha o programa que deseja rodar')
print('***********************************')

print('\nOpções:')
print('(1) Verificar o menor número digitado')
print('(2) Verificar se o número é positivo')
print('(3) Verificar se a soma é maior que o limite')
print('(4) Verificar se os números são maiores que o limite')
print('(5) FizzBuzz')
print('(6) Informar acréscimo percentual')
print('(7) Calcular área do triângulo')
print('(8) Mostrar um número sorteado dentro de um limite informado')
print('(9) Soma de todos os números até um limite')
print('(10) Realizar operação solicitada')
opcao = int(input('Opção desejada: '))

if opcao == 1:
    programasAula05.funcao01()
elif opcao == 2:
    programasAula05.funcao02()
elif opcao == 3:
    programasAula05.funcao03()
elif opcao == 4:
    programasAula05.funcao04()
elif opcao == 5:
    programasAula05.funcao05()
elif opcao == 6:
    programasAula05.funcao06()
elif opcao == 7:
    programasAula05.funcao07()
elif opcao == 8:
    programasAula05.funcao08()
elif opcao == 9:
    programasAula05.funcao09()
elif opcao == 10:
    programasAula05.funcao10()
else:
    print('Opção inválida')