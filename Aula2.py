import programasAula02
import programasAula01

print('***********************************')
print('Escolha o programa que deseja rodar')
print('***********************************')

print('Opções:')
print('(1) Cálculo da média')
print('(2) Cálculo do IMC')
print('(3) Cálculo da área de um quadrado')
print('(4) Validação de usuário e senha')
print('(5) Liberação de cancela')
print('(6) Apresentação do maior número')
print('(7) Informar se número positivo, negativo ou ZERO')
print('(8) Informar se aprovado ou não por média')
print('(9) Verificação se par ou ímpar')
print('(10) Verificação de IMC')
print('(11) Tipo de triângulo')
print('(12) Quantidade de hospitais')
print('(13) Índice de poluição')
print('(14) Resultado jogo de futebol')
print('(15) Aposentadoria')
print('(16) Produto mais barato')
print('(17) Signos')

opcao = int(input('Opção desejada: '))

if (opcao == 1):
    programasAula02.media()
elif (opcao == 2):
    programasAula01.imc()
elif (opcao == 3):
    programasAula02.areaq()
elif (opcao == 4):
    programasAula02.usuario()
elif (opcao == 5):
    programasAula02.cancela()
elif (opcao == 6):
    programasAula02.maior()
elif (opcao == 7):
    programasAula02.positivo()
elif (opcao == 8):
    programasAula02.aprovado()
elif (opcao == 9):
    programasAula02.par()
elif (opcao == 10):
    programasAula02.imcv()
elif (opcao == 11):
    programasAula02.triangulo()
elif (opcao == 12):
    programasAula02.hospitais()
elif (opcao == 13):
    programasAula02.poluicao()
elif (opcao == 14):
    programasAula02.futebol()
elif (opcao == 15):
    programasAula02.aposentadoria()
elif (opcao == 16):
    programasAula02.barato()
elif (opcao == 17):
    programasAula02.signos()