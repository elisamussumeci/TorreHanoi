import numpy as np

roteiro = []
def removerPilha(nome,pilha,topo,base):
    if topo > base:
        topo = topo - 1
        sucesso = True
        return pilha,topo,sucesso,nome
    else:
        sucesso=False
        return pilha,topo,sucesso,nome

def inserirPilha(nome,pilha,tamanho,topo,valor):
    if(topo<=tamanho-1):
        pilha[topo] = valor
        topo = topo + 1
        sucesso = True
        return pilha,topo,sucesso,nome
    else:
        sucesso = False
        return pilha,topo,sucesso,nome

def inicializarPilha(nome,base,tamanho):
    if (base<0) or (tamanho<0):
        sucesso = False
        return None,None,sucesso
    else:
        topo = base
        pilha = np.empty(tamanho)
        sucesso = True
        return pilha,topo,sucesso,nome

def Hanoi(ndiscos):
	global roteiro
	roteiro = []
	PilhaInicio = inicializarPilha('Inicio', 0, ndiscos)
	cont = ndiscos
	while cont > 0:
		PilhaInicio = inserirPilha(PilhaInicio[3],PilhaInicio[0], ndiscos, PilhaInicio[1], cont)
		cont = cont-1
	PilhaFinal = inicializarPilha('Final', 0, ndiscos)
	PilhaAux = inicializarPilha('Auxiliar', 0, ndiscos)
	last=0
	if ndiscos % 2 == 0:
		while PilhaFinal[1] != ndiscos :
			(PilhaInicio,PilhaAux, last) = legalmove(PilhaInicio, PilhaAux, last)
			if PilhaFinal[1] == ndiscos:
				break
			(PilhaInicio,PilhaFinal, last) = legalmove(PilhaInicio, PilhaFinal, last)
			if PilhaFinal[1] == ndiscos:
				break
			(PilhaAux,PilhaFinal, last) = legalmove(PilhaAux,PilhaFinal, last)
			if PilhaFinal[1] == ndiscos:
				break
	else:
		while PilhaFinal[1] != ndiscos :
			(PilhaInicio,PilhaFinal, last) = legalmove(PilhaInicio, PilhaFinal, last)
			if PilhaFinal[1] == ndiscos:
				break
			(PilhaInicio,PilhaAux, last) = legalmove(PilhaInicio, PilhaAux, last)
			if PilhaFinal[1] == ndiscos:
				break
			(PilhaAux,PilhaFinal, last) = legalmove(PilhaAux,PilhaFinal, last)
			if PilhaFinal[1] == ndiscos:
				break
	return roteiro


#Pilha1 = (pilha, topo, sucesso)

def legalmove(Pilha1, Pilha2, last):
	ValorTopo1 = Pilha1[0][Pilha1[1]-1]
	ValorTopo2 = Pilha2[0][Pilha2[1]-1]
	if Pilha1[1] and Pilha2[1] != 0:
		if ValorTopo1 < ValorTopo2 and ValorTopo1 != last:
			(Pilha1,Pilha2,last) = move(Pilha1,Pilha2)
			roteiro.append((Pilha1[3], Pilha2[3]))
			print 'mova disco da Pilha%s para a Pilha%s' %(Pilha1[3],Pilha2[3])
		elif ValorTopo1 > ValorTopo2 and ValorTopo2 != last:
			(Pilha2, Pilha1, last) = move(Pilha2,Pilha1)
			roteiro.append((Pilha2[3], Pilha1[3]))
			print 'mova disco da Pilha%s para a Pilha%s' %(Pilha2[3],Pilha1[3])
	elif Pilha1[1] == 0 and ValorTopo2 != last:
		(Pilha2, Pilha1, last) = move(Pilha2,Pilha1)
		roteiro.append((Pilha2[3], Pilha1[3]))
		print 'mova disco da Pilha%s para a Pilha%s' %(Pilha2[3],Pilha1[3])
	elif Pilha2[1] == 0 and ValorTopo1 != last:
		(Pilha1, Pilha2, last) = move(Pilha1,Pilha2)
		roteiro.append((Pilha1[3], Pilha2[3]))
		print 'mova disco da Pilha%s para a Pilha%s' %(Pilha1[3],Pilha2[3])
	return (Pilha1, Pilha2, last) 

def move(Pilha1, Pilha2): #mover da pilha 1 para a pilha 2
	Pilha2 = inserirPilha(Pilha2[3],Pilha2[0], len(Pilha2[0]), Pilha2[1], Pilha1[0][Pilha1[1]-1])
	Pilha1 = removerPilha(Pilha1[3],Pilha1[0],Pilha1[1], 0)
	last = Pilha2[0][Pilha2[1]-1]
	return(Pilha1, Pilha2, last)

Hanoi(3)