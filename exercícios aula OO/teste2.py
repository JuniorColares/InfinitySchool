from configuracao import Configuracao

modelo = input('Qual o modelo do seu aparelho: ')
fabricante = input('Qual o fabricante: ')
processador = input('Qual o processador: ')
mram = int(input('Memória RAM: '))
tHD = float(input('HD: '))

ap1 = Configuracao(modelo, fabricante, processador, mram, tHD)

ap1.ocuparHD(2)
ap1.limparHD(1)