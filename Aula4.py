import programasAula04

print('***********************************')
print('Escolha o programa que deseja rodar')
print('***********************************')

print('\nOpções:')
print('(1) Sequência de ZERO a um número informado')
print('(2) Informações sobre uma população')
print('(3) Calcular a média de n notas')
print('(4) Porcentagem de pacientes com sintomas de Covid')
print('(5) Contas as vogais em uma palavra')
opcao = int(input('Opção desejada: '))

if opcao == 1:
    programasAula04.imprimir()
elif opcao == 2:
    programasAula04.populacao()
elif opcao == 3:
    programasAula04.media()
elif opcao == 4:
    programasAula04.sintomas()
elif opcao == 5:
    programasAula04.vogais()
else:
    print('Opção inválida!')