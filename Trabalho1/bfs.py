import time

inicio = time.time()

# g = Graph()
# g.add_vertices(7)
# g.add_edges([(0,3),(0,4),(1,0),(1,3),(1,5),(2,6),(3,4)])
# print(g)
# plot(g)

# Caso 1
# lista = {'1':['2'],'3':['4'],'2':['3'],'4':['1']}
# Caso 2
# lista = {'1':['4','5'],'2':['1','4','6'],'3':['7'],'4':['1','2','5'],'5':['1','4'],'6':['2'],'7':['3']}
# Caso 3
#lista = {'1':['2','3','4','5'],'2':['1','3','4','5'],'3':['1','2','4','5'],'4':['1','2','3','5'],'5':['1','2','3','4']}

# grafo
lista = {'1':['4','5'],'2':['1','4','6'],'3':['7'],'4':['1','2','5'],'5':['1','4'],'6':['2'],'7':['3']}
explorados = []
fila = []

# inicia o loop da busca
for i in lista:
    # verificando se o nó foi explorado
    if i not in explorados:
        # adiciona o elemento a fila
        fila.append(i)
        print('Fila: ', fila)
        explorados.append(i)
        # se a fila não tiver vazia
        while not fila==[]:
            # pegando o primeiro elemento da fila
            u = fila.pop()
            print('Fila: ', fila)
            # verificando se v é adjacente de u
            for v in lista[u]:
                if v not in explorados:
                    explorados.append(v)
                    fila.append(v)
                    print('Fila:', fila)       

# tempo
fim = time.time()

print('Explorados: ', explorados)

print('tempo de execução: ', fim - inicio)
    