import programasAula01

print('***********************************')
print('Escolha o programa que deseja rodar')
print('***********************************')


print('Opções:')
print('(1) Cálculo do IMC')
print('(2) Transformação de temperatura (TF -> TC)')
print('(3) Área de um retângulo')
print('(4) Porcentagem de votos')
print('(5) Realizar mudança de variáveis')
print('(6) Cálculo do custo de um carro')

opcao = int(input('Escolha a opção desejada: '))

if (opcao == 1):
    programasAula01.imc()
elif (opcao == 2):
    programasAula01.temperatura()
elif ( opcao == 3):
    programasAula01.arearet()
elif (opcao == 4):
    programasAula01.votos()
elif (opcao == 5):
    programasAula01.mudanca()
elif (opcao == 6):
    programasAula01.custo()