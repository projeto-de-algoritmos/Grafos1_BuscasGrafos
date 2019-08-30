import time

inicio = time.time()

# g = Graph()
# g.add_vertices(7)
# g.add_edges([(0,3),(0,4),(1,0),(1,3),(1,5),(2,6),(3,4)])
# print(g)
# plot(g)

lista = {'1':['4','5'],'2':['1','4','6'],'3':['7'],'4':['1','2','5'],'5':['1','4'],'6':['2'],'7':['3']}
explorados = []

fila = []

for i in lista:
    if i not in explorados:
        fila.append(i)
        print('Fila: ', fila)
        explorados.append(i)
        while not fila==[]:
            u = fila.pop()
            print('Fila: ', fila)
            for v in lista[u]:
                if v not in explorados:
                    explorados.append(v)
                    fila.append(v)
                    print('Fila:', fila)       

fim = time.time()

print('Explorados: ', explorados)

print(fim - inicio)
    