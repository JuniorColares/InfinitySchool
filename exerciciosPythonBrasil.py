# 1. Classe Bola: Crie uma classe que modele uma bola:
# a. Atributos: Cor, circunferência, material
# b. Métodos: trocaCor e mostraCor

'''
class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, novaCor):
        self.cor = novaCor

    def mostraCor(self):
        print(f'A bola é da cor: {self.cor}')

bola = Bola('Vermelha',20,'Couro')

bola.mostraCor()
bola.trocaCor('Azul')
bola.mostraCor()
'''

# 2. Classe Quadrado: Crie uma classe que modele um quadrado:
# a. Atributos: Tamanho do lado
# b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

'''
class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudaLado(self, novoLado):
        self.lado = novoLado

    def mostraLado(self):
        print(f'O valor do lado do quadrado é {self.lado}')

    def calculaArea(self):
        print(f'A área do quadrado vale {self.lado**2}m²')

quadrado = Quadrado(10)
quadrado.mostraLado()
quadrado.mudaLado(5)
quadrado.mostraLado()
quadrado.calculaArea()
'''

# 3. Classe Retangulo: Crie uma classe que modele um retangulo:
# a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

'''
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudarBase(self, novabase):
        self.base = novabase

    def mudarAltura(self, novaaltura):
        self.altura = novaaltura

    def retornarLados(self):
        print(f'Base: {self.base}m\nAltura: {self.altura}m')

    def calculaArea(self):
        print(f'A área do retângulo vale {self.base*self.altura}m²')

    def calculaPerimetro(self):
        perimetro = (2*self.base)+(2*self.altura)
        print(f'Perímetro do retângulo: {perimetro}m')

ret = Retangulo(10,20)

ret.retornarLados()
ret.calculaArea()
ret.calculaPerimetro()
'''

# 4. Classe Pessoa: Crie uma classe que modele uma pessoa:
# a. Atributos: nome, idade, peso e altura
# b. Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            self.crecer()
        self.idade += 1

    def engordar(self,kgganhos):
        self.peso += kgganhos

    def emagrecer(self, kgperdidos):
        self.peso -= kgperdidos

    def crecer(self):
        self.altura += 0.05

    def mostrar(self):
        print(f'Nome: {self.idade}\nIdade: {self.idade}\nPeso: {self.peso}\nAltura: {self.altura}')

pessoa = Pessoa('Junior', 20, 87,1.7)

pessoa.envelhecer()
pessoa.envelhecer()
pessoa.mostrar()
'''

# 5. Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
'''
class Conta:
    def __init__(self, conta, titular, saldo = 0.0):
        self.conta = conta
        self.titular = titular
        self.saldo = saldo
    
    def mudarNome(self, novonome):
        self.titular = novonome
    
    def depositar(self, deposito):
        if deposito > 0:
            self.saldo += deposito
            
    def sacar(self, saque):
        if saque < self.saldo:
            self.saldo -= saque
'''

# 6. Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
'''
class Televisao:
    def __init__(self, volume, canal = 0):
        self.canal = canal
        self.volume = volume

    def mudaCanal(self,canal):
        if 1 < canal < 20:
            self.canal = canal
        else:
            print('Canal indisponível')

    def aumentaVolume(self):
        if self.volume < 100:
            self.volume += 1

    def diminuiVolume(self):
        if self.volume > 0:
            self.volume -= 1

televisao = Televisao(99)
print(televisao.volume)
televisao.aumentaVolume()
print(televisao.volume)
televisao.aumentaVolume()
print(televisao.volume)
'''

# 7. Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
# a. Atributos: Nome, Fome, Saúde e Idade
# b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
# Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
'''
class Tamagushi:
    def __init__(self, nome, saude = 10, fome = 5, idade = 0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        
    def alteraNome(self, nome):
        self.nome = nome
        
    def aumentaFome(self):
        if 10 > self.fome >= 0:
            self.fome += 1
    
    def diminuiFome(self):
        if 10 >= self.fome > 0:
            self.fome -= 1

    def aumentaSaude(self):
        if 10 > self.saude > 0:
            self.saude += 1

    def diminuiSaude(self):
        if 10 > self.saude > 0:
            self.saude -= 1
    
    def envelhecer(self):
        if self.idade < 12:
            self.idade += 1
        else:
            print(f'{self.nome} morreu')
            
    def humor(self):
        if self.fome > 7 or self.saude < 3 or (self.fome > 5 and self.saude < 5):
            print('MAU HUMOR')
        else:
            print('BOM HUMOR')
'''

# 8. Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
'''
class Macaco:
    def __init__(self, nome, bucho = []):
        self.nome = nome
        self.bucho = bucho

    def comer(self, alimento):
        self.bucho.append(alimento)

    def verBucho(self):
        print(self.bucho)

    def digerir(self):
        self.bucho.pop(0)

macaco = Macaco('Junior')
macaco2 = Macaco('Ytalo')
macaco.comer('banana')
macaco.comer('uva')
macaco.comer('maçã')
macaco.verBucho()
macaco.digerir()
macaco.verBucho()
macaco.digerir()
macaco.verBucho()
macaco.comer(macaco2)
macaco.verBucho()
'''

# 9. Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:
#
# a. Possua uma classe chamada Ponto, com os atributos x e y.                         OK
# b. Possua uma classe chamada Retangulo, com os atributos largura e altura.          OK
# c. Possua uma função para imprimir os valores da classe Ponto                       OK
# d. Possua uma função para encontrar o centro de um Retângulo.                       OK
# e. Você deve criar alguns objetos da classe Retangulo.
# f. Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
# g. A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
# h. O valor do centro do objeto deve ser mostrado na tela
# i. Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostraPonto(self):
        print(f'({self.x} ,{self.y})')

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def centroRet(self):
        x = self.base/2
        y = self.altura/2
        centro = Ponto(x,y)
        print(f'Centro do retângulo: ')
        centro.mostraPonto()

ret = Retangulo(10,20)
ret.centroRet()




















