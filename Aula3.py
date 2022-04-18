import programasAula03

print('***********************************')
print('Escolha o programa que deseja rodar')
print('***********************************')

print('Opções:')
print('(1) Converter metros para centímetros')
print('(2) Calcular área do círculo')
print('(3) Faixa de calor')
print('(4) Imprimir até 100')
print('(5) Imprimir pares até 100')
print('(6) Imprimir quantidade de pares e ímpares')
print('(7) Relação tempo x aumento população')
print('(8) Imprimir tabuada')
print('(9) Adivinhar número sorteado')
print('(10) Calculo do faturamento total')
print('(11) Calcular a média de N notas')
print('(12) Controle de pacientes')
print('(13) Contar as vogais de uma palavra')
opcao = int(input('\nOpção desejada: '))

if (opcao == 1):
    programasAula03.converter()
elif (opcao == 2):
    programasAula03.areac()
elif (opcao == 3):
    programasAula03.faixacalor()
elif (opcao == 4):
    programasAula03.imprimir100()
elif (opcao == 5):
    programasAula03.imprimirpares()
elif (opcao == 6):
    programasAula03.quantidadepi()
elif (opcao == 7):
    programasAula03.população()
elif (opcao == 8):
    programasAula03.tabuada()
elif (opcao == 9):
    programasAula03.adivinhacao()
elif (opcao == 10):
    programasAula03.faturamento()
elif (opcao == 11):
    programasAula03.median()
elif (opcao == 12):
    programasAula03.controlepacientes()
elif (opcao == 13):
    programasAula03.vogais()