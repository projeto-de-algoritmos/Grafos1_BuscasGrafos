import time

inicio = time.time()

lista = [[1,2],[2,3],[3,4],[4,1]]
explorados = []

fila = []

for i in lista:
    if i not in explorados:
        fila.append(i)
        explorados.append(i)
        while not fila==[]:
            u = fila.pop()
            for v in lista:
                if v not in explorados:
                    # lista.remove([v,u])
                    explorados.append(v)
                    fila.append(v)
        

fim = time.time()

print(explorados)

print(fim - inicio)
    