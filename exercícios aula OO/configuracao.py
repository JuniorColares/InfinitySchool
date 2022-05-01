class Configuracao:
    def __init__(self, modelo, fabricante, processador, mram, tamanhoHD, hdocupado = 0, ligado = False):
        self.modelo = modelo
        self.fabricante = fabricante
        self.processador = processador
        self.mram = mram
        self.tamanhoHD = tamanhoHD
        self.hdocupado = hdocupado
        self.ligado = ligado

    def liga(self):
        if self.ligado == True:
            print('Aparalho já está ligado!')
        else:
            self.ligado = True
            print('Aparelho inicializado com sucesso!')

    def desliga(self):
        if self.ligado == False:
            print('Aparelho já está desligado!')
        else:
            self.ligado = False
            print('Aparelho desligado com sucesso!')

    def limparHD(self, valor):
        if valor > self.hdocupado:
            print('Foi liberado o tamanho de',self.hdocupado,'. Memória total disponível!')
            self.hdocupado = 0
        else:
            self.hdocupado -= valor
            print('Foi liberado o tamanho de',valor,'. Nova memória ocupada:',self.hdocupado)
    
    def ocuparHD(self, valor):
        if valor > (self.tamanhoHD - self.hdocupado):
            print('HD não possui esse tamanho disponível. Aumente sua memória!')
        else:
            self.hdocupado += valor
            print('Memória ocupada com sucesso!')