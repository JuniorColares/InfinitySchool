class Conta:
    def __init__(self, titular, numero, saldo, vip):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.vip = vip

    def saca(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print('O valor de saque não pode ser superior ao saldo!')

    def deposita(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print('O valor de deposito não pode ser inferior a zero!')

    def extrato(self):
        print('Titular: ',self.titular,'\nNúmero da conta:',self.numero,'\nSaldo: R$',self.saldo,'\nStatus:',self.vip) 