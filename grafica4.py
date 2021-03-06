from pyprocessing import *
import TorreHanoi

roteiro_teste = [('Pino1','Pino2'),('Pino1','Pino3'),('Pino1','Pino4'),('Pino3','Pino4'),('Pino2','Pino4'),]

class Torre(object):
 	def __init__(self, centro = None, indice = None):
 		self.altura = 200
 		self.torreAltura = self.altura + 10
 		self.largura = 270
 		self.centro = centro
 		self.indice = indice
 		self.discos = 0

class Disco(object):
	def __init__(self, largura, posX, posY):
		self.largura = largura
		self.altura = 10
		self.posX = posX
		self.posY = posY
		self.torre = 0

#pegar os resultados da funcao Hanoi, e os devolve em forma de lista de inteiros,
#e pergunta quantos discos a pessoa deseja utilizar em um maximo de 20 discos
def comandos(): 
	global tamanho
	tamanho = input('Digite a quantidade de discos de 1 a 22: ')
	roteiro = trata_roteiro(roteiro_teste)
	return roteiro

def torre_inteiro(st): #Auxiliar de trata_roteiro
	if st == 'Pino1':
		return 0
	elif st == 'Pino2':
		return 1
	elif st == 'Pino3':
		return 2
	else:
		return 3

def trata_roteiro(roteiro): #usada na comandos, tranforma as strings em 0,1 ou 2
	lista = []
	for tupla in roteiro:
		lista.append(torre_inteiro(tupla[0]))
		lista.append(torre_inteiro(tupla[1]))
		lista.append(torre_inteiro(tupla[1]))
	return lista


def setup():
	global tamanho
	global listaTorres
	global listaDiscos
	global roteiro
	global frame
	global passoatual

	frame = 0
	passoatual = 0
	roteiro = comandos()

	height = 500
	width = 1220
	size(width,height)
	background(255)

#construindo as torres
	i = 0
	listaTorres = []
	widthDisponivel = 1130
	for t in range(0, 4):
		centro = widthDisponivel/8
		centro = centro + (widthDisponivel/4 * i) + 50
		listaTorres.append(Torre(centro,i))
		i += 1

	listaTorres[0].discos = tamanho

#construindo os discos dado n 
	listaDiscos = []
	i = 0
	larguraInicial = 1130/4 - 30
	for t in range(0,tamanho):
		largura = larguraInicial - i*10
		if largura < 40:
			largura = 40
		posX = listaTorres[0].centro - largura/2
		posY = 440 - (i*11)
		listaDiscos.append(Disco(largura,posX,posY))
		i += 1

def draw():
	global tamanho
	global listaTorres
	global listaDiscos
	global roteiro
	global frame
	global passoatual

	background(255)
	fill(100)
	noStroke()

	frame += 1

#testa qual passo deve ser feito
	if frame % 20 == 0 and passoatual < len(roteiro):
		passo = roteiro[passoatual]
		torre = listaTorres[passo]
		pula = False
		i=0
		for d in range(0,tamanho):
			disco = listaDiscos[i]
			if disco.posY < 150: 				
				if disco.torre == passo:
					altura = 0
					j = 0
					for di in range(0, tamanho):
						if listaDiscos[j].torre == passo:
							altura += 1
						j += 1
					disco.posY = 450 - (altura*10.5)
					pula = True
					break
				else:			
					disco.posX = torre.centro - disco.largura/2
					disco.torre = passo
					pula = True
					break
			i += 1

		if pula == False:
			i = 0
			menorDisco = None
			for d in range(0,tamanho):
				disco = listaDiscos[i]				
				if disco.torre == passo:					
					if menorDisco == None:
						menorDisco = disco
					if disco.largura < menorDisco.largura:						
						menorDisco = disco
				i += 1
			if menorDisco != None:
				menorDisco.posY = 100
		
		passoatual += 1		


	i = 0

	# Imprime as torres
	for t in range(0,4):
		torre = listaTorres[i]
		fill(99,24,0)
		rect(torre.centro-10, 250-50, 15, torre.torreAltura+50)
		fill(99,24,0)
		rect(torre.centro-torre.largura/2+5, 450, torre.largura-10, 20)
		i += 1	

	# Imprime os discos
	i = 0
	for t in range(0, tamanho):
		disco = listaDiscos[i]
		stroke(186,27,19)
		fill(255,0,0)
		rect(disco.posX, disco.posY, disco.largura, disco.altura)
		i += 1	


run()