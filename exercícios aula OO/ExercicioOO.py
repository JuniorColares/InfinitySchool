from conta import Conta

titular = input('Nome do Titular: ')
numero = input('Número da conta: ')
saldo = float(input('Qual o saldo a ser inicializado: '))
vip = input('Cliente VIP ou COMUM: ')

conta = Conta(titular, numero, saldo, vip)

conta.extrato()