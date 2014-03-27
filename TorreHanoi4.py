roteiro = []
def hanoi3(ndiscos, inicial=1, final=3):
    if ndiscos:
        hanoi3(ndiscos-1, inicial, 6-inicial-final)
        print "Mova o disco do pino %d para o pino %d" % (inicial, final)
        roteiro.append((inicial,final))
        hanoi3(ndiscos-1, 6-inicial-final, final)
    else:
    	return roteiro

def FrameStewart_Contagem(ndiscos,npinos):
    if  ndiscos == 1 and npinos > 1:
        return (1, 1)
    if npinos == 3:
        return (2**ndiscos - 1, 1)
    if npinos >= 3 and ndiscos > 0:
        sol = []
        for kdiscos in range(1, ndiscos):
        	sol.append((2*FrameStewart_Contagem(kdiscos,npinos)[0] + FrameStewart_Contagem(ndiscos-kdiscos,npinos-1)[0], kdiscos))
        return min(sol, key = lambda x: x[0])

print FrameStewart_Contagem(16,4)



